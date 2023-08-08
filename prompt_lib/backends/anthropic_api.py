# Backend for a self-hosted API
import os
from pprint import pprint
from typing import Any, Dict
import anthropic
import requests

from prompt_lib.backends.wrapper import BaseAPIWrapper

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "Your_Default_Value")
client = anthropic.Client(ANTHROPIC_API_KEY)


class AnthropicAPIWrapper(BaseAPIWrapper):
    @staticmethod
    def _call_api(
        prompt: str,
        max_tokens: int,
        engine: str,
        stop_token: str,
        temperature: float,
        num_completions: int = 1,
    ) -> dict:
        prompt = f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}"

        response = client.completion(
            prompt=prompt,
            stop_sequences=[anthropic.HUMAN_PROMPT],
            model=engine,
            max_tokens_to_sample=max_tokens,
            temperature=temperature,
        )

        return response

    @staticmethod
    def call(
        prompt: str,
        max_tokens: int,
        engine: str,
        stop_token: str,
        temperature: float,
        num_completions: int = 1,
    ) -> dict:
        max_completions_in_one_call = 8
        if num_completions > max_completions_in_one_call:
            response_combined = dict()
            num_completions_remaining = num_completions
            for i in range(0, num_completions, max_completions_in_one_call):
                response = AnthropicAPIWrapper._call_api(
                    prompt=prompt,
                    max_tokens=max_tokens,
                    engine=engine,
                    stop_token=stop_token,
                    temperature=temperature,
                    num_completions=min(num_completions_remaining, max_completions_in_one_call),
                )
                print(f"Remaining completions: {num_completions_remaining}")
                num_completions_remaining -= max_completions_in_one_call
                if i == 0:
                    response_combined = response
                else:
                    response_combined["choices"] += response["choices"]

            return response_combined
        response = AnthropicAPIWrapper._call_api(
            prompt=prompt,
            max_tokens=max_tokens,
            engine=engine,
            stop_token=stop_token,
            temperature=temperature,
            num_completions=num_completions,
        )

        return response

    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses."""
        text = response["completion"]
        return text

    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        """Returns the majority answer."""
        # Anthropics doesn't have a majority answer
        raise NotImplementedError

    @staticmethod
    def get_all_responses(response) -> Dict[str, Any]:
        """Returns the list of responses."""
        # Anthropics doesn't have a list of responses
        raise NotImplementedError


def test():
    wrapper = AnthropicAPIWrapper()

    response = wrapper.call(
        prompt="The quick brown fox",
        max_tokens=10,
        engine="claude-2",
        stop_token="\n",
        temperature=0.7,
    )

    pprint(response)

if __name__ == "__main__":
    test()
