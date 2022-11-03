# Given the path to a text file, queries alpa for each line in the file.
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

from openai_api import OpenaiAPIWrapper
from scripts.eval import get_exact_match_acc
from prompts.utils import PromptConfig, TaskConfig, make_task_file_from_config


def run_inference(task_config: TaskConfig) -> None:
    """Query a language model API for each line in the file."""

    task_file = make_task_file_from_config(task_config).to_dict(orient="records")
    if task_config.cached_timestamp is None:
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    else:
        time_stamp = task_config.cached_timestamp

    outdir = f"data/logs/{task_config.task_id}/{time_stamp}/k{task_config.num_examples}/"
    if task_config.tag is not None:
        outdir += f"{task_config.tag}/"

    cached_examples = set()
    thread_offset = 0
    if pathlib.Path(outdir).exists():
        for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
            cached = pd.read_json(r_file, orient="records", lines=True)
            for i, row in cached.iterrows():
                cached_examples.add(row["question"])
            part_idx = re.search('outputs_part(\d+).jsonl',
                                  os.path.basename(r_file)).group(1)
            thread_offset = max(thread_offset, int(part_idx))
        thread_offset += 1


    # remove cached examples from task_file
    task_file = [example for example in task_file if example['question'] not in cached_examples]
    print(f'Found {len(cached_examples)} cached examples, {len(task_file)} examples to query')

    pathlib.Path(f"{outdir}").mkdir(parents=True, exist_ok=True)

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

    outputs = []
    accuracy_so_far = 0

    for (input, thread_id) in tqdm(load_per_task):
        thread_outputs = query_openai_over_inputs(input, thread_id, task_config)
        outputs.append(thread_outputs)
        progress_perc = round(len(outputs) * 100 / len(load_per_task), 2)
        wandb.log({"progress_so_far": progress_perc})
        accuracy_so_far += get_exact_match_acc(pd.DataFrame(thread_outputs))
        wandb.log({"accuracy_so_far": accuracy_so_far / len(outputs)})

        
        pd.DataFrame(thread_outputs).to_json(
            f"{outdir}/outputs_part{thread_id + thread_offset}.jsonl",
            orient="records",
            lines=True,
        )

    outputs = pd.DataFrame(chain(*outputs))

    # post-process cached examples and newly queried examples
    for r_file in glob.glob(f"{outdir}/outputs_part*.jsonl"):
        cached = pd.read_json(r_file, orient="records", lines=True)
        outputs = pd.concat([outputs, cached])

    # remove duplicates
    outputs = outputs.drop_duplicates(subset=["question"])
    # delete bck_outdir

    wandb.log({"accuracy": get_exact_match_acc(outputs)})
    wandb.log({"num_examples": len(outputs)})
    wandb.log({"num_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    # store outputs in data/logs/task_id/time_stamp/outputs.csv





    print(f"Number of successful queries: {len(outputs)}")
    outputs.to_json(
        f"{outdir}/outputs.jsonl", orient="records", lines=True
    )



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
                stop_token=task_config.prompt_config.question_prefix,  # generate till the model starts generating a new question
            )

            print(OpenaiAPIWrapper.parse_response(response))
            
            outputs.append(
                {
                    "question": inputs[i]["question"],
                    "generated_answer": OpenaiAPIWrapper.parse_response(response),
                    "answer": inputs[i]["answer"],
                }
            )
            i += 1
            pbar.update(1)

        except Exception as e:
            print(f"Exception: {e}")
            if "code" not in task_config.model_name:  # usually codex models throw rate limit errors
                i += 1
            elif num_retries < max_retries:
                num_retries += 1
                print("Retrying...")
                continue
            else:
                num_retries = 0
                i += 1
                print("Skipping...")
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
    
    args.add_argument("--tag", type=str, default=None)
    
    
    
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
        temperature=args.temperature
    )

    if args.is_debug:
        wandb.init(mode="disabled")
    else:
        wandb.init(project="alpa", config=dataclasses.asdict(task_config), name=args.name)

    run_inference(task_config=task_config)
