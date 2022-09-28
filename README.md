# DECOT

- This repo contains code and data required to reproduce the results in our submission. Note that we experiment with four different models: i) codex, ii) gpt-3, iii) PaLM-62B, and iv) PaLM-540B. Since the PaLM variants are not publicly available, this script allows you to reproduce the results for codex and gpt-3. While gpt-3 is not free, codex is free with a rate limit of 20 requests / min. Our code implements the rate limit and retries for code models. For both these models, a key is required to access the API. The key can be accessed from [this link](https://beta.openai.com/account/api-keys) after making an OpenAI account ([link](https://openai.com/join/)).

- The key needs to be exported as an environment variable. For example, if the key is `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`, then the following command can be used to export the key:


```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- After this, all the jobs can be run using the following command:

```bash
bash scripts/run_jobs.sh
```

- To make the repo self-contained, we have included all the datasets and prompts:

1. Prompts are located in `prompts/` directory.
2. Datasets are located in `data/tasks/` directory.