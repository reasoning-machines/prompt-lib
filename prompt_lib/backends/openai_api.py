from collections import Counter
import os
from typing import Dict, Any
import openai
import random
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

# check if orgainization is set

if os.getenv("OPENAI_ORG") is not None:
    openai.organization = os.getenv("OPENAI_ORG")

# from https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb
def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
    errors: tuple = (openai.error.RateLimitError,),
):
    """Retry a function with exponential backoff."""

    def wrapper(*args, **kwargs):
        # Initialize variables
        num_retries = 0
        delay = initial_delay

        # Loop until a successful response or max_retries is hit or an exception is raised
        while True:
            try:

                return func(*args, **kwargs)

            # Retry on specified errors
            except errors as e:
                # Increment retries
                num_retries += 1

                # Check if max retries has been reached
                if num_retries > max_retries:
                    raise Exception(f"Maximum number of retries ({max_retries}) exceeded.")

                # Increment the delay
                delay *= exponential_base * (1 + jitter * random.random())

                # Sleep for the delay
                time.sleep(delay)

            # Raise exceptions for any errors not specified
            except Exception as e:
                raise e

    return wrapper


class  OpenaiAPIWrapper:
    @staticmethod
    @retry_with_exponential_backoff
    def call(
        prompt: str,
        max_tokens: int,
        engine: str,
        stop_token: str,
        temperature: float,
        num_completions: int = 1
    ) -> dict:
        """Calls the completion API.

        if the num_completions is > 2, we call the API multiple times. This is to prevent 
        overflow issues that can occur when the number of completions is too large.
        """
        if num_completions > 2:
            response_combined = dict()
            num_completions_remaining = num_completions
            for i in range(0, num_completions, 2):
                # note that we are calling the same function --- this prevents backoff from being reset for the entire function
                response = OpenaiAPIWrapper.call(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    engine=engine,
                    stop_token=stop_token,
                    temperature=temperature,
                    num_completions=min(num_completions_remaining, 2),
                )
                num_completions_remaining -= 2
                print(f"num_completions_remaining: {num_completions_remaining}")
                if i == 0:
                    response_combined = response
                else:
                    response_combined["choices"] += response["choices"]
            return response_combined
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            stop=[stop_token],
            # logprobs=3,
            n=num_completions,
        )
        return response

    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses."""
        text = response["choices"][0]["text"]
        return text

    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        """Returns the majority answer from the list of responses."""
        answers = [choice["text"] for choice in response["choices"]]
        answers = Counter(answers)
        # if there is a tie, return the first answer
        if answers.most_common(1)[0][1] == answers.most_common(2)[1][1]:
            return OpenaiAPIWrapper.get_first_response(response)

        return answers.most_common(1)[0][0]


    @staticmethod
    def get_all_responses(response) -> Dict[str, Any]:
        """Returns the list of responses."""
        return [choice["text"] for choice in response["choices"]]  # type: ignore

def test():
    prompt = "Optimize the following Python code:\n\n# Start of code\n\nimport sys\n\nimport numpy as np\n\nn,m = [int(x) for x in sys.stdin.readline().split()]\n\nr = np.zeros(n)\n\nfor i in range(m):\n\n\ta, b = [int(x) for x in sys.stdin.readline().split()]\n\n\tr[a-1] += 1\n\n\tr[b-1] += 1\n\nfor i in range(n):\n\n\tprint((int(r[i])))\n\n# End of code\nRewrite the above Python code only from \"Start of code\" to \"End of code\", to make it more efficient WITHOUT CHANGING ITS RESULTS. Assume the code has already executed all the imports; do NOT include them in the optimized code.\n\nUse native libraries if that would make it faster than pure Python.\n\nYour output should only consist of valid Python code. Output the resulting Python with brief explanations only included as comments prefaced with #. Include a detailed explanatory comment before the code, starting with the text \"# Proposed optimization:\". Make the code as clear and simple as possible, while also making it as fast and memory-efficient as possible. Use vectorized operations whenever it would substantially increase performance, and quantify the speedup in terms of orders of magnitude. Eliminate as many for loops, while loops, and list or dict comprehensions as possible, replacing them with vectorized equivalents. If the performance is not likely to increase, leave the code unchanged. Fix any errors in the optimized code."
    engine = "code-davinci-002"
    num_completions = 32
    max_tokens = 300
    response = OpenaiAPIWrapper.call(prompt=prompt, max_tokens=max_tokens, engine=engine, stop_token="Optimize the following Python code:\n\n", temperature=0.7, num_completions=num_completions)
    print(response)

if __name__ == "__main__":
    # test the API
    test()