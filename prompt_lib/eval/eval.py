# evaluates the generated output
import re
from importlib import reload
import pandas as pd
from tqdm import tqdm

import os
from prompt_lib.eval.eval_utils import timeout


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

    data["is_correct"] = data.apply(_is_correct, axis=1)
    acc = data["is_correct"].mean() * 100

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
    for i, row in tqdm(data.iterrows(), total=len(data), desc="Evaluating generated python thoughts"):
        soln = row[generated_field]
        
        # soln can have multiple functions. We only want to run the first function
        imports = ""
        if "nltk" in soln:
            imports += "import nltk\n"
        if "numpy" in soln:
            imports += "import numpy as np\n"
        if "pandas" in soln:
            imports += "import pandas as pd\n"
        
        if "spacy" in soln:
            imports += "import spacy\n"
            imports += "nlp = spacy.load('en_core_web_sm')\n"
            
        soln = imports + "\ndef " + soln.split("def ")[1] + "\n"
        
        os.system("rm -rf __pycache__")
        os.system("rm -f temp_result.pyc")
        # soln is a python string, write it to a file, and then run it, get the output
        with open("temp_result.py", "w") as f:
            f.write(soln)

        try:
            import temp_result
            reload(temp_result)
            correct_solution = row[answer_field]
            exec(soln)
            with timeout(timeout_seconds):
                result = temp_result.solution()
            is_corr = _check_corr(result, correct_solution)
            num_corr += int(is_corr)
            data.loc[i, "is_correct"] = is_corr
            data.loc[i, "execution_result"] = result
        except:
            data.loc[i, "is_correct"] = 0
            continue
        # compare float values

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
# if __name__ == "__main__":
#     import argparse

#     parser = argparse.ArgumentParser()
#     parser.add_argument("--path", type=str, default="data/quco/quco_test.jsonl")
#     parser.add_argument("--type", type=str, default="code")
#     args = parser.parse_args()
#     if args.type == "code":
#         func = evaluate_code_prompt
#     else:
#         func = evaluate_text_prompt
#     if "*" in args.path:
#         avg_acc = 0
#         for path in glob(args.path):
#             print(f"Evaluating {path}")
#             avg_acc += func(path)
#         print(f"Average accuracy = {avg_acc / len(glob(args.path)):.2%}")
#     else:
#         func(args.path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide the path to the test file")
        sys.exit(1)

    
    answer_field = sys.argv[2] if len(sys.argv) > 2 else "answer"
    
    generated_field = sys.argv[3] if len(sys.argv) > 3 else "generated_answer"

    run(sys.argv[1], answer_field=answer_field, generated_field=generated_field)
