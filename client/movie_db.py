from datetime import datetime
from dotenv import load_dotenv
import os
from random import choice
import requests
from abstract_request import AbstractRequest
from BusinessObject.Question.question_factory import QuestionFactory
load_dotenv()


class MovieDB(AbstractRequest):
    def __init__(self) -> None:
        self.__DATABASE_URL = os.environ.get('DATABASE_URL')
        self.__API_KEY = os.environ.get('API_KEY')

    def get_movie_info(self, movie_id: int):
        """
        Request to get movie info based on its id.

        Parameters
        ----------
        movie_id : int
            id of the movie to request

        Returns
        -------
        dict
            returns a question containing the following information :
                - movie title
                - original movie title (in the language of the movie)
                - budget
                - genres
                - spoken languages in the movie
                - plot of the movie
        """
        payload = {
            "api_key": str(self.__API_KEY)
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "movie/" + str(movie_id),
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            question_factory = QuestionFactory()
            question = question_factory.instantiate_movie_question(
                movie_title=raw_request['title'],
                original_movie_title=raw_request['original_title'],
                budget=raw_request['budget'],
                genres_name=[raw_request['genres'][item]['name'] for item in range(len(raw_request['genres']))],
                release_date=datetime.strptime(
                    raw_request['release_date'],
                    '%Y-%m-%d'
                ).year,
                spoken_languages=[raw_request['spoken_languages'][item]['english_name'] for item in range(len(raw_request['spoken_languages']))],
                plot=raw_request['overview'],
                type_question=choice(['movie genre', 'movie plot', 'movie release date'])
            )
            return question

    def get_tv_series_info(self, tv_id: int):
        """
        Request to tv series movie info based on its id.

        Parameters
        ----------
        tv_id : int
            id of the TV series to request

        Returns
        -------
        dict
            returns a question containing the following information :
                - series title
                - original series title (in the language of the TV series)
                - first air date
                - last air date
                - number of episodes per season
                - total number of episodes
                - number of seasons
                - TV host
                - genres
                - spoken languages
                - plot
        """
        payload = {
            "api_key": str(self.__API_KEY)
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "tv/" + str(tv_id),
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            question_factory = QuestionFactory()
            question = question_factory.instantiate_series_question(
                series_title=raw_request['name'],
                original_series_title=raw_request['original_name'],
                first_air_date=raw_request['first_air_date'],
                last_air_date=raw_request['last_air_date'],
                nb_episodes_per_season=[raw_request['seasons'][item]['episode_count'] for item
                                        in range(len(raw_request['seasons']))],
                nb_episodes_tot=sum(
                    [raw_request['seasons'][item]['episode_count'] for item in range(len(raw_request['seasons']))]
                ),
                nb_seasons=len(raw_request['seasons']),
                tv_host=[raw_request['networks'][item]['name'] for item in range(len(raw_request['networks']))],
                genres_name=[raw_request['genres'][item]['name'] for item in range(len(raw_request['genres']))],
                spoken_languages=[raw_request['spoken_languages'][item]['english_name'] for item in range(len(raw_request['spoken_languages']))],
                plot=raw_request['overview'],
                type_question=choice(['series genre', 'series number episodes total', 'series number seasons',
                                      'series plot'])
            )
            return question

    def get_people_info(self, people_id: int):
        """
        Request to get people info based on its id.

        Parameters
        ----------
        people_id : int
            id of the TV series to request

        Returns
        -------
        dict
            returns a dictionary containing the following information :
                - name
                - main role
                - place of birth
                - birthdate
                - date of death
                - is the person dead ?
        """
        payload = {
            "api_key": str(self.__API_KEY)
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "person/" + str(people_id),
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            result = {
                'name': raw_request['name'],
                'main_role': raw_request['known_for_department'],
                'place_birth': raw_request['place_of_birth'],
                'date_birth': raw_request['birthday'],
                'date_death': raw_request['deathday'],
                'is_dead': False if raw_request['deathday'] is None else True
                }
            return result

    def get_people_credits(self, people_id: int):
        """
        Request to get people info based on its id.
        """
        payload = {
            "api_key": str(self.__API_KEY),
            "language": "en-US"
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "person/" + str(people_id) + "/combined_credits",
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            return raw_request

    def get_list_movie_genres(self):
        """
        Request to get all the movies genres.

        Returns
        -------
        list
            list of all the movie genres
        """
        payload = {
            "api_key": str(self.__API_KEY),
            "language": "en-US"
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "genre/movie/list",
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            return [raw_request['genres'][item]['name'] for item in range(len(raw_request['genres']))]

    def get_list_tv_genres(self):
        """
        Request to get all the TV genres.

        Returns
        -------
        list
            list of all the TV genres
        """
        payload = {
            "api_key": str(self.__API_KEY),
            "language": "en-US"
        }
        req = requests.get(
            str(self.__DATABASE_URL) + "genre/tv/list",
            params=payload
        )
        if req.status_code == 200:
            raw_request = req.json()
            return [raw_request['genres'][item]['name'] for item in range(len(raw_request['genres']))]
