from dotenv import load_dotenv
import os
from requests import get
from abstract_request import AbstractRequest
load_dotenv()

class MovieDB(AbstractRequest):
    def __init__(self) -> None:
        self.DATABASE_URL = os.environ.get('DATABASE_URL')
        self.API_KEY = os.environ.get('API_KEY')

    def get_movie_info(self, movie_id: int = 1):
        '''
        Request to get movie info based on its id.
        '''
        req = get(
                    str(self.DATABASE_URL) + "movie/" + str(movie_id) + "?api_key=" + str(self.API_KEY)
                )   
        if req.status_code == 200:
            raw_request = req.json()
            return raw_request
    
    def get_tv_series_info(self, tv_id: int = 1):
        '''
        Request to tv series movie info based on its id.
        '''
        req = get(
                    str(self.DATABASE_URL) + "tv/" + str(tv_id) + "?api_key=" + str(self.API_KEY)
                )   
        if req.status_code == 200:
            raw_request = req.json()
            return raw_request
    
    def get_people_info(self, tv_id: int = 1):
        '''
        Request to get people info based on its id.
        '''
        req = get(
                    str(self.DATABASE_URL) + "person/" + str(tv_id) + "?api_key=" + str(self.API_KEY)
                )   
        if req.status_code == 200:
            raw_request = req.json()
            return raw_request
    

