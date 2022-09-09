# Given the path to a text file, queries alpa for each line in the file.
from datetime import datetime
from itertools import chain
import pathlib
import sys
from typing import List
from tqdm import tqdm
import pandas as pd
from joblib import Parallel, delayed
import wandb
import dataclasses


from alpa_api import call_alpa_endpoint
from eval import get_exact_match_acc
from prompts.utils import TaskConfig, make_task_file_from_config

def query_alpa(
    task_config: TaskConfig
) -> None:
    """Query alpa for each line in the file."""

    task_file = make_task_file_from_config(task_config).to_dict(orient="records")

    num_chunks = len(task_file) // task_config.num_questions_per_thread
    load_per_task = []
    for i in range(num_chunks):
        load_per_task.append(
            (task_file[i * task_config.num_questions_per_thread : (i + 1) * task_config.num_questions_per_thread], i)
        )

    if len(task_file) % task_config.num_questions_per_thread != 0:
        load_per_task.append((task_file[num_chunks * task_config.num_questions_per_thread :], num_chunks))

    # outputs = []
    # for (input, task_idx) in tqdm(load_per_task):
    #     outputs.append(query_alpa_over_inputs(input, task_idx, max_tokens))

    outputs = Parallel(n_jobs=-1, verbose=10)(
        delayed(query_alpa_over_inputs)(input, thread_id, task_config)
        for input, thread_id in load_per_task
    )

    outputs = chain(*outputs)

    outputs = pd.DataFrame(outputs)

    wandb.log({"accuracy": get_exact_match_acc(outputs)})
    wandb.log({"num_examples": len(outputs)})
    wandb.log({"num_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    # store outputs in data/logs/task_id/time_stamp/outputs.csv
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pathlib.Path(f"data/logs/{task_config.task_id}/{time_stamp}").mkdir(parents=True, exist_ok=True)
    outputs.to_json(f"data/logs/{task_config.task_id}/{time_stamp}/outputs.jsonl", orient="records", lines=True)


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


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str)
    args.add_argument("--num_questions_per_thread", type=int, default=100)
    args.add_argument("--max_tokens", type=int, default=60)
    args.add_argument("--num_examples", type=int, default=0)
    args.add_argument("--timeout", type=int, default=720)
    args.add_argument("--name", type=str)
    args.add_argument("--seed", type=int)
    args.add_argument("--cot_task", action="store_true")


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
    )

    wandb.init(project="alpa", config=dataclasses.asdict(task_config), name=args.name)



    query_alpa(
        task_config=task_config
    )
