from dataclasses import dataclass


@dataclass
class Example:
    question: str
    answer: str
    thought: str
