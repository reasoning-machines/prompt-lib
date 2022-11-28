# sanity check

from prompt_lib.backends import openai_api


response = openai_api.OpenaiAPIWrapper.call(prompt="# x = 2; y = 3; # add x and y set it to z\n", engine="code-davinci-002", max_tokens=50, stop_token="\n\n", temperature=0.5,
                                            best_of=15)
print(response)

print(openai_api.OpenaiAPIWrapper.get_majority_answer(response))