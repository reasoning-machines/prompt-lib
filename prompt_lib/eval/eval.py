# evaluates the generated output
from glob import glob
import re
from importlib import reload
import pandas as pd
from tqdm import tqdm
from rouge_score import rouge_scorer

import os
from prompt_lib.eval.eval_utils import timeout

from rouge_score import rouge_scorer

def get_rouge_l(data: pd.DataFrame,
                answer_field: str = "answer",
                generated_field: str = "generated_answer",
                return_df: bool = False) -> float:

    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

    def _get_score(row):
        if row[generated_field] is None:
            return 0.0
        generated_answer = row[generated_field].split("Q:")[0].strip()
        generated_answer = re.sub(r"(\d)([a-zA-Z\.])", r"\1 \2", generated_answer)

        scores = scorer.score(str(row[answer_field]).lower(), generated_answer.lower())
        return scores['rougeL'].fmeasure

    data["rouge_l"] = data.apply(_get_score, axis=1)
    rouge_l_avg = data["rouge_l"].mean()

    print(f"Average Rouge-L: {rouge_l_avg:.2f}")
    if return_df:
        return rouge_l_avg, data
    return rouge_l_avg


def get_exact_match_acc(
    data: pd.DataFrame,
    answer_field: str = "answer",
    generated_field: str = "generated_answer",
    return_df: bool = False,
) -> float:
    """Evaluate the generated output. The evaluation is simple: if the target answer is in the generated answer, then it is correct.
    Args:
        data (pd.DataFrame): a dataframe with the columns "generated_answer" and "answer"
    Returns:
        float: the accuracy
    """


    def _is_correct(row):
        if row[generated_field] is None:
            return 0
        generated_answer = row[generated_field].split("Q:")[0].strip()
        # add space between numbers and words. Eg. $16 -> $ 16, 20cm -> 20 cm
        generated_answer = re.sub(r"(\d)([a-zA-Z\.])", r"\1 \2", generated_answer)

        return int(str(row[answer_field]).lower() in generated_answer.lower())
    try:
        data["is_correct"] = data.apply(_is_correct, axis=1)
        acc = data["is_correct"].mean() * 100

        print(f"Accuracy: {acc:.2f}")
        if return_df:
            return acc, data
    except:
        acc = 0
        print(f"Accuracy: {acc:.2f}")
        if return_df:
            return acc, data
    return acc


def run(
    test_file_path: str, answer_field: str = "answer", generated_field: str = "generated_answer"
) -> float:
    data = pd.read_json(test_file_path, lines=True, orient="records")
    return get_exact_match_acc(data, answer_field, generated_field)


def get_acc_from_python_thoughts(
    data: pd.DataFrame,
    answer_field: str = "answer",
    generated_field: str = "generated_answer",
    tol: float = 1e-3,
    return_df: bool = False,
    timeout_seconds: int = 5
):
    """Evaluation function for code-based thoughts. The evaluation is done by running the generated code and comparing the output with the target answer. Assumes that the generated code is a python file. The answer is the field that contains ground truth answer.

    Args:
        data (pd.DataFrame): a dataframe with the columns "generated_answer" and "answer"
        answer_field (str, optional): ground truth answer field. Defaults to "answer".
        generated_field (str, optional): generated answer field. Defaults to "generated_answer".
        tol (float, optional): tolerance for comparing float values. Defaults to 1e-3.
        return_df (bool, optional): if True, return the dataframe with the evaluation results. Defaults to False.
    Returns:
        the accuracy and/or the dataframe with the evaluation results
    """
    def _check_corr(result: float, correct_solution: float):
        if result.strip() == correct_solution.strip():
            return 1
        try:
            result = float(result)
            correct_solution = float(correct_solution)
            return abs(result - correct_solution) < tol
        except:
            return 0
    

    num_corr = 0
    data["is_correct"] = 0
    for i, row in tqdm(data.iterrows(), total=len(data), desc="Evaluating generated python thoughts"):
        soln = row[generated_field]
        
        try:
            # soln can have multiple functions. We only want to run the first function
            imports = ""
            if "nltk" in soln:
                imports += "import nltk\n"
            if "numpy" in soln:
                imports += "import numpy as np\n"
            if "pandas" in soln:
                imports += "import pandas as pd\n"
            
            if "datetime" in soln:
                imports += "from datetime import datetime\n" + "from dateutil.relativedelta import relativedelta\n"
                soln = soln.replace("timedelta", "relativedelta")
            if "spacy" in soln:
                imports += "import spacy\n"
                imports += "nlp = spacy.load('en_core_web_sm')\n"
                
            if "def solution():" not in soln:
                # indent each line and prepend "def solution():"
                soln = "\n".join(["    " + line for line in soln.split("\n")])
                soln = "def solution():\n" + soln
            
            if "return" not in soln:
                soln = soln.splitlines()
                soln[-1] = "    return " + soln[-1].lstrip()
                soln = "\n".join(soln)
            soln = "\ndef " + soln.split("def ")[1] + "\n"
            
            soln = imports + soln
            os.system("rm -rf __pycache__")
            os.system("rm -f temp_result.pyc")
            # soln is a python string, write it to a file, and then run it, get the output
            with open("temp_result.py", "w") as f:
                f.write(soln)

            import temp_result
            reload(temp_result)
            correct_solution = str(row[answer_field])
            exec(soln)
            with timeout(timeout_seconds):
                result = str(temp_result.solution())
            is_corr = _check_corr(result, correct_solution)
            num_corr += int(is_corr)
            data.loc[i, "is_correct"] = is_corr
            data.loc[i, "execution_result"] = result
            print(f"Correct: {is_corr}, Result: {result}, Correct Solution: {correct_solution}")
        except Exception as e:
            data.loc[i, "is_correct"] = 0
            continue
        # compare float values
        
    data["is_correct"] = data["is_correct"].fillna(0)

    os.system("rm -rf __pycache__")
    os.system("rm -f temp_result.pyc")
    os.system("rm -f temp_result.py")

    acc = data["is_correct"].mean() * 100
    print(f"Accuracy: {acc:.2f}")
    if return_df:
        return acc, data
    else:
        return acc
    

# TODO: make the following function more general
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="data/quco/quco_test.jsonl")
    parser.add_argument("--type", type=str, default="code")
    parser.add_argument("--answer_field", type=str, default="answer")
    parser.add_argument("--generated_field", type=str, default="generated_answer")
    
    args = parser.parse_args()
    
    if args.type == "code":
        func = get_acc_from_python_thoughts
    else:
        func = get_exact_match_acc
    if "*" in args.path:
        avg_acc = 0
        for path in glob(args.path):
            print(f"Evaluating {path}")
            data = pd.read_json(path, lines=True, orient="records")
            avg_acc += func(data)
        print(f"Average accuracy = {avg_acc / len(glob(args.path)):.2%}")
    else:
        data = pd.read_json(args.path, lines=True, orient="records")
        func(data)
