# Backend for a self-hosted API
import os
from pprint import pprint
from typing import Any, Dict

import os
import requests


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

    def completions(
        self,
        prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None,
        top_p=0.9,
        engine=None,
        logprobs=None,
    ):
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



    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses."""
        
        print(response)
        text = response["choices"][0]["text"]
        return text

    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        """Returns the majority answer from the list of responses."""
        answers = [choice["text"] for choice in response["choices"]]
        answers = Counter(answers)
        # if there is a tie, return the first answer
        if answers.most_common(1)[0][1] == answers.most_common(2)[1][1]:
            return CompletionAPIWrapper.get_first_response(response)

        return answers.most_common(1)[0][0]

    @staticmethod
    def get_all_responses(response) -> Dict[str, Any]:
        """Returns the list of responses."""
        return [
            {
                "generated_answer": choice["text"],
                "logprobs": choice["logprobs"] if "logprobs" in choice else None,
            }
            for choice in response["choices"]
        ]


class TogetherAPIBackend(OpenSourceAPIBackend):
    def __init__(self, base_url: str = None):
        self.base_url = base_url or "https://api.together.xyz"
        if os.environ.get("SELF_HOSTED_URL"):
            self.base_url = os.environ.get("SELF_HOSTED_URL")
        # Fetching the token from environment variable
        token = os.environ.get("TOGETHER_KEY")
        if not token:
            raise ValueError("TOGETHER_KEY environment variable is not set!")
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url):
        print(f"Setting base_url to {url}")
        self._base_url = url

    def completions(
        self,
        prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=0.9,
        engine="togethercomputer/llama-2-70b",
        logprobs=None,
        n: int = 1,
        stop_token: str = None,
        stop: str = None,
    ):
        url = f"{self.base_url}/inference"
        data = {
            "model": engine,
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "request_type": "language-model-inference",
            "n": n,
            "stop": stop or stop_token,

        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()



    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses."""
        
        print(response)
        text = response["output"]["choices"][0]["text"]
        return text



def get_backend(engine: str):
    """Factory method to get appropriate backend based on engine name."""
    if "togethercomputer" in engine:
        return TogetherAPIBackend()
    else:
        return OpenSourceAPIBackend()

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
        # Dynamically select the backend based on engine
        api = get_backend(engine)
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
    def get_api_wrapper(model_name: str):
        if "togethercomputer" in model_name:
            return TogetherAPIBackend
        else:
            return OpenSourceAPIBackend


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

    @staticmethod
    def get_api_wrapper(model_name: str):
        if "togethercomputer" in model_name:
            return TogetherAPIBackend
        else:
            return OpenSourceAPIBackend


def test():
    
    api = OpenSourceAPIBackend()
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
    assert (
        test_api.base_url == "http://pitt.lti.cs.cmu.edu:5000"
    ), f"api.base_url: {test_api.base_url}"
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

def test_together():

    # Test using the TogetherAPIBackend directly
    together_api = TogetherAPIBackend()

    response = together_api.completions(
        prompt="What is the capital of France?",
        max_tokens=10,
        n=1,
        stop_token="\n",
        temperature=0.7,
        engine="togethercomputer/llama-2-70b",
    )
    pprint(response)

    # Test using the wrapper with the together engine
    wrapper = OpenSourceAPIWrapper()

    response = wrapper.call(
        prompt="What is the capital of France?",
        max_tokens=10,
        engine="togethercomputer/llama-2-70b",
        stop_token="\n",
        temperature=0.7,
    )
    pprint(response)

import argparse

def main():
    parser = argparse.ArgumentParser(description="Run specific tests for the API wrappers.")
    parser.add_argument("--test", choices=["default", "together"], required=True,
                        help="Specify the test to run. Options: 'default' or 'together'.")
    
    args = parser.parse_args()
    
    if args.test == "default":
        test()
    elif args.test == "together":
        test_together()

if __name__ == "__main__":
    main()
