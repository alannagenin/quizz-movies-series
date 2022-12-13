from abc import ABC, abstractmethod


class AbstractRequest(ABC):
    @abstractmethod
    def get_movie_info(self):
        pass

    @abstractmethod
    def get_tv_series_info(self):
        pass

    @abstractmethod
    def get_people_info(self):
        pass
