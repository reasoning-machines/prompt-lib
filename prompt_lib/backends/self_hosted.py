# Backend for a self-hosted API
import os
from pprint import pprint
from typing import Any, Dict

import requests

from prompt_lib.backends.wrapper import BaseAPIWrapper


class OpenSourceAPIBackend:
    def __init__(self, base_url: str = None):
        self.base_url = base_url
        if os.environ.get("SELF_HOSTED_URL"):
            self.base_url = os.environ.get("SELF_HOSTED_URL")

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url):
        print(f"Setting base_url to {url}")
        self._base_url = url

    def completions(self, prompt, temperature=0.7, max_tokens=150, n=1, stop=None, top_p=None, engine=None, logprobs=None):
        url = f"{self.base_url}/completion"
        data = {
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "n": n,
            "stop": stop,
            "top_p": top_p,
        }
        response = requests.post(url, json=data)
        return response.json()


api = OpenSourceAPIBackend()


class OpenSourceAPIWrapper(BaseAPIWrapper):

    @staticmethod
    def _call_api(
        prompt: str,
        max_tokens: int,
        engine: str,
        stop_token: str,
        temperature: float,
        num_completions: int = 1,
    ) -> dict:
        response = api.completions(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            stop=[stop_token],
            n=num_completions,
            logprobs=5,
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
                response = OpenSourceAPIWrapper._call_api(
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
        response = OpenSourceAPIWrapper._call_api(
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
        api_wrapper = OpenSourceAPIWrapper.get_api_wrapper(response["model"])
        return api_wrapper.get_first_response(response)

    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        api_wrapper = OpenSourceAPIWrapper.get_api_wrapper(response["model"])
        return api_wrapper.get_majority_answer(response)
    
    
    @staticmethod
    def get_all_responses(response) -> Dict[str, Any]:
        api_wrapper = OpenSourceAPIWrapper.get_api_wrapper(response["model"])
        return api_wrapper.get_all_responses(response)
    

def test():
    
    wrapper = OpenSourceAPIWrapper()
    api.base_url = "http://pitt.lti.cs.cmu.edu:5000"

    response = wrapper.call(
        prompt="The quick brown fox",
        max_tokens=10,
        engine="self-vulcan-13b",
        stop_token="\n",
        temperature=0.7,
    )
    
    pprint(response)

    test_api = OpenSourceAPIBackend()
    test_api.base_url = "http://pitt.lti.cs.cmu.edu:5000"
    assert test_api.base_url == "http://pitt.lti.cs.cmu.edu:5000", f"api.base_url: {test_api.base_url}"
    pprint(
        test_api.completions(
            "The quick brown fox",
            max_tokens=10,
            n=1,
            stop="\n",
            temperature=0.7,
            engine="self-vulcan-13b",
        )
    )

    test_api.base_url = None

    # make sure it fails
    import unittest

    api.base_url = None
    unittest.TestCase().assertRaises(
        Exception,
        wrapper.call,
        prompt="The quick brown fox",
        max_tokens=10,
        engine="self-vulcan-13b",
        stop_token="\n",
        temperature=0.7,
    )

    # environment variable
    os.environ["SELF_HOSTED_URL"] = "http://pitt.lti.cs.cmu.edu:5000"

    test_api = OpenSourceAPIBackend()
    pprint(
        test_api.completions(
            "The quick brown fox",
            max_tokens=10,
            n=1,
            stop="\n",
            temperature=0.7,
            engine="self-vulcan-13b",
        )
    )


if __name__ == "__main__":
    test()
