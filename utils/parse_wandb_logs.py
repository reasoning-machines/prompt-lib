"""
Sweeps over all the runs, downlaods the outputs, and saves them to a file.
"""
import wandb
import pandas as pd
from tqdm import tqdm

def run(project_name: str = "amn/alpa", outdir: str = "wandb/outputs"):
    api = wandb.Api()
    runs = api.runs(project_name)
    for run in tqdm(runs):
        if not ("codex" in run.name or "davinci" in run.name) or run.state != "finished":
            continue
        id = run.id
        art = api.artifact(f"{project_name}/run-{id}-outputs:latest")
        tab = art.get("outputs")
        df = to_pandas_df(tab)
        df.to_json(f"{outdir}/{run.name}.jsonl", orient="records", lines=True)


def to_pandas_df(tab):
    columns = tab.columns
    data = {col: tab.get_column(col) for col in columns}
    return pd.DataFrame(data)

if __name__ == "__main__":
    run()