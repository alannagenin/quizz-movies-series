from abc import ABC, abstractmethod

class AbstractQuestion(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass