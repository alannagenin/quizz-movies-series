from BusinessObject.Question.abstract_question import AbstractQuestion
from BusinessObject.Question.question_movie_genre import QuestionMovieGenre
from BusinessObject.Question.question_movie_plot import QuestionMoviePlot
from BusinessObject.Question.question_movie_release_date import QuestionMovieReleaseDate
from BusinessObject.Question.question_series_genre import QuestionSeriesGenre
from BusinessObject.Question.question_series_nb_episodes_total import QuestionSeriesNumberEpisodesTotal
from BusinessObject.Question.question_series_nb_seasons import QuestionSeriesNumberSeasons
from BusinessObject.Question.question_series_plot import QuestionSeriesPlot
from utils.singleton import Singleton


class QuestionFactory(metaclass=Singleton):
    @staticmethod
    def instantiate_movie_question(
            type_question, movie_title, original_movie_title,
            budget, genres_name, release_date, spoken_languages, plot
            ) -> AbstractQuestion:
        question = None
        if type_question == "movie genre":
            question = QuestionMovieGenre(
                movie_title=movie_title,
                original_movie_title=original_movie_title,
                budget=budget,
                genres_name=genres_name,
                release_date=release_date,
                spoken_languages=spoken_languages,
                plot=plot
            )
        elif type_question == "movie plot":
            question = QuestionMoviePlot(
                movie_title=movie_title,
                original_movie_title=original_movie_title,
                budget=budget,
                genres_name=genres_name,
                release_date=release_date,
                spoken_languages=spoken_languages,
                plot=plot
            )
        elif type_question == "movie release date":
            question = QuestionMovieReleaseDate(
                movie_title=movie_title,
                original_movie_title=original_movie_title,
                budget=budget,
                genres_name=genres_name,
                release_date=release_date,
                spoken_languages=spoken_languages,
                plot=plot
            )
        return question

    @staticmethod
    def instantiate_series_question(
                type_question, series_title, original_series_title,
                first_air_date, last_air_date, nb_episodes_per_season,
                nb_episodes_tot, nb_seasons, tv_host, genres_name,
                spoken_languages, plot) -> AbstractQuestion:
        question = None
        if type_question == "series genre":
            question = QuestionSeriesGenre(
                series_title=series_title,
                original_series_title=original_series_title,
                first_air_date=first_air_date,
                last_air_date=last_air_date,
                nb_episodes_per_season=nb_episodes_per_season,
                nb_episodes_tot=nb_episodes_tot,
                nb_seasons=nb_seasons,
                tv_host=tv_host,
                genres_name=genres_name,
                spoken_languages=spoken_languages,
                plot=plot
            )
        elif type_question == "series number episodes total":
            question = QuestionSeriesNumberEpisodesTotal(
                series_title=series_title,
                original_series_title=original_series_title,
                first_air_date=first_air_date,
                last_air_date=last_air_date,
                nb_episodes_per_season=nb_episodes_per_season,
                nb_episodes_tot=nb_episodes_tot,
                nb_seasons=nb_seasons,
                tv_host=tv_host,
                genres_name=genres_name,
                spoken_languages=spoken_languages,
                plot=plot
            )
        elif type_question == "series number seasons":
            question = QuestionSeriesNumberSeasons(
                series_title=series_title,
                original_series_title=original_series_title,
                first_air_date=first_air_date,
                last_air_date=last_air_date,
                nb_episodes_per_season=nb_episodes_per_season,
                nb_episodes_tot=nb_episodes_tot,
                nb_seasons=nb_seasons,
                tv_host=tv_host,
                genres_name=genres_name,
                spoken_languages=spoken_languages,
                plot=plot
            )
        elif type_question == "series plot":
            question = QuestionSeriesPlot(
                series_title=series_title,
                original_series_title=original_series_title,
                first_air_date=first_air_date,
                last_air_date=last_air_date,
                nb_episodes_per_season=nb_episodes_per_season,
                nb_episodes_tot=nb_episodes_tot,
                nb_seasons=nb_seasons,
                tv_host=tv_host,
                genres_name=genres_name,
                spoken_languages=spoken_languages,
                plot=plot
            )
        return question
