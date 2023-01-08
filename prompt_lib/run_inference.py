# Given the path to a text file, queries alpa for each line in the file.
import json
from pprint import pprint
import wandb
import dataclasses
import logging

from prompt_lib.prompts.utils import PromptConfig, TaskConfig
from prompt_lib.inference import inference_loop

logging.basicConfig(level=logging.INFO)


def read_config_and_populate_defaults(config_path: str, args) -> dict:
    """Reads a json config file. For values that are not specified, uses default values.
    We want to supply the constructors for TaskConfig and PromptConfig with a dictionary with
    all the required fields. This function helps us do that.

    Args:
        config_path (str): path to config file

    Returns:
        dict: a dictionary with all the required fields.
    """
    with open(config_path, "r") as f:
        config = json.load(f)

    prompt_fields = PromptConfig.__dataclass_fields__.keys()
    task_config_fields = TaskConfig.__dataclass_fields__.keys()

    critical_fields = [
        "task_id",
        "model_name",
        "temperature",
        "seed",
        "num_prompt_examples",
        "num_questions_per_thread",
    ]
    for field in critical_fields:
        assert field in config, f"Field {field} not found in config file {config_path}"

    if "prompt_config" not in config:
        config["prompt_config"] = {}

    for k in vars(args):
        default_val = getattr(args, k)
        if k in prompt_fields and k not in config["prompt_config"]:
            config["prompt_config"][k] = default_val
        elif k in task_config_fields and k not in config:
            config[k] = default_val

    return TaskConfig.from_config_dict(config)


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str)
    args.add_argument("--num_questions_per_thread", type=int, default=100)
    args.add_argument("--max_tokens", type=int, default=100)
    args.add_argument("--num_prompt_examples", type=int, default=-1)
    args.add_argument("--name", type=str, required=False)
    args.add_argument("--seed", type=int, required=False)
    args.add_argument("--cot_task", action="store_true")
    args.add_argument("--temperature", type=float, default=0.0)

    args.add_argument("--model_name", type=str, default="code-davinci-002")
    args.add_argument("--cached_timestamp", type=str, default=None)
    args.add_argument("--is_debug", action="store_true")

    # prompt config fields: decide how the prompt is constructed
    args.add_argument("--question_prefix", type=str, default="Q: ")
    args.add_argument("--answer_prefix", type=str, default="A: ")
    args.add_argument("--final_answer_prefix", type=str, default="The answer is ")
    args.add_argument("--intra_example_sep", type=str, default="\n")
    args.add_argument("--inter_example_sep", type=str, default="\n\n")

    args.add_argument(
        "--eval_function",
        type=str,
        default="get_exact_match_acc",
        help="The function to use for evaluation. Should be defined in scripts/eval.py. The signature should be the same as `get_exact_match_acc`",
    )

    args.add_argument("--num_inference_examples", type=int, default=None)

    args.add_argument("--tag", type=str, default=None)
    args.add_argument("--wandb_project", type=str, default="cot")
    args.add_argument("--config_file", type=str, default=None)
    
    args.add_argument("--num_completions", type=int, default=1, help="Number of completions to generate per prompt")

    args = args.parse_args()

    if args.name is None:
        args.name = args.task_id

    if args.config_file is not None:

        task_config = read_config_and_populate_defaults(args.config_file, args)
    else:
        assert args.seed is not None
        prompt_config = PromptConfig.from_args(args)
        task_config = TaskConfig.from_args(args, prompt_config)

    pprint(prompt_config)

    if args.is_debug:
        wandb.init(mode="disabled")
    else:
        wandb.init(
            project=args.wandb_project, config=dataclasses.asdict(task_config), name=args.name
        )

    inference_loop(task_config=task_config, num_inference_examples=args.num_inference_examples, num_completions=args.num_completions)
