from collections import Counter
import os
from typing import Dict, Any
import openai
import random
import time

openai.api_key = os.getenv("OPENAI_API_KEY")


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


class OpenaiAPIWrapper:
    @staticmethod
    @retry_with_exponential_backoff
    def call(
        prompt: str, max_tokens: int, engine: str, stop_token: str, temperature: float, best_of: int = 1
    ) -> dict:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[stop_token],
            # logprobs=3,
            best_of=best_of,
            n=best_of,
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
