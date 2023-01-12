# calls the alpa autocompletion API at https://opt.alpa.ai/completions
from cmath import log
import requests
from pprint import pprint
import json
import sys
import logging

logging.basicConfig(level=logging.INFO)


class AlpaWrapper:
    @staticmethod
    def call_alpa_endpoint(
        text: str, max_tokens: int = 60, temperature: float = 0.0, top_p: float = 0.5, timeout: int = 180
    ) -> str:
        url = "https://opt.alpa.ai/completions"
        headers = {"Content-Type": "application/json"}
        payload = {
            "prompt": text,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=timeout).json()
            if "choices" in response:
                return response["choices"][0]["text"]
            else:
                logging.info(f"Error: {response}")
                logging.info(response)
                return None
        except requests.Timeout:
            logging.info(f"Timeout: {text}")
            return None
            


if __name__ == "__main__":
    call_alpa_endpoint(sys.argv[1])
