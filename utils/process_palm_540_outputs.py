import pathlib
import pandas as pd
import re

from eval import get_exact_match_acc


def run(basepath: str):
    all_files = list(pathlib.Path(basepath).rglob("sports_*.jsonl"))
    results = []
    for filepath in all_files:
        print(filepath)
        df = pd.read_json(filepath, lines=True, orient="records")
        # acc, df_processed = get_exact_match_acc(df, answer_field="target", generated_field="prediction", return_df=True)
        acc, df_processed = get_exact_match_acc(df, return_df=True)
        
        print(f"{filepath.name} {acc}")
        filename = re.sub(r"-\d+.jsonl", "", filepath.name)
        seed = filename.split("_")[-1]
        filename = filename.replace(f"_{seed}", "")
        results.append({"task": filename, "acc": acc, "seed": seed})
        pathlib.Path(f"{basepath}/processed_df/").mkdir(parents=True, exist_ok=True)
        df_processed.to_json(f"{basepath}/processed_df/{filename}_{seed}", orient="records", lines=True)

    df = pd.DataFrame(results)
    df.to_csv("outputs/results.csv", index=False)
    df.groupby("task")["acc"].apply(lambda x: ",".join([str(round(xi, 2)) for xi in x])).reset_index().to_csv(f"{basepath}/results_mean.csv", sep="\t", index=None)
if __name__ == "__main__":
    run("wandb/outputs/")