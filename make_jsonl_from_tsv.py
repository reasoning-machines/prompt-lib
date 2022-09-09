import sys
import pandas as pd


def to_json():
    if len(sys.argv) != 4:
        print("Usage: python3 make_jsonl_from_tsv.py <question_file> <answer_file> <output_file>")
        return

    questions = pd.read_csv(sys.argv[1], sep="\t", header=None, names=["question"])

    # only take the last question
    questions["input"] = questions["question"].apply(
        lambda x: x.split("Q:")[-1].strip().replace("A:", "").strip()
    )

    # remove all the escape characters
    questions["input"] = questions["input"].apply(lambda x: x.replace("\\", "")[:-1])

    answers = pd.read_csv(sys.argv[2], sep="\t", header=None, names=["target"])
    assert len(questions) == len(answers)
    combined = pd.concat([questions, answers], axis=1)[['input', 'target']]
    combined.to_json(sys.argv[3], orient="records", lines=True)


def attach_target_to_json():
    if len(sys.argv) != 4:
        print("Usage: python3 make_jsonl_from_tsv.py <json file> <target file> <output file>")
        return

    json_file = pd.read_json(sys.argv[1], lines=True, orient="records")
    target_file = pd.read_csv(sys.argv[2], sep="\t", header=None, names=["answer"])
    assert len(json_file) == len(target_file)
    combined = pd.concat([json_file, target_file], axis=1)
    combined.to_json(sys.argv[3], orient="records", lines=True)


if __name__ == "__main__":
    to_json()
