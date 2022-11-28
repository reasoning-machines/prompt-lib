# Given the path to a text file, queries alpa for each line in the file.
import json
import os.path
from datetime import datetime
from itertools import chain
import pathlib
from pprint import pprint
from typing import List
from tqdm import tqdm
import pandas as pd
import wandb
import dataclasses
import glob
import re
import os
import logging

from prompt_lib.openai_api import OpenaiAPIWrapper
from prompts.utils import PromptConfig, TaskConfig, make_task_file_from_config
from eval.eval_utils import read_jsonl

logging.basicConfig(level=logging.INFO)


def run_inference(task_config: TaskConfig, num_inference_examples: int = None) -> None:
    """Query a language model API for each line in the file."""

    task_file = make_task_file_from_config(task_config).to_dict(orient="records")
    if num_inference_examples is not None:
        task_file = task_file[:num_inference_examples]

    # make output directory
    outdir = get_outdir(task_config)

    # remove cached examples from task_file

    cached_examples, thread_offset = load_cached_examples(outdir)

    task_file = [example for example in task_file if example["question"] not in cached_examples]
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
        thread_outputs = query_openai_over_inputs(batch, batch_idx, task_config)
        outputs.append(thread_outputs)
        progress_perc = round(len(outputs) * 100 / len(batched_tasks), 2)
        wandb.log({"progress_so_far": progress_perc})
        accuracy_so_far += task_config.eval_function(pd.DataFrame(thread_outputs))
        wandb.log({"accuracy_so_far": accuracy_so_far / len(outputs)})

        pd.DataFrame(thread_outputs).to_json(
            f"{outdir}/outputs_part{batch_idx + thread_offset}.jsonl",
            orient="records",
            lines=True,
        )

    outputs = pd.DataFrame(chain(*outputs))

    # post-process cached examples and newly queried examples
    for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
        cached = read_jsonl(r_file)
        outputs = pd.concat([outputs, cached])

    # remove duplicates
    outputs = outputs.drop_duplicates(subset=["question"])

    wandb.log({"accuracy": task_config.eval_function(outputs)})
    wandb.log({"num_examples": len(outputs)})
    wandb.log({"num_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    logging.info(f"Number of successful queries: {len(outputs)}")
    outputs.to_json(f"{outdir}/outputs.jsonl", orient="records", lines=True)

    with open(f"{outdir}/task_config.json", "w") as f:
        f.write(json.dumps(task_config.to_dict(), indent=4))


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
                cached_examples.add(row["question"])
            part_idx = re.search("outputs_part(\d+).jsonl", os.path.basename(r_file)).group(1)
            thread_offset = max(thread_offset, int(part_idx))
        thread_offset += 1
    return cached_examples, thread_offset


def get_outdir(task_config):
    if task_config.cached_timestamp is None:
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    else:
        time_stamp = task_config.cached_timestamp

    outdir = f"data/logs/{task_config.task_id}/{task_config.model_name}/temp_{task_config.temperature}/seed_{task_config.seed}"
    if task_config.num_examples == -1:
        outdir += "/k_all/"
    else:
        outdir += f"/k_{task_config.num_examples}/"
    if task_config.tag is not None:
        outdir += f"{task_config.tag}/"

    outdir += f"{time_stamp}/"
    return outdir


def query_openai_over_inputs(
    inputs: List[dict],
    thread_id: int,
    task_config: TaskConfig,
    max_retries: int = 10,
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
            )

            entire_response = OpenaiAPIWrapper.parse_response(response)
            generated_answer = entire_response.split(task_config.prompt_config.inter_example_sep)[0]
            print(generated_answer)

            
            # nicely print the question and generated answer
            prompt_only = inputs[i]["question"].split(task_config.prompt_config.inter_example_sep)[
                :-1
            ]
            prompt_only = task_config.prompt_config.inter_example_sep.join(prompt_only)
            
            question = inputs[i]["question"].split(task_config.prompt_config.inter_example_sep)[-1]
            logging.info("\n" + f"Question ({i}): {question}")
            logging.info("\n" + f"Answer ({i}): {generated_answer}")
            outputs.append(
                {
                    "prompt": prompt_only,
                    "question": question,
                    "answer": inputs[i]["answer"],
                    "generated_answer": generated_answer,
                    "entire_response": entire_response,  # everything generated by the model
                }
            )
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


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str)
    args.add_argument("--num_questions_per_thread", type=int, default=100)
    args.add_argument("--max_tokens", type=int, default=100)
    args.add_argument("--num_examples", type=int, default=-1)
    args.add_argument("--timeout", type=int, default=720)
    args.add_argument("--name", type=str)
    args.add_argument("--seed", type=int)
    args.add_argument("--cot_task", action="store_true")

    args.add_argument("--model_name", type=str, default="code-davinci-002")
    args.add_argument("--max_requests_per_min", type=int, default=20)
    args.add_argument("--cached_timestamp", type=str, default=None)
    args.add_argument("--is_debug", action="store_true")

    args.add_argument("--question_prefix", type=str, default="Q: ")
    args.add_argument("--answer_prefix", type=str, default="A: ")
    args.add_argument("--final_answer_prefix", type=str, default="The answer is ")
    args.add_argument("--intra_example_sep", type=str, default="\n")
    args.add_argument("--inter_example_sep", type=str, default="\n\n")
    args.add_argument("--temperature", type=float, default=0.0)

    args.add_argument(
        "--eval_function",
        type=str,
        default="get_exact_match_acc",
        help="The function to use for evaluation. Should be defined in scripts/eval.py. The signature should be the same as `get_exact_match_acc`",
    )

    args.add_argument("--num_inference_examples", type=int, default=None)

    args.add_argument("--tag", type=str, default=None)
    args.add_argument("--wandb_project", type=str, default="cot")

    args = args.parse_args()

    prompt_config = PromptConfig.from_args(args)

    pprint(prompt_config)
    assert args.seed is not None

    if args.name is None:
        args.name = args.task_id

    task_config = TaskConfig(
        task_id=args.task_id,
        num_questions_per_thread=args.num_questions_per_thread,
        max_tokens=args.max_tokens,
        num_examples=args.num_examples,
        timeout=args.timeout,
        seed=args.seed,
        is_cot_task=args.cot_task,
        model_name=args.model_name,
        cached_timestamp=args.cached_timestamp,
        max_requests_per_min=args.max_requests_per_min,
        prompt_config=prompt_config,
        tag=args.tag,
        temperature=args.temperature,
        eval_function=args.eval_function,
    )

    if args.is_debug:
        wandb.init(mode="disabled")
    else:
        wandb.init(
            project=args.wandb_project, config=dataclasses.asdict(task_config), name=args.name
        )

    run_inference(task_config=task_config, num_inference_examples=args.num_inference_examples)
