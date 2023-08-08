# routes a query to the correct backend
import os

from prompt_lib.backends.openai_api import OpenaiAPIWrapper
from prompt_lib.backends.shadowfire_api import ShadowFireWrapper
from prompt_lib.backends.alpa_api import AlpaWrapper
from prompt_lib.backends.self_hosted import OpenSourceAPIWrapper

# TODO: all of this should be in a config file
backend_map = {
    "openai": OpenaiAPIWrapper,
    "shadowfire": ShadowFireWrapper,
    "alpa": AlpaWrapper,
    "self_hosted": OpenSourceAPIWrapper,
}

openai_engines = [
    "text-curie-001",
    "text-davinci-001",
    "text-davinci-002",
    "text-davinci-003",
    "code-davinci-002",
    "code-cushman-001",
    "gpt-3.5-turbo",
    "gpt-4",
    "vicuna-33b-v1.3",
    "meta-llama/Llama-2-70b-hf"
]
shadowfire_engines = ["shadowfire"]

self_hosted_engines = [
    "self-vulcan-13b"
]

engine_to_backend = {e: "openai" for e in openai_engines}
engine_to_backend.update({e: "shadowfire" for e in shadowfire_engines})
engine_to_backend.update({e: "self_hosted" for e in self_hosted_engines})


def few_shot_query(prompt: str, engine: str, return_entire_response: bool = False, **kwargs):
    backend_name = engine_to_backend[engine]

    output = backend_map[backend_name].call(prompt=prompt, engine=engine, **kwargs)
    top_response = backend_map[backend_name].get_first_response(output)
    if return_entire_response:
        return output
    else:
        return top_response


def get_first_response(output, engine):
    backend_name = engine_to_backend[engine]
    return backend_map[backend_name].get_first_response(output)

def call(prompt: str, engine: str, return_entire_response: bool = False, **kwargs):
    return few_shot_query(
        prompt=prompt, engine=engine, return_entire_response=return_entire_response, **kwargs
    )


def test():
    prompt = """Question: Who wrote Katie Queen Of Tennessee?
Answer: The Apache Relay
###
Question: Who wrote Never Going Back Again?"""

    for engine_name in ["text-curie-001", "shadowfire", "self-vulcan-13b"]:

        print(f"Testing {engine_name}\n")
        output = few_shot_query(
            prompt=prompt,
            engine=engine_name,
            max_tokens=100,
            stop_token="###",
            temperature=0.7,
        )
        print(output)


if __name__ == "__main__":
    test()
