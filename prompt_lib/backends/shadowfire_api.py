import os
from typing import Dict, Any, Tuple
import random
import time
import nemollm

# NOTE: You need to set the following environment variables:
API_HOST = os.getenv("SHADOWFIRE_API_URL") 
API_KEY = os.getenv("SHADOWFIRE_API_KEY")
API_MODEL_NAME = os.getenv("SHADOWFIRE_MODEL_NAME") 

conn = None


# from https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb
def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
    errors: tuple = (TimeoutError,nemollm.exceptions.ApiException,),
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


class ShadowFireWrapper:
    
    trimmed_prompt_cache: Dict[Tuple[str, int, str], str] = {}    
    @staticmethod
    def trim_prompt(prompt: str, max_tokens: int, stop_token: str) -> str:
        # assumes that prompt consists of blocks of text separated by stop_token
        # retains as many blocks as possible while keeping the total length of the prompt
        # also maintains a cache of trimmed prompts to avoid re-computing the same thing

        if (prompt, max_tokens, stop_token) in ShadowFireWrapper.trimmed_prompt_cache:
            return ShadowFireWrapper.trimmed_prompt_cache[(prompt, max_tokens, stop_token)]
        prompt_examples = prompt.split(stop_token)
        max_allowed_prompt_length = ShadowFireWrapper.SHADOWFIRE_MAX_PROMPT_CHARS - max_tokens - 10
        while len(stop_token.join(prompt_examples)) > max_allowed_prompt_length:
            prompt_examples.pop(0)
        trimmed_prompt = stop_token.join(prompt_examples)
        ShadowFireWrapper.trimmed_prompt_cache[(prompt, max_tokens, stop_token)] = trimmed_prompt
        return trimmed_prompt
    
    SHADOWFIRE_MAX_PROMPT_CHARS: int = 4096
    @staticmethod
    @retry_with_exponential_backoff
    def call(
        prompt: str, max_tokens: int, stop_token: str, temperature: float, engine: str = None, num_completions: int = 1
    ) -> dict:
        global conn
        if conn is None:
            conn = nemollm.Connection(host=API_HOST, access_token=API_KEY)
        
        if len(prompt) + max_tokens > ShadowFireWrapper.SHADOWFIRE_MAX_PROMPT_CHARS:
            prompt = ShadowFireWrapper.trim_prompt(prompt, max_tokens, stop_token)
        response = conn.generate_completion(
            model_id=API_MODEL_NAME,  # default to the model specified in the environment variable
            prompt=prompt,
            tokens_to_generate=max_tokens,
            logprobs=False,
            temperature=temperature,
            top_p=1.,
            top_k=64,
            stop=[stop_token],
            random_seed=0,
            repetition_penalty=1.,
            beam_search_diversity_rate=0.,
            beam_width=1,
            length_penalty=1.,
        )
        return response

    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses."""
        text = response["text"]
        return text
    
    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        """Returns the majority answer from the list of responses."""
        raise NotImplementedError("Not implemented for ShadowFire API")



def test():
    prompt = """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now? Answer: Let's think step by step."""
    output = ShadowFireWrapper.call(prompt=prompt, max_tokens=100, stop_token="###", temperature=0.5, num_completions=1)
    print(ShadowFireWrapper.get_first_response(output))

if __name__ == "__main__":
    test()
    
    