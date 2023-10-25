# Given the path to a text file, queries alpa for each line in the file.
import json
import os.path
from datetime import datetime
from itertools import chain
import pathlib
import sys
import time
from typing import List
from tqdm import tqdm
import pandas as pd
import wandb
import glob
import re
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from prompt_lib.backends.openai_api import OpenaiAPIWrapper
from prompt_lib.prompts.utils import (
    TaskConfig,
    make_task_file_from_config,
    get_question_from_prompt,
)
from prompt_lib.eval.eval_utils import read_jsonl

logging.basicConfig(level=logging.INFO)



def inference_loop(task_config: TaskConfig, num_threads: int = 1) -> None:
    task_file = make_task_file_from_config(task_config).to_dict(orient="records")

    if task_config.num_inference_examples != -1:
        task_file = task_file[: task_config.num_inference_examples]
    outdir = get_outdir(task_config)



    cached_examples, cached_prompts, thread_offset = load_cached_examples(outdir, task_config)
    task_file = [
        example for example in task_file if not (
            (task_config.num_prompt_examples > 0 and get_question_from_prompt(example["question"], task_config) in cached_examples) or
            example["question"] in cached_examples or 
            example["question"] in cached_prompts
        )
    ]

    print(
        f"Found {len(cached_examples)} cached examples, {len(task_file)} examples to query"
    )

    # sys.exit(0)

    pathlib.Path(f"{outdir}").mkdir(parents=True, exist_ok=True)

    if num_threads > 1:  # if we are parallelizing, we need to split the task file into batches
        task_config.num_questions_per_thread = len(task_file) // num_threads

    batched_tasks = create_task_batches(task_config, task_file)

    outputs = []
    accuracy_so_far = 0
    for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
        cached = read_jsonl(r_file)
        outputs.extend(cached)

    # Parallel processing using tqdm and executor.map
    batch_data = [(batch, batch_idx, task_config, thread_offset, outdir) for (batch, batch_idx) in batched_tasks]
    
    assert len(batch_data) > 0, "No records to process!"

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for thread_outputs in tqdm(executor.map(process_batch, batch_data), total=len(batched_tasks), desc="Processing batches"):
            outputs.append(thread_outputs)
            progress_perc = round(len(outputs) * 100 / len(batched_tasks), 2)
            wandb.log({"progress_so_far": progress_perc})
            accuracy_so_far += task_config.eval_function(pd.DataFrame(thread_outputs))
            wandb.log({"accuracy_so_far": accuracy_so_far / len(outputs)})

    outputs = pd.DataFrame(chain(*outputs))

    if "logprobs" in outputs.columns:
        outputs = outputs.drop("logprobs", axis=1)

    wandb.log({"accuracy": task_config.eval_function(outputs)})
    wandb.log({"num_inference_examples": len(outputs)})
    wandb.log({"num_inference_examples_with_answer": len(outputs[outputs["answer"].notnull()])})

    outputs = outputs.dropna()
    for col in outputs.columns:
        outputs[col] = outputs[col].astype(str)
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    logging.info(f"Number of successful queries: {len(outputs)}")
    outputs.to_json(f"{outdir}/outputs.jsonl", orient="records", lines=True)

    with open(f"{outdir}/task_config.json", "w") as f:
        f.write(json.dumps(task_config.to_dict(), indent=4))
    return outputs


def process_batch(batch_data):
    batch, batch_idx, task_config, thread_offset, outdir = batch_data
    # print(batch)
    # print(f"Processing batch {batch_idx}...")
    # print(1/0)
    thread_outputs = run_inference_on_batch(batch, batch_idx, task_config=task_config)
    pd.DataFrame(thread_outputs).to_json(
        f"{outdir}/outputs_part{batch_idx + thread_offset}.jsonl",
        orient="records",
        lines=True,
    )
    return thread_outputs

def create_task_batches(task_config: TaskConfig, task_file: List) -> List:
    """Generates batches of tasks. Currently, we don't parallelize, but it's useful for caching and restarting.

    Args:
        task_config (_type_): TaskConfig
        task_file (List): List of tasks

    Returns:
        List of (batch, batch_idx) tuples
    """
    num_chunks = len(task_file) // task_config.num_questions_per_thread
    load_per_task = []
    for i in range(num_chunks):
        load_per_task.append(
            (
                task_file[
                    i
                    * task_config.num_questions_per_thread : (i + 1)
                    * task_config.num_questions_per_thread
                ],
                i,
            )
        )

    if len(task_file) % task_config.num_questions_per_thread != 0:
        load_per_task.append(
            (task_file[num_chunks * task_config.num_questions_per_thread :], num_chunks)
        )

    return load_per_task


