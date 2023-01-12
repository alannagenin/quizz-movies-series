from abc import ABC, abstractmethod
from app.business_object.Question.abstract_question import AbstractQuestion


class QuestionMovie(AbstractQuestion, ABC):
    def __init__(
        self, movie_id, movie_title, original_movie_title, budget,
        genres_name, release_date, spoken_languages, main_actors, plot
    ):
        '''
        Create a new movie question.

        Parameters
        ----------
        self.movie_id : int
            ID of the movie
        self.movie_title : string
            Title of the movie
        self.original_movie_title : string
            Title of the movie in its original language
        self.budget : integer
            Budget of the movie
        self.genres_name : string
            Genres of the movie
        self.release_date : string
            Date of release of the movie (yyyy format)
        self.spoken_languages : string
            Languages spoken in the movie
        self.plot : string
            Synopsis of the movie in few lines
        self.type_question : string
            Type of the question
    '''
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.original_movie_title = original_movie_title
        self.budget = budget
        self.genres_name = genres_name
        self.release_date = release_date
        self.spoken_languages = spoken_languages
        self.main_actors = main_actors
        self.plot = plot
        self.type_question = "movie"

    @abstractmethod
    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        pass

    @abstractmethod
    def get_correct_answer(self):
        '''
            Returns the correct answer of the corresponding question.
        '''
        pass
