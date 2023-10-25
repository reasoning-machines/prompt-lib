# Given the path to a text file, queries alpa for each line in the file.
import json
import os
from pprint import pprint
import openai
import wandb
import dataclasses
import logging

import yaml

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
    _, file_ext = os.path.splitext(config_path)

    with open(config_path, "r") as f:
        if file_ext.lower() == '.yaml' or file_ext.lower() == '.yml':
            config = yaml.safe_load(f)
        elif file_ext.lower() == '.json':
            config = json.load(f)
        else:
            raise ValueError("Unsupported configuration file format. Please use a JSON or YAML file.")

    prompt_fields = PromptConfig.__dataclass_fields__.keys()
    task_config_fields = TaskConfig.__dataclass_fields__.keys()
    

    critical_fields = [
        "task_id",
        "model_name",
    ]
    for field in critical_fields:
        if field not in config and (field not in args or getattr(args, field) is None):
            raise ValueError(f"Field {field} not found in config file {config_path} or in args")

    if "prompt_config" not in config:
        config["prompt_config"] = {}

    remaining_args = {}
    for k in vars(args):
        default_val = getattr(args, k)
        if k in prompt_fields and k not in config["prompt_config"]:
            if k in config:
                config["prompt_config"][k] = config[k]
            else:
                config["prompt_config"][k] = default_val
        elif k in task_config_fields and k not in config:
            config[k] = default_val
        elif k in config:
            remaining_args[k] = config[k]
        else:
            remaining_args[k] = default_val

    # Update the args object with the remaining arguments
    for k, v in remaining_args.items():
        setattr(args, k, v)
    task_config = TaskConfig.from_config_dict(config)
    return task_config, args

if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str, help="Task ID for the specific task. Always has the format <dataset>_<task>, where <dataset>.jsonl is expected to be in ${PWD}/data/<dataset>.jsonl. It should be a jsonl with two fields: `input` and `output`.")
    args.add_argument("--num_questions_per_thread", type=int, default=200, help="Number of questions to run per thread")
    args.add_argument("--max_tokens", type=int, default=100, help="Maximum number of tokens in completion")
    args.add_argument("--num_prompt_examples", type=int, default=-1, help="Number of prompt examples to use (-1 for all)")
    args.add_argument("--name", type=str, required=False, help="Name of the run")
    args.add_argument("--seed", type=int, required=False, help="Seed for randomization. Used to decided the order of examples. Not applicable if a text file is supplied as the prompt", default=0)
    args.add_argument("--cot_task", action="store_true", help="Indicate if it's a COT task")
    args.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature for the model")

    args.add_argument("--model_name", type=str, default="code-davinci-002", help="Model name to use for inference")
    args.add_argument("--cached_timestamp", type=str, default=None, help="Timestamp for cached data (None for no cache)")
    args.add_argument("--is_debug", action="store_true", help="Enable debug mode (disables wandb)")

    # prompt config fields: decide how the prompt is constructed. See docs/prompt.md for more details
    args.add_argument("--question_prefix", type=str, default="Q: ", help="Prefix for questions")
    args.add_argument("--answer_prefix", type=str, default="A: ", help="Prefix for answers")
    args.add_argument("--final_answer_prefix", type=str, default="The answer is ", help="Prefix for the final answer")
    args.add_argument("--intra_example_sep", type=str, default="\n", help="Separator within examples")
    args.add_argument("--inter_example_sep", type=str, default="\n\n", help="Separator between examples")

    # wandb stuff
    args.add_argument("--tag", type=str, default=None, help="Tag for the run")
    args.add_argument("--wandb_project", type=str, default="cot", help="Wandb project name")
    args.add_argument("--wandb_entity", type=str, default="cot", help="Wandb entity name")
    args.add_argument("--config_file", type=str, default=None, help="Path to the configuration file")


    args.add_argument(
        "--eval_function",
        type=str,
        default="get_exact_match_acc",
        help="The function to use for evaluation. Should be defined in scripts/eval.py. The signature should be the same as `get_exact_match_acc`",
    )

    args.add_argument("--num_inference_examples", type=int, default=-1, help="Number of examples for which inference will run.")


    
    args.add_argument("--num_completions", type=int, default=1, help="Number of completions to generate per prompt")
    
    args.add_argument("--num_threads", type=int, default=1, help="Number of threads to use for inference")
    
    args.add_argument("--base_url", type=str, default=None, help="Base URL for OpenAI API, used for vllm servers.")
    
    args = args.parse_args()

    args.is_cot_task = args.cot_task

    if args.tag is None:
        args.tag = args.task_id

    if args.config_file is not None:

        task_config, args = read_config_and_populate_defaults(args.config_file, args)
        
    else:
        assert args.seed is not None
        prompt_config = PromptConfig.from_args(args)
        task_config = TaskConfig.from_args(args, prompt_config)

    if args.name is None:
        model_name_cleaned = task_config.model_name.replace("/", "_")
        args.name = f"{task_config.task_id}_{model_name_cleaned}_seed{task_config.seed}"
        if args.tag is None:
            args.name += f"_{task_config.tag}"
    
    if args.is_debug:
        wandb.init(mode="disabled")
    else:
        wandb.init(
            project=args.wandb_project, config=dataclasses.asdict(task_config), name=args.name, notes=args.tag, entity=args.wandb_entity if args.wandb_entity is not None else os.environ.get("WANDB_ENTITY", None)
        )

    # print(task_config)
    # sys.exit(0)
    print(task_config)
    if args.base_url is not None:
        openai.api_key = "EMPTY"
        openai.api_base = args.base_url
    print(task_config.prompt_config.inter_example_sep)
    inference_loop(task_config=task_config, num_threads=args.num_threads)
