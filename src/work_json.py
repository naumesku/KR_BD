import json

class WorkJson():
    '''Класс для работы с json-файлами'''

    def save_json(self, vacancy_data: list, path):
        '''Принимает список ваканций и сохраняет в Json-файл'''
        self.path = path
        with open(self.path, "a", encoding="UTF-8") as file:
            file.write(json.dumps(vacancy_data, ensure_ascii=False))

    def get_vacancies(self, path):
        '''Загружает данные из Json - файла, возвращает список словарей с вакансиями в формате Python'''
        self.path = path
        with open(self.path, "r", encoding="UTF-8") as file_vacancy:
            return json.load(file_vacancy)

    def clean_json(self, path):
        '''Удаляет данные из Json - файла'''
        self.path = path
        with open(self.path, "w", encoding="UTF-8") as file:
            file.write('')
