from app.business_object.Question.abstract_question import AbstractQuestion
from app.business_object.Question.question_movie_genre import QuestionMovieGenre
from app.business_object.Question.question_movie_plot import QuestionMoviePlot
from app.business_object.Question.question_movie_release_date import QuestionMovieReleaseDate
from app.business_object.Question.question_series_genre import QuestionSeriesGenre
from app.business_object.Question.question_series_nb_episodes_total import QuestionSeriesNumberEpisodesTotal
from app.business_object.Question.question_series_nb_seasons import QuestionSeriesNumberSeasons
from app.business_object.Question.question_series_plot import QuestionSeriesPlot
from app.business_object.Question.question_people_birth_date import QuestionPeopleBirthDate
from app.business_object.Question.question_people_birth_place import QuestionPeopleBirthPlace
from app.business_object.Question.question_people_death_date import QuestionPeopleDeathDate
from app.business_object.Question.question_people_is_dead import QuestionPeopleIsDead
from app.business_object.Question.question_people_role import QuestionPeopleRole
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

    @staticmethod
    def instantiate_people_question(
            name: object, main_role: object, place_birth: object, date_birth: object, date_death: object, is_dead: object,
            type_question: object) -> AbstractQuestion:
        if type_question == "people birth date":
            question = QuestionPeopleBirthDate(
                name=name,
                main_role=main_role,
                place_birth=place_birth,
                date_birth=date_birth,
                date_death=date_death,
                is_dead=is_dead
            )
        elif type_question == "people birth place":
            question = QuestionPeopleBirthPlace(
                name=name,
                main_role=main_role,
                place_birth=place_birth,
                date_birth=date_birth,
                date_death=date_death,
                is_dead=is_dead
            )
        elif type_question == "people death date":
            question = QuestionPeopleDeathDate(
                name=name,
                main_role=main_role,
                place_birth=place_birth,
                date_birth=date_birth,
                date_death=date_death,
                is_dead=is_dead
            )
        elif type_question == "people is dead":
            question = QuestionPeopleIsDead(
                name=name,
                main_role=main_role,
                place_birth=place_birth,
                date_birth=date_birth,
                date_death=date_death,
                is_dead=is_dead
            )
        elif type_question == "people role":
            question = QuestionPeopleRole(
                name=name,
                main_role=main_role,
                place_birth=place_birth,
                date_birth=date_birth,
                date_death=date_death,
                is_dead=is_dead
            )
        return question
