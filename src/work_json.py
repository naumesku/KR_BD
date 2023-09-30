import json
from data import config
from abc import ABC, abstractmethod
from preparatoin import MixinPreparatoin

class VacanciesSave(ABC):
    '''Абстрактный класс для сохранения и изменения списка вакансий в файлы'''

    @staticmethod
    @abstractmethod
    def add_vacancies(vacancy_data: list) -> list:
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @staticmethod
    @abstractmethod
    def del_vacancies(user_id: int):
        pass


class WorkJson(VacanciesSave, MixinPreparatoin):
    '''Класс для сохранения, получения, изменения списка вакансий в json-файл'''
    def __init__(self ) -> None:
        self.json_file = config.PATH_VACANCIES

    def sav_json(self, vacancy_data:list):
        '''Принимает список ваканций и сохраняет в Json-файл'''
        with open(self.json_file, "w", encoding="UTF-8") as file:
            file.write(json.dumps(vacancy_data, ensure_ascii=False))

    def add_vacancies(self, user_data:dict):
        '''Принимает данные о вакансии и добавлет файл Json'''
        self.user_data = user_data
        all_vakancies = self.get_vacancies()
        all_vakancies.append(self.user_data)
        self.sav_json(all_vakancies)

    def get_vacancies(self):
        '''Загружает данные из Json - файла, возвращает список словарей с вакансиями в формате Python'''
        with open(self.json_file, "r", encoding="UTF-8") as file_vacancy:
            return json.load(file_vacancy)

    def del_vacancies(self, del_id:int):
        '''Пинимает ID вакансии для удаления, удаляет ее и созраняет измененный список в Json-файл'''
        all_vacancis = self.get_vacancies()
        count = 0
        for vacans in all_vacancis:
            if vacans["id"] == del_id:
                count += 1
                all_vacancis.remove(vacans)
        self.sav_json(all_vacancis)
        if count == 0:
            print("Вакансии с таким ID в списке нет.")
        else:
            print(f"Удалено вакансий: {count}.")
