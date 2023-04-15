import argparse
import pandas as pd
from tqdm import tqdm
import yaml

from prompt_lib.backends import openai_api


def parse_arguments():
    parser = argparse.ArgumentParser(description="Provide fixed data points for the script.")
    parser.add_argument("--config_path", type=str, required=True, help="Configuration file path")
    return parser.parse_args()


def read_config(config_path: str) -> dict:
    with open(config_path, "r") as config_file:
        config_data = yaml.safe_load(config_file)
    return config_data


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    return content


def run_inference(main_message: list, config_data: dict):
    response = openai_api.OpenaiAPIWrapper.call(
        main_message,
        max_tokens=config_data["max_tokens"],
        engine=config_data["engine"],
        stop_token=config_data["stop_token"],
        temperature=config_data["temperature"],
        num_completions=config_data["num_completions"],
    )
    response = openai_api.OpenaiAPIWrapper.get_first_response(response)
    return response


if __name__ == "__main__":
    """
    Expects a yaml config file with the following fields:
        system_message_path: path/to/system_message.txt
        user_message_path: path/to/input_str.txt
        system_response_path: path/to/output_str.txt
        prompts_path: path/to/prompts.txt
        results_path: path/to/results.txt
        max_tokens: 1000
        engine: gpt-3.5-turbo
        stop_token: ---
        temperature: 0.0
        num_completions: 1
    """
    args = parse_arguments()
    config_data = read_config(args.config_path)

    system_message = read_file(config_data["system_message_path"])
    user_message = read_file(config_data["user_message_path"])
    system_response = read_file(config_data["system_response_path"])

    # Update this part to include your custom logic for generating prompts
    prompts_file = pd.read_json(config_data["prompts_path"], orient="records", lines=True)
    prompts = prompts_file["prompt"].tolist()

    responses = []
    for prompt in tqdm(prompts):
        main_message = [
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            },
            {
                "role": "system",
                "content": system_response,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        response = run_inference(main_message, config_data)
        print(response)
        responses.append({"prompt": prompt, "response": response})
    pd.DataFrame(responses).to_json(config_data["results_path"], orient="records", lines=True)
