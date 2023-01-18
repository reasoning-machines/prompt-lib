from cmath import log
import requests
from pprint import pprint
import json
import sys
import logging
from huggingface_hub import InferenceApi
import time
import os
hf_token = os.getenv('HF_API_TOKEN')
logging.basicConfig(level=logging.INFO)

# adapted from https://github.com/Sentdex/BLOOM_Examples/blob/main/BLOOM_api_example.ipynb

class BloomWrapper:
    @staticmethod
    def call_bloom_api(
        prompt: str, 
        max_length: int = 248, 
        top_k: float = 0, 
        num_beams: int = 0,
        no_repeat_ngram_size: int = 0,
        top_p: float = 0.9,
        seed: int = 42, 
        temperature: float = 0.7,
        greedy_decoding: bool = False,
        return_full_text: bool = False
    ) -> str:
        
        top_k = None if top_k == 0 else top_k
        do_sample = False if num_beams > 0 else not greedy_decoding
        num_beams = None if (greedy_decoding or num_beams == 0) else num_beams
        no_repeat_ngram_size = None if num_beams is None else no_repeat_ngram_size
        top_p = None if num_beams else top_p
        early_stopping = None if num_beams is None else num_beams > 0

        params = {
            "max_new_tokens": max_length,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
            "do_sample": do_sample,
            "seed": seed,
            "early_stopping":early_stopping,
            "no_repeat_ngram_size":no_repeat_ngram_size,
            "num_beams":num_beams,
            "return_full_text":return_full_text
        }
        
        s = time.time()
        inference = InferenceApi("bigscience/bloom",token=hf_token)
        response = inference(prompt, params=params)
        return response
    


if __name__ == "__main__":
    response = BloomWrapper.call_bloom_api(
        prompt="The thing that makes large language models interesting is",
        max_length=248, 
        num_beams=0,
        greedy_decoding=True
    )
    
    print(response)
