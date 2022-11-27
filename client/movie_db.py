from dotenv import load_dotenv
import os
from requests import get
from utils.singleton import Singleton
load_dotenv()

class MovieDB(metaclass=Singleton):
    def __init__(self) -> None:
        self.DATABASE_URL = os.environ.get('DATABASE_URL')
        self.API_KEY = os.environ.get('API_KEY')

    def get_movie_info(self, movie_id: int = 999000):
        req = get(
                    str(self.DATABASE_URL) + "movie/" + str(movie_id) + "?api_key=" + str(self.API_KEY)
                )
        raw_request = req.json()
        return raw_request
