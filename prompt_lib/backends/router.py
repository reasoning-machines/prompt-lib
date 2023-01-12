# routes a query to the correct backend
import os

from prompt_lib.backends.openai_api import OpenaiAPIWrapper
from prompt_lib.backends.shadowfire_api import ShadowFireWrapper
from prompt_lib.backends.alpa_api import AlpaWrapper

backend_map = {
    "openai": OpenaiAPIWrapper,
    "shadowfire": ShadowFireWrapper,
    "alpa": AlpaWrapper,
}


def few_shot_query(prompt: str, engine: str, backend_name: str, **kwargs):
    return backend_map[backend_name].call(prompt=prompt, engine=engine, **kwargs)


def test():
    prompt = """Question: Who wrote Katie Queen Of Tennessee?
Answer: The Apache Relay
###
Question: Who wrote Never Going Back Again?"""
    backend_to_engine = {
        "openai": "text-curie-001",
        "shadowfire": os.getenv("SHADOWFIRE_MODEL_NAME"),
    }
    for backend_name in ["openai", "shadowfire"]:

        print(backend_name)
        output = few_shot_query(
            backend_name=backend_name,
            prompt=prompt,
            engine=backend_to_engine[backend_name],
            max_tokens=100,
            stop_token="###",
            temperature=0.7,
        )
        print(backend_map[backend_name].get_first_response(output))


if __name__ == "__main__":
    test()
