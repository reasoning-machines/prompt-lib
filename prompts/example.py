from dataclasses import dataclass


# prompts are either a list of Example objects or just a string

@dataclass
class Example:
    question: str
    answer: str
    thought: str


class PromptStr:
    """Class to store the prompt string.
    Wraps a prompt string to allow type checking.
    """

    def __init__(self, prompt_str: str):
        self.prompt_str = prompt_str
