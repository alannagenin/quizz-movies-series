from abc import ABC, abstractmethod

class AbstractRequest(ABC):

    @abstractmethod
    def get_movie_info(self):
        pass
    