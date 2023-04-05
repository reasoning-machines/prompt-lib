# Given the path to a text file, queries alpa for each line in the file.
import json
import os.path
from datetime import datetime
from itertools import chain
import pathlib
import sys
from typing import List
from tqdm import tqdm
import pandas as pd
import wandb
import glob
import re
import os
import logging

from prompt_lib.backends.openai_api import OpenaiAPIWrapper
from prompt_lib.prompts.utils import TaskConfig, make_task_file_from_config, get_question_from_prompt
from prompt_lib.eval.eval_utils import read_jsonl

logging.basicConfig(level=logging.INFO)


def inference_loop(
    task_config: TaskConfig, num_inference_examples: int = None, num_completions: int = 1
) -> None:
    """Query a language model API for each line in the file."""

    task_file = make_task_file_from_config(task_config).to_dict(orient="records")
    if num_inference_examples is not None:
        task_file = task_file[:num_inference_examples]

    # make output directory
    outdir = get_outdir(task_config, num_completions)

    # remove cached examples from task_file

    cached_examples, thread_offset = load_cached_examples(outdir)

    task_file = [
        example
        for example in task_file
        if get_question_from_prompt(example["question"], task_config) not in cached_examples
    ]
    logging.info(
        f"Found {len(cached_examples)} cached examples, {len(task_file)} examples to query"
    )


    pathlib.Path(f"{outdir}").mkdir(parents=True, exist_ok=True)

    # split tasks into subtasks. This is redundant for now, but will be useful when we want to parallelize. Also helps with caching/restarting, as intermediate results are saved.
    batched_tasks = create_task_batches(task_config, task_file)

    outputs = []
    accuracy_so_far = 0

    # run inference
    for (batch, batch_idx) in tqdm(batched_tasks):
        thread_outputs = query_openai_over_inputs(
            batch, batch_idx, task_config=task_config, num_completions=num_completions
        )
        outputs.append(thread_outputs)
        progress_perc = round(len(outputs) * 100 / len(batched_tasks), 2)
        wandb.log({"progress_so_far": progress_perc})
        pd.DataFrame(thread_outputs).to_json(
            f"{outdir}/outputs_part{batch_idx + thread_offset}.jsonl",
            orient="records",
            lines=True,
        )
        accuracy_so_far += task_config.eval_function(pd.DataFrame(thread_outputs))
        wandb.log({"accuracy_so_far": accuracy_so_far / len(outputs)})

    outputs = pd.DataFrame(chain(*outputs))

    # post-process cached examples and newly queried examples
    for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
        cached = read_jsonl(r_file)
        outputs = pd.concat([outputs, cached])

    # remove duplicates
    outputs = outputs.drop_duplicates(subset=["question"]).drop("logprobs", axis=1)

    wandb.log({"accuracy": task_config.eval_function(outputs)})
    wandb.log({"num_inference_examples": len(outputs)})
    wandb.log({"num_inference_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})



    logging.info(f"Number of successful queries: {len(outputs)}")
    outputs.to_json(f"{outdir}/outputs.jsonl", orient="records", lines=True)

    with open(f"{outdir}/task_config.json", "w") as f:
        f.write(json.dumps(task_config.to_dict(), indent=4))
    return outputs


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


def load_cached_examples(outdir):
    """Loads cached examples from a directory."""
    cached_examples = set()
    thread_offset = 0
    if pathlib.Path(outdir).exists():
        for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
            cached = read_jsonl(r_file)
            for i, row in cached.iterrows():
                cached_examples.add(row["question"].strip())
            part_idx = re.search("outputs_part(\d+).jsonl", os.path.basename(r_file)).group(1)
            thread_offset = max(thread_offset, int(part_idx))
        thread_offset += 1
    return cached_examples, thread_offset


def get_outdir(task_config: TaskConfig, num_completions: int) -> str:
    if task_config.cached_timestamp is None:
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    else:
        time_stamp = task_config.cached_timestamp

    outdir = f"data/logs/{task_config.task_id}/{task_config.model_name}/temp_{task_config.temperature}/seed_{task_config.seed}/num_completions_{num_completions}/"
    if task_config.num_prompt_examples == -1:
        outdir += "/k_all/"
    else:
        outdir += f"/k_{task_config.num_prompt_examples}/"
    if task_config.tag is not None:
        outdir += f"{task_config.tag}/"

    outdir += f"{time_stamp}/"
    return outdir


def query_openai_over_inputs(
    inputs: List[dict],
    thread_id: int,
    task_config: TaskConfig,
    max_retries: int = 10,
    num_completions: int = 1,
) -> List[dict]:
    outputs = []
    i = 0
    n = len(inputs)

    pbar = tqdm(total=n, desc=f"Querying openai [thread_id={thread_id}]")
    num_retries = 0

    while i < n:

        try:
            response = OpenaiAPIWrapper.call(
                temperature=task_config.temperature,
                prompt=inputs[i]["question"],
                max_tokens=task_config.max_tokens,
                engine=task_config.model_name,
                stop_token=task_config.prompt_config.inter_example_sep,  # generate till the model starts generating a new question
                num_completions=num_completions,
            )
            prompt_only = inputs[i]["question"].split(task_config.prompt_config.inter_example_sep)[
                :-1
            ]
            prompt_only = task_config.prompt_config.inter_example_sep.join(prompt_only)

            question = inputs[i]["question"].split(task_config.prompt_config.inter_example_sep)[-1]

            res = {
                "prompt": prompt_only,
                "question": question,
                "answer": inputs[i]["answer"],
                "entire_prompt": inputs[i]["question"],
            }
            if num_completions == 1:
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
                if "logprobs" in response["choices"][0]:
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
            logging.info(f"Exception: {e}")
            if "code" not in task_config.model_name:  # usually codex models throw rate limit errors
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
    if task_config.prompt_config.inter_example_sep in response:
        answer = response.split(task_config.prompt_config.inter_example_sep)[0]
    else:
        answer = response
    return answer
