"""
Reads files that follow a certain glob from a directory.
Then, runs mcnemar's test and kohen's kappa on each file compared with the `pivot` file.
"""
import pandas as pd
from glob import glob

from statsmodels.stats.contingency_tables import mcnemar
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix


type_to_order = {
    "verbose": 0,
    "direct": 0,
    "stream": 1,   
    "ood": 2,
    "simple_fractions": 2,
    "abs": 3,
    "greek": 3,
    "abstract_person": 3,
    "pat_wrong": 4,
    "wrong_math_right_ans": 4,
    "pat_none": 5,
    "no_equation": 5,
    "no_eqn": 5,
    "pat_only": 6,
    "ccot": 7,
    "short_thought": 7,
    "text_rand": 8,
    "random_thought": 8,
    "text_yoda_thought": 9,
    "yodathought": 9,
    "text_intra_shuf": 10,
    "shuffled_intra": 10,
    "text_inter_shuf": 11,
    "shuffled_inter": 11,
    "text_diff_entities": 12,
    "different_entities": 12,
    "different_player": 13,
    "different_player_different_activity": 14,
}

def run(files_glob, pivot_file):
    pivot_df = pd.read_json(pivot_file, lines=True, orient="records")
    pivot_df = extract_actual_question(pivot_df)
    res = []
    assert len(files_glob) > 0, "No files found"
    for file in glob(files_glob):
        try:
            print(file)
            df = pd.read_json(file, lines=True, orient="records")
            df = extract_actual_question(df)
            # assert len(df) == len(pivot_df)
            res.append(compare(pivot_df, df, file))
        except Exception as e:
            print(e)
            continue
    data = pd.DataFrame(res)

    
    # assign order, based on presence of a key in the `type_to_order` dict in the column `type`
    data["order"] = data.apply(lambda row: type_to_order.get(row["type"], 10000), axis=1)
    for key in type_to_order:
        data.loc[data["type"].str.contains(key), "order"] = type_to_order[key]
    
    
    data = data.sort_values("order")
    print("--p-values-- list")
    for index, row in data.iterrows():
        if row['pvalue'] < 0.00001:
            print("$<$0.00001")
        else:
            print(row["pvalue"])
    print("\n\n")
    print("--kappa--")
    for index, row in data.iterrows():
        print(row["kappa"])

    print(data)


def extract_actual_question(df):
    if "question" not in df.columns:
        df["question"] = df["input"].apply(lambda x: x["question"])
    df["actual_question"] = df.apply(lambda row: row["question"].split("Q:")[-1].strip(), axis=1)
    return df

def compare(pivot_df, df, file):
    if "answer" not in df.columns:
        df["answer"] = df["target"]
    if "answer" not in pivot_df.columns:
        pivot_df["answer"] = pivot_df["target"]
    df = df.merge(pivot_df, on=["actual_question", "answer"], suffixes=("", "_pivot"))
    
    # mcnemar's test
    table = confusion_matrix(df["is_correct"].tolist(), df["is_correct_pivot"].tolist(), normalize=None)
    pvalue = mcnemar(table, exact=True).pvalue

    acc = df["is_correct"].mean() * 100

    # kohen's kappa

    kappa = cohen_kappa_score(df["is_correct"], df["is_correct_pivot"])

    file_basename = file.split("/")[-1]
    
    # print(f"{file_basename}, {acc:.2f}, {pvalue:.2f}, {kappa:.2f}")
    return {"type": file_basename, "acc": round(acc, 2), "pvalue": round(pvalue, 4), "kappa": round(kappa, 2)}

    
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 stats_test.py <files_glob> <pivot_file>")
        sys.exit(1)
    run(sys.argv[1], sys.argv[2])
