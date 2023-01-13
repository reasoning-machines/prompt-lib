# routes a query to the correct backend
import os

from prompt_lib.backends.openai_api import OpenaiAPIWrapper
from prompt_lib.backends.shadowfire_api import ShadowFireWrapper
from prompt_lib.backends.alpa_api import AlpaWrapper


# TODO: all of this should be in a config file
backend_map = {
    "openai": OpenaiAPIWrapper,
    "shadowfire": ShadowFireWrapper,
    "alpa": AlpaWrapper,
}

openai_engines = [
    "text-curie-001",
    "text-davinci-001",
    "text-davinci-002",
    "text-davinci-003",
    "code-davinci-002",
    "code-cushman-001",
]
shadowfire_engines = ["shadowfire"]

engine_to_backend = {e: "openai" for e in openai_engines}
engine_to_backend.update({e: "shadowfire" for e in shadowfire_engines})


def few_shot_query(
    prompt: str, engine: str, return_entire_response: bool = False, **kwargs
):  
    backend_name = engine_to_backend[engine]
    
    output = backend_map[backend_name].call(prompt=prompt, engine=engine, **kwargs)
    top_response = backend_map[backend_name].get_first_response(output)
    if return_entire_response:
        return output
    else:
        return top_response


def test():
    prompt = """Question: Who wrote Katie Queen Of Tennessee?
Answer: The Apache Relay
###
Question: Who wrote Never Going Back Again?"""

    for engine_name in ["text-curie-001", "shadowfire"]:

        print(engine_name)
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
