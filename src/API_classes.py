from abc import ABC, abstractmethod
import requests
from data.config import HH_VACANCIES_URL, HH_HEADERS, SJ_VACANCIES_URL, SJ_HEADERS, COUNT_SJ, COUNT_HH

class API(ABC):
    """Родительский класс для работы с АПИ"""

    @abstractmethod
    def get_response(self):
        pass

class HH(API):
    '''Класс для поиска вакансиях на сайте HH.ru по названию'''
    def __init__(self, user_search: str) -> None:
        self.__url = HH_VACANCIES_URL
        self.__headers = HH_HEADERS
        self.params = {"text": user_search, "per_page": COUNT_HH,'page': 0, "archived": False}

    def get_response(self):
    # Принимает текст для поиска и выдает список найденных вакансий в формате Json
        self.response = requests.get(url=self.__url, headers=self.__headers, params=self.params) #headers=self.__headers,
        return self.response.json()

class SJ(API):
    '''Класс для поиска вакансиях на сайте SJ.ru'''

    def __init__(self, user_search: str) -> None:
        self.__url = SJ_VACANCIES_URL
        self.__headers = SJ_HEADERS
        self.params = {"count":COUNT_SJ, "keyword":user_search, "archive":False}

    def get_response(self):
    # Принимает текст для поиска и выдает список найденных вакансий в формате Json
        self.response = requests.get(url=self.__url, headers=self.__headers, params=self.params)
        return self.response.json()
