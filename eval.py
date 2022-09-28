# evaluates the generated output
import re
import pandas as pd


def get_exact_match_acc(
    data: pd.DataFrame, answer_field: str = "answer", generated_field: str = "generated_answer", return_df: bool = False
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


def run(test_file_path: str, answer_field: str = "answer", generated_field: str = "generated_answer") -> float:
    data = pd.read_json(test_file_path, lines=True, orient="records")
    return get_exact_match_acc(data, answer_field, generated_field)


if __name__ == "__main__":
    import sys

    run(sys.argv[1], answer_field="target", generated_field="prediction")
