import sys
sys.path.append("prompt-lib")  # to allow imports from outside the project directory
import os
from prompt_lib.prompts.gsm import gsm_task_id_to_prompt
from prompt_lib.prompts.sports import sports_task_id_to_prompt
from prompt_lib.prompts.date import date_task_id_to_prompt
from prompt_lib.prompts.sorting import sorting_task_id_to_prompt
from prompt_lib.prompts.boolsimplify.boolsimplify import bool_simplify_taskid_to_prompt


from prompt_lib.prompts.plot_generation import plot_generation_task_id_to_prompt
from prompt_lib.prompts.human_eval import humaneval_task_id_to_prompt
from prompt_lib.prompts.quco_gsm import quco_gsm_task_id_to_prompt
from prompt_lib.prompts.example import PromptStr


task_id_to_prompt = dict()
task_id_to_prompt.update(gsm_task_id_to_prompt)
task_id_to_prompt.update(sports_task_id_to_prompt)
task_id_to_prompt.update(date_task_id_to_prompt)
task_id_to_prompt.update(sorting_task_id_to_prompt)
task_id_to_prompt.update(bool_simplify_taskid_to_prompt)
task_id_to_prompt.update(plot_generation_task_id_to_prompt)
task_id_to_prompt.update(humaneval_task_id_to_prompt)
task_id_to_prompt.update(quco_gsm_task_id_to_prompt)


def get_prompt_from_file(prompt_path: str) -> PromptStr:
    # see if path exists
    if not os.path.exists(prompt_path):
        if not os.path.exists("prompt-lib/" + prompt_path):
            raise ValueError(f"Path {prompt_path} does not exist")
        else:
            prompt_path = "prompt-lib/" + prompt_path
    with open(prompt_path) as f:
        prompt_str = f.read()
    return PromptStr(prompt_str)

for task_id, example_list_or_prompt_path in task_id_to_prompt.items():
    if isinstance(example_list_or_prompt_path, str):
        
        task_id_to_prompt[task_id] = get_prompt_from_file(example_list_or_prompt_path)

def update_task_id_to_prompt_with_dynamic_import(import_module_name: str):
    import importlib
    import_module = importlib.import_module(import_module_name)
    task_id_to_prompt.update(import_module.task_id_to_prompt)
    for task_id, example_list_or_prompt_path in import_module.task_id_to_prompt.items():
        if isinstance(example_list_or_prompt_path, str):
            try:
                task_id_to_prompt[task_id] = get_prompt_from_file(example_list_or_prompt_path)
            except ValueError:
                print(f"Could not find prompt for {task_id} in {example_list_or_prompt_path}")

try:
    # update_task_id_to_prompt_with_dynamic_import("quco_prompts.prompt_list")
    update_task_id_to_prompt_with_dynamic_import("pir_prompts.prompt_list")
except ModuleNotFoundError as e:
    pass # no quco prompts

# TODO: make the above dynamic import more robust

if __name__ == '__main__':
    import argparse
    from prompt_lib.prompts.utils import format_prompt, PromptConfig

    args = argparse.ArgumentParser()
    args.add_argument("--task_id", type=str)
    args.add_argument("--num_examples", type=int, default=-1)
    args.add_argument("--seed", type=int)
    args.add_argument("--cot_task", action="store_true")

    args.add_argument("--question_prefix", type=str, default="Q: ")
    args.add_argument("--answer_prefix", type=str, default="A: ")
    args.add_argument("--final_answer_prefix", type=str, default="The answer is ")
    args.add_argument("--intra_example_sep", type=str, default="\n")
    args.add_argument("--inter_example_sep", type=str, default="\n\n")
    args.add_argument("--temperature", type=float, default=0.0)
    
    
    args = args.parse_args()

    prompt_config = PromptConfig.from_args(args)
    
    prompt_str = format_prompt(
        prompt_examples=task_id_to_prompt[args.task_id],
        prompt_config=prompt_config,
        num_examples=args.num_examples,
        seed=args.seed,
        is_cot_prompt=args.cot_task,
    )
    
    print(prompt_str)
    
    # update_task_id_to_prompt_with_dynamic_import("quco_prompts.prompt_list")
    # prompt_str = format_prompt(
    #     prompt_examples=task_id_to_prompt["gsmhard_interactive"],
    #     prompt_config=prompt_config,
    #     num_examples=args.num_examples,
    #     seed=args.seed,
    #     is_cot_prompt=args.cot_task,
    # )
    # print(prompt_str)
    