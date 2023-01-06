from abc import ABC, abstractmethod
from app.business_object.Question.abstract_question import AbstractQuestion


class QuestionPeople(AbstractQuestion, ABC):
    def __init__(
            self, name, main_role, place_birth, date_birth, date_death, is_dead
            ):
        """
        Create a new people question.

        Parameters
        ----------
        self.name : string
            Title of the series
        self.main_role : string
            Title of the movie in its original language
        self.place_birth : string
            Place of birth of the person
        self.date_birth : Date
            Date of the birth (yyyy-mm-dd format)
        self.date_death : Date
            If the person is dead then date of death (yyyy-mm-dd format) otherwise None
        self.is_dead : bool
            Is the person death or not?

        """
        self.name = name
        self.main_role = main_role
        self.place_birth = place_birth
        self.date_birth = date_birth
        self.date_death = date_death
        self.is_dead = is_dead
        self.type_question = 'people'

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
