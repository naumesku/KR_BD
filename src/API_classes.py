from abc import ABC, abstractmethod
from pprint import pprint
import requests, json
from data.config import HH_VACANCIES_URL, HH_HEADERS, COUNT_HH, PATH_LOG, currency_change

class HH_API():
    '''Класс для поиска вакансий на сайте HH.ru по id_работодателя '''
    def __init__(self, employer_id: str) -> None:
        self.employer_id = employer_id
        self.__url = HH_VACANCIES_URL
        self.__headers = HH_HEADERS
        self.params = {"employer_id": self.employer_id, "per_page": COUNT_HH,'page': 0, "archived": False}

    def get_response(self):
        '''Принимает параметры и выдает список найденных вакансий в формате Json'''
        self.response = requests.get(url=self.__url, headers=self.__headers, params=self.params)
        return self.response.json()

    def preparation_api_json (self):
        '''Получает данные в формате Json и возвращает общий список словарей с только необходимыми параметрами вакансий'''
        all_vacancy = []
        vacancy_hh = self.get_response()

        for vacancy in vacancy_hh["items"]:
            try:
                all_vacancy.append(dict(vacancy_id=int(vacancy['id']),
                    employer_id=self.employer_id, vacancy_name=vacancy.get('name'),
                    salary_from=(self.currency_exchange(vacancy['salary']['from'],
                               vacancy['salary']['currency'])) if vacancy.get('salary')
                                        else None, url=vacancy['alternate_url']))
            except TypeError:
                with open(PATH_LOG, "a", encoding="UTF-8") as file:
                    file.write(json.dumps(vacancy, ensure_ascii=False))
                continue

        return all_vacancy

    def currency_exchange(self, salary, currenty):
        '''Получает данные о сумме и валюте, и возвращает сумму конвертируемую в рубли при необходимости'''
        if salary != None and salary != 0:
            if currenty == "RUR" or "rub":
                data_change = salary
            else:
                data_change = salary * currency_change[currenty.upper()]
        else:
            data_change = "не указана"
        return data_change
