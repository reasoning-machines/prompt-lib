from collections import Counter
import os
from typing import Dict, Any, List, Optional, Union
import openai
import random
import time
import json
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")

"""_summary_
{
    "id": "cmpl-75KEH8y6hIClWMYjn3ou2UzpSnLfb",
    "object": "text_completion",
    "created": 1681503757,
    "model": "text-davinci-003",
    "choices": [
        {
            "text": "\n\nThis is indeed a test",
            "index": 0,
            "logprobs": {
                "tokens": [
                    "\n",
                    "\n",
                    "This",
                    " is",
                    " indeed",
                    " a",
                    " test"
                ],
                "token_logprobs": [
                    -0.05565891,
                    -0.016669365,
                    -0.53892577,
                    -0.04674201,
                    -0.028350571,
                    -0.00021824928,
                    -0.00011225586
                ],
                "top_logprobs": [
                    {
                        "\n": -0.05565891
                    },
                    {
                        "\n": -0.016669365
                    },
                    {
                        "This": -0.53892577
                    },
                    {
                        " is": -0.04674201
                    },
                    {
                        " indeed": -0.028350571
                    },
                    {
                        " a": -0.00021824928
                    },
                    {
                        " test": -0.00011225586
                    }
                ],
                "text_offset": [
                    18,
                    19,
                    20,
                    24,
                    27,
                    34,
                    36
                ]
            },
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 7,
        "total_tokens": 12
    }
}
"""
def get_completion(prompt, model='text-davinci-003', max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop="\n\n",
        temperature=1,
        top_p=1,
        logprobs=1,
    )

    return response.choices[0].logprobs['tokens'], response.choices[0].logprobs['token_logprobs']

def calculate_log_probabilities(tokens, token_logprobs, span_size=3):
    span_to_logprob = []
    i = 0
    while i < len(tokens):
        
        j = 0
        span_ = []
        take_next_tok_in_span = True

        while take_next_tok_in_span:
            span_.append(tokens[i + j])
            j += 1
            take_next_tok_in_span = (i + j) < len(tokens) and (len(span_) < span_size or tokens[i + j][0] != " ")
        
        span_size = len(span_)
        log_probs = token_logprobs[i:i+span_size]
        span_to_logprob.append(("".join(tokens[i:i+span_size]), sum(log_probs)))
        i += j
        

    return span_to_logprob



def categorize_log_probs(log_probs):
    def _get_label(log_prob):
        if log_prob < thresholds[0]:
            return "very low"
        elif log_prob < thresholds[1]:
            return "low"
        elif log_prob < thresholds[2]:
            return "medium"
        elif log_prob < thresholds[3]:
            return "high"
        else:
            return "very high"
        
    log_prob_values = [p[1] for p in log_probs]
    percentiles = [20, 40, 60, 80]

    thresholds = np.percentile(log_prob_values, percentiles)

    res = [f"{span} ({_get_label(log_prob)}) " for (span, log_prob) in log_probs]
    return res



prompt = """Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: Olivia (very high)  started with $23. (very high)  She bought 5 bagels (high)  for $3 each, (medium)  so she spent $15. (very low)  23 - 15 = 8. (very low)  The answer is $8. (low)


Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A: Michael started with (medium) 58 golf balls. (very high) He lost 23 golf (very low) balls on Tuesday and (high) 2 more on Wednesday. (high) That is 25 in total. (very low) So he has 58 - 25 (low) = 33 golf balls. The (low) answer is 33. (very high)


Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A: There were 9 (high) computers in the (very high) server room at (very low) the start. (high) 5 computers were (low) added per day: (very low) 5 x 4 = (very low) 20. So the (low) total number of computers (medium) in the server room (medium) is 9 + 20 (medium) = 29. The (very high) answer is 29. (very high)


Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
A: Shawn had (high) five toys. (low) He got two (very low) toys from his (very low) mom and two (very high) toys from his (medium) dad. So (low) now he has (very low) 5 + 2 (medium) + 2 = (very high) 9 toys. (high) The answer is (very high) 9. (medium)


Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
A: Jason had 20 (high) lollipops. (very high) After giving some to Denny, (low) he had 12 left. 20 - (very low) 12 is 8. The answer is (medium) 8 lollipops. (very high)


Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had (high) 32 chocolates (high) and her sister had (very high) 42. If they (very low) ate 35, then (low) they have 32 + (low) 42 - 35 = (very high) 39 pieces left. (very low) The answer is 39. (medium)


Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There were initially (very low) 3 cars in (high) the parking lot. (very high) After 2 more cars (medium) arrived, the total (low) number is 3 + (very low) 2 = 5. (very high) The answer is 5. (medium)


Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
A: Originally, there (very low) were 15 trees. (very high) After the grove (low) workers planted trees, (very low) there were 21 trees. (medium) So they planted 21 - (medium) 15 = 6 trees. (very high) The answer is 6. (high)


"""


tokens, logprobs = get_completion(prompt, max_tokens=50)


logprobs = calculate_log_probabilities(tokens, logprobs)

span_to_logprob = categorize_log_probs(logprobs)

print("".join(span_to_logprob))