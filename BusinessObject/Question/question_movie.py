from abc import ABC, abstractmethod
from abstract_question import AbstractQuestion

class QuestionMovie(AbstractQuestion, ABC):
    def __init__(self, movie_title, original_movie_title, budget, genres_name, release_date, spoken_languages, plot):
        self.movie_title = movie_title
        self.original_movie_title = original_movie_title
        self.budget = budget
        self.genres_name =  genres_name
        self.release_date = release_date
        self.spoken_languages = spoken_languages
        self.plot = plot
    
    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass