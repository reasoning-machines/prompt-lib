import os
from typing import Dict, Any
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# code: "code-davinci-001"

class OpenaiAPIWrapper:
    @staticmethod
    def call(prompt: str, max_tokens: int, engine: str, stop_token: str) -> dict:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=0.0,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[stop_token],
            # logprobs=3,
            best_of=1
        )
        return response

    @staticmethod
    def parse_response(response) -> Dict[str, Any]:
        text = response["choices"][0]["text"]
        return text

