no_prompt = []  # zero-shot prompt
num_toks_to_tag = {
    95000: "100k",
    7500: "8k",
    0: "0k",
    50: "50",
    500: "500",
    1000: "1k",
    2000: "2k",
    3500: "3pt5k",
    4000: "4k",
    16000: "16k",
    32000: "32k",
    64000: "64k",
    80000: "80k",
}



datasets = ["govrep", "ssd", "cnli", "qasper", "quality", "qmsum", "narrative", "musique"]


tag_to_model = {
    "100k": "claude-v1-100k",
    "80k": "claude-v1-100k",
    "64k": "claude-v1-100k",
    "32k": "claude-v1-100k",
    "16k": "claude-v1-100k",
}
task_id_to_prompt = dict()

for tag in num_toks_to_tag.values():
    for dataset in datasets:
        task_id_to_prompt[f"{dataset}{tag}_zs"] = no_prompt
