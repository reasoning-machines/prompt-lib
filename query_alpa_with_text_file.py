# Given the path to a text file, queries alpa for each line in the file.
from itertools import chain
from typing import List
from tqdm import tqdm
import pandas as pd
from joblib import Parallel, delayed
import wandb


from alpa_api import call_alpa_endpoint
from eval import get_exact_match_acc

def query_alpa(
    input_file_path: str,
    output_path: str,
    num_inputs_per_parallel_query: int,
    max_tokens: int,
    cut_examples: int,
    timeout: int,
) -> None:
    """Query alpa for each line in the file."""

    # first count the number of lines in the file
    inputs = pd.read_json(input_file_path, lines=True, orient="records").to_dict("records")

    num_chunks = len(inputs) // num_inputs_per_parallel_query
    load_per_task = []
    for i in range(num_chunks):
        load_per_task.append(
            (inputs[i * num_inputs_per_parallel_query : (i + 1) * num_inputs_per_parallel_query], i)
        )

    if len(inputs) % num_inputs_per_parallel_query != 0:
        load_per_task.append((inputs[num_chunks * num_inputs_per_parallel_query :], num_chunks))

    # outputs = []
    # for (input, task_idx) in tqdm(load_per_task):
    #     outputs.append(query_alpa_over_inputs(input, task_idx, max_tokens))

    outputs = Parallel(n_jobs=-1, verbose=10)(
        delayed(query_alpa_over_inputs)(input, task_id, max_tokens, cut_examples, timeout)
        for input, task_id in load_per_task
    )

    outputs = chain(*outputs)

    outputs = pd.DataFrame(outputs)

    wandb.log({"accuracy": get_exact_match_acc(outputs)})

    wandb.log({"num_examples": len(outputs)})
    wandb.log({"num_examples_with_answer": len(outputs[outputs["answer"].notnull()])})
    wandb.log({"outputs": wandb.Table(dataframe=outputs)})

    outputs.to_json(output_path, orient="records", lines=True)


def query_alpa_over_inputs(
    inputs: List[dict], task_id: int, max_tokens: int, cut_examples: int, timeout: int
) -> List[dict]:
    outputs = []
    for input in tqdm(inputs, total=len(inputs), desc=f"Querying alpa [task_id={task_id}]"):
        try:
            question = input["question"]
            question = "Q:".join(question.split("Q:")[cut_examples:]).strip()
            generated_answer = call_alpa_endpoint(
                text=question, max_tokens=max_tokens, timeout=timeout
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
    args.add_argument("--input_file_path", type=str)
    args.add_argument("--output_path", type=str)
    args.add_argument("--num_inputs_per_parallel_query", type=int, default=100)
    args.add_argument("--max_tokens", type=int, default=60)
    args.add_argument("--cut_examples", type=int, default=0)
    args.add_argument("--timeout", type=int, default=360)
    args.add_argument("--name", type=str)
    args = args.parse_args()

    config = vars(args)
    wandb.init(project="alpa", config=config, name=args.name)

    query_alpa(
        args.input_file_path,
        args.output_path,
        num_inputs_per_parallel_query=args.num_inputs_per_parallel_query,
        max_tokens=args.max_tokens,
        cut_examples=args.cut_examples,
        timeout=args.timeout,
    )
