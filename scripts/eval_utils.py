# evaluates the generated output
import re
from importlib import reload
import pandas as pd
from tqdm import tqdm
from contextlib import contextmanager
import signal
from glob import glob
import os


@contextmanager
def timeout(duration):
    def timeout_handler(signum, frame):
        raise TimeoutError(f"block timedout after {duration} seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(duration)
    try:
        yield
    finally:
        signal.alarm(0)

def read_json(path):
    import json
    rows = []
    with open(path, "r") as f:
        for line in f:
            rows.append(json.loads(line))
    
    task_df = pd.DataFrame(rows)
    return task_df

def check_corr(result: float, correct_solution: float, tol: float = 1e-3) -> bool:
    return abs(result - correct_solution) < 1e-3