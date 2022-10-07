from prompts.gsm import gsm_task_id_to_prompt
from prompts.sports import sports_task_id_to_prompt
from prompts.date import date_task_id_to_prompt
from prompts.sorting import sorting_task_id_to_prompt
from prompts.boolsimplify import bool_simplify_taskid_to_prompt


task_id_to_prompt = dict()
task_id_to_prompt.update(gsm_task_id_to_prompt)
task_id_to_prompt.update(sports_task_id_to_prompt)
task_id_to_prompt.update(date_task_id_to_prompt)
task_id_to_prompt.update(sorting_task_id_to_prompt)
task_id_to_prompt.update(bool_simplify_taskid_to_prompt)


if __name__ == '__main__':
    import sys
    from utils import format_prompt, PromptConfig

    task_id = sys.argv[1]
    is_cot = sys.argv[2] == 'cot'
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    prompt_str = format_prompt(
        prompt_examples=task_id_to_prompt[task_id],
        prompt_config=PromptConfig(),
        num_examples=0,
        seed=seed,
        is_cot_prompt=is_cot,
    )
    
    print(prompt_str)