def load_cached_examples(outdir, task_config):
    """Loads cached examples from a directory."""
    cached_examples = set()
    cached_prompts = set()
    thread_offset = 0
    if pathlib.Path(outdir).exists():
        for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
            cached = read_jsonl(r_file)
            for i, row in cached.iterrows():
                cached_examples.add(get_question_from_prompt(row["question"], task_config))
                cached_prompts.add(row["entire_prompt"])
            part_idx = re.search("outputs_part(\d+).jsonl", os.path.basename(r_file)).group(1)
            thread_offset = max(thread_offset, int(part_idx))
        thread_offset += 1
    return cached_examples, cached_prompts, thread_offset


def get_outdir(task_config: TaskConfig) -> str:
    if task_config.cached_timestamp is None:
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    else:
        print(f"Using cached timestamp: {task_config.cached_timestamp}")
        time_stamp = task_config.cached_timestamp

    outdir = f"data/logs/{task_config.task_id}/{task_config.model_name}/temp_{task_config.temperature}/seed_{task_config.seed}/num_completions_{task_config.num_completions}/"
    if task_config.num_prompt_examples == -1:
        outdir += "/k_all/"
    else:
        outdir += f"/k_{task_config.num_prompt_examples}/"
    if task_config.tag is not None:
        outdir += f"{task_config.tag}/"

    outdir += f"{time_stamp}/"
    return outdir


def run_inference_on_batch(
    rows: List[dict],
    thread_id: int,
    task_config: TaskConfig,
    max_retries: int = 10,
) -> List[dict]:
    outputs = []
    i = 0
    n = len(rows)

    pbar = tqdm(total=n, desc=f"Querying {task_config.model_name} {task_config.task_id} [thread_id={thread_id}]")
    num_retries = 0

    while i < n:

        try:
            response = OpenaiAPIWrapper.call(
                temperature=task_config.temperature,
                prompt=rows[i]["question"],
                max_tokens=task_config.max_tokens,
                engine=task_config.model_name,
                stop_token=task_config.prompt_config.inter_example_sep,  # generate till the model starts generating a new question
                num_completions=task_config.num_completions,
            )
            if task_config.prompt_config.inter_example_sep:
                prompt_only = rows[i]["question"].split(task_config.prompt_config.inter_example_sep)[
                    :-1
                ]
                prompt_only = task_config.prompt_config.inter_example_sep.join(prompt_only)

                question = rows[i]["question"].split(task_config.prompt_config.inter_example_sep)[-1]
            else:  # zero-shot, everything is the prompt
                prompt_only = rows[i]["question"]
                question = rows[i]["question"]

            res = {
                "prompt": prompt_only,
                "question": question,
                "answer": rows[i]["answer"],
                "entire_prompt": rows[i]["question"],
            }
            res.update({k: v for k, v in rows[i].items() if k not in res})
            if task_config.num_completions == 1:
                entire_response = OpenaiAPIWrapper.get_first_response(response)
                generated_answer = extract_answer_from_response(entire_response, task_config)
                
                # nicely print the question and generated answer

                logging.info("\n" + f"Question ({i}):" + "\n" + question)
                logging.info("\n" + f"Answer ({i}):" + "\n" + generated_answer)
                res.update(
                    {
                        "generated_answer": generated_answer,
                        "entire_response": entire_response,  # everything generated by the model
                    }
                )
                if "choices" in response and "logprobs" in response["choices"][0]:
                    res.update({"logprobs": response["choices"][0]["logprobs"]})

            else:
                all_responses = OpenaiAPIWrapper.get_all_responses(response)

                generated_answer_list = [response["generated_answer"] for response in all_responses]
                logprobs = [response["logprobs"] for response in all_responses]

                generated_answers = [
                    extract_answer_from_response(r, task_config) for r in generated_answer_list
                ]
                res.update(
                    {
                        "generated_answers": generated_answers,
                        "generated_answer": generated_answers[0],
                        "logprobs": logprobs,
                    }
                )
            outputs.append(res)
            i += 1
            pbar.update(1)

        except Exception as e:
            raise e
            logging.info(f"Exception: {e}")
            if "code" not in task_config.model_name:
                i += 1
            elif num_retries < max_retries:
                num_retries += 1
                logging.info("Retrying...")
                continue
            else:
                num_retries = 0
                i += 1
                logging.info("Skipping...")
    return outputs


def extract_answer_from_response(response, task_config: TaskConfig) -> str:
    """Extracts the answer from the response generated by LLM.

    Args:
        response (str): Response from the model
        task_config (TaskConfig): TaskConfig

    Returns:
        str: Answer
    """
    if task_config.prompt_config.inter_example_sep and task_config.prompt_config.inter_example_sep in response:
        answer = response.split(task_config.prompt_config.inter_example_sep)[0]
    else:
        answer = response
    return answer
