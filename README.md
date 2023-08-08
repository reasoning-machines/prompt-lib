# Prompt-lib

- A library for hassle-free few-shot prompting.

TLDR: This library makes it easy to write prompts for few-shot prompting tasks. It includes rate-limiting and retry logic, and makes it easy to write prompts for different tasks.

- To get started, run:
```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
python prompt_lib/run_inference.py --task_id boolsimplify_stream --num_prompt_examples -1 --name boolsimplify_stream_code-davinci-002_s1 --model_name code-davinci-002 --max_tokens 600 --seed 1 --num_questions_per_thread 500 --temperature 0.0 --num_inference_examples 3 --cot_task --is_debug

```

- The outputs are stored in `data/logs/boolsimplify_stream/code-davinci-002/temp_0.0/seed_1/k_all/`


## News 📢
[Aug 2023] Added support for Together.ai API.

[June 2023] Added support for claude series of  models from Anthropic.

[Mar 2023] `prompt-lib` now works with ChatGPT/GPT-4. The addition is backward compatible, so you can simply use`gpt-3.5-turbo` or `gpt-4` as the engine name. However, you may want to checkout how we convert the prompt to messages [here](https://github.com/reasoning-machines/prompt-lib/blob/e55c23080505daa1d3e73d26fadb5cd29bf07d25/prompt_lib/backends/openai_api.py#L169).

## Colabs

You can run these colabs directly in the browser. Supporting bulk-inference is the main goal of `prompt-lib`, but these notebooks should give you a good idea of some of the functionality.


* [Querying OpenAI](https://github.com/reasoning-machines/prompt-lib/blob/main/notebooks/QueryOpenAI.ipynb)

* [Custom task](https://github.com/reasoning-machines/prompt-lib/blob/main/notebooks/PromptLibCustomTask.ipynb)

If your goal is not to do bulk inference (typically required for research papers/benchmarking), we recommend checking out https://langchain.readthedocs.io/.

## Running on a custom task

`prompt-lib` comes with a large number of tasks. To register a new task, please follow these instructions: 


### Step 1: Defining a custom task

- To begin we need a prompt. A prompt is a list of examples, where each example is an instantiation of the following:

```py
@dataclass
class Example:
    question: str
    answer: str
    thought: str
```

- The `question` is the input to the model, the `answer` is the expected output, and the `thought` is an intermediate reasoning step. The `thought` is optional, and can be left as an empty string if not needed (for direct prompting for example).

- Let us define a prompt for the task of boolean expression simplification. The following is a list of examples for this task:

```py
[
    Example(
        question="!a & a & (a ^ c & d | !b)",
        answer="false",
        thought="false & expr is false",
    ),
    Example(
        question="a & b | a & c",
        answer="a & (b | c)",
        thought="a & (b | c) is the same as a & b | a & c",
    ),
    Example(
        question="a & b | a & b",
        answer="a & b",
        thought="expr | expr is the same as expr",
    ),
    Example(
        question="(a | !a) | ((b & !c | c & !b) & (a | !a) | (b & !c | c & !b))",
        answer="true",
        thought="true | expr is true",
    ),
]
```

- The prompt can be added to any python file in scope, but for the sake of this example, we will add it to `prompts/boolsimplify/boolsimplify.py`. Typically, you will try multiple variations of a prompt for a task.
 To keep things manageable, we add a dictionary at the end of `prompts/boolsimplify/boolsimplify.py` that gives a task_id to each prompt:

```py
 bool_simple_taskid_to_prompt = {
    "boolsimplify_stream": bool_simple_examples
}
```

- Note the id we give to our task: `boolsimplify_stream`. By convention, task_ids have two parts: `{dataset}_{prompt_type}`. Here, the `dataset` is `boolsimplify` and the `prompt_type` is `stream`.  This is important: we expect `dataset.jsonl` to be present in `data/tasks/`


**Text-file based prompt:**
- For many use cases, you may not want to define a prompt in a text file. This is easily done by specifying a path in `bool_simple_taskid_to_prompt`:

```py
 bool_simple_taskid_to_prompt = {
    "boolsimplify_txt": "prompts/boolsimplify/boolsimplify.txt"
}
```

- All the steps below remain the same. When running a job, you need to specify boolsimplify_txt as the task_id.

### Step 2: Registering the task

- The next step is to register the task. The file `task_id_to_prompt` maintains a global dictionary that maps task_ids to prompts. We can add our task to this dictionary by adding the following line to `task_id_to_prompt`:

```py
from prompt_lib.prompts.boolsimplify import boolsimplify_taskid_to_prompt

task_id_to_prompt.update(bool_simple_taskid_to_prompt)
```

- The task is now registered, and can be used to run a custom task.


### Step 3: Defining inputs/outputs

- We want to evaluate the model on some test file, and thus we need a file with inputs and expected outputs. The file `data/tasks/boolsimplify.jsonl` contains the inputs and outputs for the `boolsimplify` dataset. The file is a jsonl, and each line is a json object with the following keys:

```py
{
    "input": "a & b | a & c",
    "target": "a & (b | c)",
}
```

- A simple task file with 5 lines has been added to `data/tasks/boolsimplify.jsonl` for this example. You can add more lines to this file to evaluate the model on more examples.


### Step 4: Running the task


- Now that the task is registered, and the inputs/outputs are defined, we can run the task. The following command will run the task:

- Export your openai api key to the environment variable `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```


```bash
bash scripts/run_single_task.sh boolsimplify_stream
```


- The outputs are stored in `data/logs/boolsimplify_stream/`



### Structure of a prompt

- We highly recommend reading [this document](docs/prompt.md) to understand the structure of a prompt better.

### Additional notes

- If you are using text prompts, seeds are not supported. Instead, you can use 'scripts/shuffle_prompt.py' to create a shuffled version of the prompt.

```bash
python prompt-lib/scripts/shuffle_prompt.py --prompt_path quco_prompts/gsm/function_with_comments.txt --seeds 1 2 3 --example_sep $'\n\n\n'
```

(note the $'\n\n\n' to separate examples--this is needed for passing newlines to the script)


### Custom Evaluation

- You can also run custom evaluation scripts. This is highly recommended. If you are running a large number of prompt variations, consider writing the custom evaluation function in `scripts/eval.py`, and then passing it as an argument `--eval_function`. Combined with `wandb`, this can be a powerful way to track the performance of your prompts without having to track the outputs of each prompt variation.


### Multiple outputs

- You can specify `--num_completions` to get multiple outputs. The output file is stored in the same location, with an extra field `generated_answers` that is a list of outputs. The `generated_answer` field is still present, and is the first element of `generated_answers`.

For example:

```sh
python3 prompt_lib/run_inference.py --task_id boolsimplify_stream --num_prompt_examples -1 --name boolsimplify_stream_code-davinci-002_s1 --model_name code-davinci-002 --max_tokens 600 --seed 1 --num_questions_per_thread 500 --temperature 0.9 --num_inference_examples 3 --cot_task --is_debug --num_completions 3
```

Generates an output file `data/logs/boolsimplify_stream/code-davinci-002/temp_0.9/seed_1/k_all/2023-01-02_10-16-39/outputs.jsonl` (the timestamp will be different). One entry in the file is:

```
{
    "prompt": "Q: a & b | a & c\nA: a & (b | c) is the same as a & b | a & c The answer is a & (b | c)\n\n\nQ: a & b | a & b\nA: expr | expr is the same as expr The answer is a & b\n\n\nQ: !a & a & (a ^ c & d | !b)\nA: false & expr is false The answer is false\n\n\nQ: (a | !a) | ((b & !c | c & !b) & (a | !a) | (b & !c | c & !b))\nA: true | expr is true The answer is true",
    "question": "\nQ: a & b | a & b\nA: ",
    "answer": "a & b",
    "generated_answers": [
        "expr | expr is the same as expr The answer is a & b",
        "expr | expr is the same as expr The answer is a & b",
        "!b & a is the same as a & !b The answer is !b & a"
    ],
    "generated_answer": "expr | expr is the same as expr The answer is a & b",
    "is_correct": 1
}
```


### TODOs:

- [ ] Allow formatting functions to be used for creating a prompt dynamically. Currently, prompts are created either by reading from a file or by using prefixes for question/answer. This excludes use cases like https://github.com/reasoning-machines/CoCoGen

- [ ] Cache previous outputs in a memory during a run.

- [ ] Add example of using `--cached_timestamp`
