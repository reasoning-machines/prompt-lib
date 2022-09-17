# Given the path to a text file, queries alpa for each line in the file.
from datetime import datetime
from itertools import chain
import pathlib
import sys
import time
from typing import List
from tqdm import tqdm
import pandas as pd
from joblib import Parallel, delayed
import wandb
import dataclasses


from alpa_api import call_alpa_endpoint
from openai_api import OpenaiAPIWrapper
from eval import get_exact_match_acc
from prompts.utils import TaskConfig, make_task_file_from_config, maintain_request_per_minute


def query_alpa(task_config: TaskConfig) -> None:
    """Query alpa for each line in the file."""

    task_file = make_task_file_from_config(task_config).to_dict(orient="records")
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pathlib.Path(f"data/logs/{task_config.task_id}/{time_stamp}").mkdir(parents=True, exist_ok=True)

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

    if task_config.model_name == "alpa":
        outputs = Parallel(n_jobs=-1, verbose=10)(
            delayed(query_alpa_over_inputs)(input, thread_id, task_config)
            for input, thread_id in load_per_task
        )
    else:
        outputs = []
        for (input, thread_id) in tqdm(load_per_task):
            thread_outputs = query_openai_over_inputs(input, thread_id, task_config)
            outputs.append(thread_outputs)
            progress_perc = len(outputs) / len(load_per_task)
            progress_perc = f"{progress_perc:.2%}"
            wandb.log({"progress": progress_perc})

            
            pd.DataFrame(thread_outputs).to_json(
                f"data/logs/{task_config.task_id}/{time_stamp}/outputs_part{thread_id}.jsonl",
                orient="records",
                lines=True,
            )

    outputs = pd.DataFrame(chain(*outputs))

    wandb.log({"accuracy": get_exact_match_acc(outputs)})
    wandb.log({"num_examples": len(outputs)})
    wandb.log({"num_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    # store outputs in data/logs/task_id/time_stamp/outputs.csv

    outputs.to_json(
        f"data/logs/{task_config.task_id}/{time_stamp}/outputs.jsonl", orient="records", lines=True
    )


def query_alpa_over_inputs(
    inputs: List[dict], thread_id: int, task_config: TaskConfig
) -> List[dict]:
    outputs = []
    for input in tqdm(inputs, total=len(inputs), desc=f"Querying alpa [thread_id={thread_id}]"):
        try:
            question = input["question"]

            generated_answer = call_alpa_endpoint(
                text=question, max_tokens=task_config.max_tokens, timeout=task_config.timeout
            )
            outputs.append(
                {
                    "question": question,
                    "generated_answer": generated_answer,
                    "answer": input["answer"],
                }
            )
        except Exception as e:
            print(f"Error: {e}")
            continue
    return outputs


def query_openai_over_inputs(
    inputs: List[dict], thread_id: int, task_config: TaskConfig
) -> List[dict]:
    outputs = []
    time_begin = time.time()
    num_requests = 0
    i = 0
    n = len(inputs)

    pbar = tqdm(total=n, desc=f"Querying openai [thread_id={thread_id}]")
    while i < n:
        input = inputs[i]
        try:
            num_requests += 1
            maintain_request_per_minute(
                num_requests=num_requests,
                time_begin=time_begin,
                max_requests_per_min=task_config.max_requests_per_min,
                task_idx=thread_id,
            )
            question = input["question"]
            response = OpenaiAPIWrapper.call(
                prompt=question,
                max_tokens=task_config.max_tokens,
                engine=task_config.model_name,
                stop_token=task_config.prompt_config.inter_example_sep,
            )
            outputs.append(
                {
                    "question": question,
                    "generated_answer": OpenaiAPIWrapper.parse_response(response),
                    "answer": input["answer"],
                }
            )
            i += 1
            pbar.update(1)

        except Exception as e:
            print(f"Error: {e}")
            continue
    return outputs


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str)
    args.add_argument("--num_questions_per_thread", type=int, default=100)
    args.add_argument("--max_tokens", type=int, default=100)
    args.add_argument("--num_examples", type=int, default=0)
    args.add_argument("--timeout", type=int, default=720)
    args.add_argument("--name", type=str)
    args.add_argument("--seed", type=int)
    args.add_argument("--cot_task", action="store_true")

    args.add_argument("--model_name", type=str, default="code-davinci-002")
    args.add_argument("--max_requests_per_min", type=int, default=20)

    args = args.parse_args()

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
        max_requests_per_min=args.max_requests_per_min,
    )

    wandb.init(project="alpa", config=dataclasses.asdict(task_config), name=args.name)

    query_alpa(task_config=task_config)
