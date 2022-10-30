from importlib import reload
import pandas as pd
from tqdm import tqdm
from contextlib import contextmanager
import signal


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

def evaluate_quco_stream(path):
    data = read_json(path)
    num_corr = 0
    for i, row in tqdm(data.iterrows()):
        soln = row["generated_answer"]
        # soln is a python string, write it to a file, and then run it, get the output
        with open("temp_result.py", "w") as f:
            f.write(soln)

        try:
            import temp_result

            reload(temp_result)
            correct_solution = row["answer"]
            with timeout(5):
                result = temp_result.solution()
        except:
            continue
        if not (isinstance(result, int) or isinstance(result, float)):
            continue
        # compare float values
        is_corr = abs(result - correct_solution) < 1e-3
        num_corr += int(is_corr)

    print(f"Accuracy = {num_corr / len(data):.2%} ({num_corr}/{len(data)})")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="data/quco/quco_test.jsonl")
    args = parser.parse_args()
    evaluate_quco_stream(args.path)
