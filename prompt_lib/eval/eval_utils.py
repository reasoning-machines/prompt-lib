# evaluates the generated output
import pandas as pd
from contextlib import contextmanager
import signal
import json


@contextmanager
def timeout(duration):
    """
    Timeout context manager.
    Taken from: https://stackoverflow.com/questions/492519/timeout-on-a-function-call
    """

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


def read_jsonl(path):

    rows = []
    with open(path, "r") as f:
        for line in f:
            rows.append(json.loads(line))

    task_df = pd.DataFrame(rows)
    return task_df
