from abc import ABC, abstractmethod


class AbstractQuestion(ABC):
    def __init__(self) -> None:
        """
        Create a question.
        """
        super().__init__()

    @abstractmethod
    def display_question(self):
        """
            Returns the question as it should be displayed in the quizz.
        """
        pass

    @abstractmethod
    def get_correct_answer(self):
        """
        Returns the correct answer of the corresponding question.
        """
        pass
