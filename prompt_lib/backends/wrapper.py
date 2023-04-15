from abc import ABC, abstractmethod
from typing import Dict, Any
class BaseAPIWrapper(ABC):
    @staticmethod
    @abstractmethod
    def call(
        prompt: str,
        max_tokens: int,
        engine: str,
        stop_token: str,
        temperature: float,
        num_completions: int,
        **kwargs,
    ) -> dict:
        pass


    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        raise NotImplementedError()

    @staticmethod
    def get_majority_answer(response) -> Dict[str, Any]:
        raise NotImplementedError()

    @staticmethod
    def get_all_responses(response) -> Dict[str, Any]:
        raise NotImplementedError()