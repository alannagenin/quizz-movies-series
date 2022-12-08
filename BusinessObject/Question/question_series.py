from abc import ABC, abstractmethod
from BusinessObject.Question.abstract_question import AbstractQuestion

class QuestionSeries(AbstractQuestion, ABC):
    def __init__(self, series_title, original_series_title, first_air_date, last_air_date, nb_episodes_per_season, nb_episodes_tot, nb_seasons, tv_host, genres_name, spoken_languages, plot):
        '''
        Create a new TV series question.

        Parameters
        ----------
        self.series_title : string
        self.original_series_title : string
        self.first_air_date : int
        self.last_air_date : int
        self.nb_episodes_per_season : list
        self.nb_episodes_tot : int
        self.nb_seasons : int
        self.tv_host : string
        self.genres_name : list
        self.spoken_languages : string
        self.plot : string
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
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass

