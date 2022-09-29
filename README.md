# Text and Patterns: For Effective Chain of Thought, It Takes Two to Tango

## Reproducing the results in the paper

- This repo contains code and data required to reproduce the results in our submission. Note that we experiment with four different models: i) codex, ii) gpt-3, iii) PaLM-62B, and iv) PaLM-540B. Since the PaLM variants are not publicly available, this script allows you to reproduce the results for codex and gpt-3. While gpt-3 is not free, codex is free with a rate limit of 20 requests / min. Our code implements the rate limit and retries for code models. For both these models, a key is required to access the API. The key can be accessed from [this link](https://beta.openai.com/account/api-keys) after making an OpenAI account ([link](https://openai.com/join/)).

- The key needs to be exported as an environment variable. For example, if the key is `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`, then the following command can be used to export the key:


```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- After this, all the jobs can be run using the following command:
 
```bash
bash scripts/run_jobs.sh
```

## Outputs and prompts

-----------

- The lightweight requirements are listed in `requirements.txt`. 

- To make the repo self-contained, we have included all the datasets and prompts:

1. Prompts are located in `prompts/` directory.
2. Datasets are located in `data/tasks/` directory.


## File listing

----

```
📁 ./
├─📁 utils/
│ ├─📄 stats_test.py
├─📄 query_openai.py
├─📁 prompts/
│ ├─📄 task_id_to_prompt.py
│ ├─📄 gsm.py
│ ├─📄 utils.py
│ ├─📄 __init__.py
│ ├─📄 example.py
│ ├─📄 sports.py
│ ├─📄 date.py
│ └─📄 sorting.py
├─📄 eval.py
└─📄 openai_api.py
```

* Some notable files:

1. `query_openai.py` contains the code to query the API.

2. `prompts/` contains the prompts for each task (`gsms.py`, `sports.py`, `sorting.py`, `date.py`).

3. `eval.py` contains the code to evaluate the outputs.

4. `prompts/utils.py` includes rate-limiting and retry logic.


---

## Outputs

* The outputs are located in `outputs.zip`. 

* Each file is a jsonl, and follows a specific naming format: `{task_id}-{model_name}_s{seed}.jsonl`. For example, `outputs/sports_stream_text-davinci-002_s1.jsonl` contains the outputs for the `sports_stream_text` task for the `text-davinci-002` model with seed 1.

* A sample line in the output is as follows:

```json
{
    "question": "Q: Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'\nA: Jonas Valanciunas is a basketball player. Beating the buzzer is part of basketball. The answer is yes.\n\n\nQ: Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'\nA: Kyle Palmieri is a hockey player. Being called for slashing is part of hockey. The answer is yes.\n\n\nQ: Is the following sentence plausible? 'Jamal Murray was perfect from the line.'\nA: Jamal Murray is a basketball player. Being perfect from the line is part of basketball. The answer is yes.\n\n\nQ: Is the following sentence plausible? 'Draymond Green threw a touchdown.'\nA: Draymond Green is an basketball player. Throwing a touchdown is part of football, not basketball. The answer is no.\n\n\nQ: Is the following sentence plausible? 'Carson Wentz set the pick and roll.'\nA: Carson Wentz is an American football player. Pick and roll is part of basketball, not football. The answer is no.\n\n\nQ: Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'\nA: Joao Moutinho is a soccer player. The NFC championship is part of American football, not soccer. The answer is no.\n\n\nQ: Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'\nA: Malcolm Brogdon is a basketball player. Banking the shot in is part of basketball. The answer is yes.\n\n\nQ: Is the following sentence plausible? 'Sam Darnold passed the puck.'\nA: Sam Darnold is a American football player. Passing the puck is part of hockey, not American football. The answer is no.\n\n\nQ: Yes or no: Is the following sentence plausible? \"Neal Pionk took the snap.\"\nA:",
    "generated_answer": " Neal Pionk is a hockey player. Taking the snap is part of American football, not hockey. The answer is no.",
    "answer": "no",
    "is_correct": 1
}
```

* Here:

1. `question` is the prompt + test question.
2. `generated_answer` is the generated answer.
3. `answer` is the correct answer.
4. `is_correct` is 1 if the generated answer is correct, and 0 otherwise.
