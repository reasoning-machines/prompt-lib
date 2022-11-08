import random
def make_shuffled_prompt(prompt_path: str, seed: int, example_sep: str):
    with open(prompt_path, "r") as f:
        prompt = f.read()
    random.seed(seed)
    prompt_parts = prompt.split(example_sep)
    prompt_parts = [p for p in prompt_parts if p.strip()]
    print(prompt_parts)
    print(f"Found {len(prompt_parts)} examples")
    random.shuffle(prompt_parts)
    
    shuffled_prompt = example_sep.join(prompt_parts).strip() + example_sep # add back the separator at the end
    
    with open(f"{prompt_path}.s{seed}", "w") as f:
        f.write(shuffled_prompt)
    print(f"Shuffled prompt written to {prompt_path}.s{seed}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt_path", type=str, required=True)
    parser.add_argument("--seeds", type=int, nargs="+", required=True)
    parser.add_argument("--example_sep", type=str, default="\n\n\n", help="Separator between examples in the prompt")
    args = parser.parse_args()

    for seed in args.seeds:
        make_shuffled_prompt(args.prompt_path, seed, example_sep=args.example_sep)