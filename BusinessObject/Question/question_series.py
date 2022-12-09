from abc import ABC, abstractmethod
from BusinessObject.Question.abstract_question import AbstractQuestion

class QuestionSeries(AbstractQuestion, ABC):
    def __init__(self, series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot):
        '''
        Create a new TV series question.

        Parameters
        ----------
        self.series_title : string
            Title of the series
        self.original_series_title : string
            Title of the movie in its original language
        self.first_air_date : int
            Date of the first air date (yyyy format)
        self.last_air_date : int
            Date of the last air date (yyyy format)
        self.nb_episodes_per_season : list
            Number of episodes per season 
        self.nb_episodes_tot : int
            Total number of episodes
        self.nb_seasons : int
            Number of seasons
        self.tv_host : string
            Name of the TV host
        self.genres_name : list
            Genres of the TV series
        self.spoken_languages : string
            Languages spoken in the series
        self.plot : string
            Synopsis of the series in few lines
        self.type : string
            Type of the question
        '''
        self.series_title = series_title
        self.original_series_title = original_series_title
        self.first_air_date = first_air_date
        self.last_air_date = last_air_date
        self.nb_episodes_per_season = nb_episodes_per_season
        self.nb_episodes_tot = nb_episodes_tot
        self.nb_seasons = nb_seasons
        self.tv_host = tv_host
        self.genres_name = genres_name
        self.spoken_languages = spoken_languages
        self.plot = plot
        self.type = "series"
    
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

