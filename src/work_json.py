import json
from data import config

class WorkJson():
    '''Класс для работы с json-файлами'''

    def save_json(self, vacancy_data: list, path):
        self.path = path
        '''Принимает список ваканций и сохраняет в Json-файл'''
        with open(self.path, "a", encoding="UTF-8") as file:
            file.write(json.dumps(vacancy_data, ensure_ascii=False))

    def get_vacancies(self, path):
        self.path = path
        '''Загружает данные из Json - файла, возвращает список словарей с вакансиями в формате Python'''
        with open(self.path, "r", encoding="UTF-8") as file_vacancy:
            return json.load(file_vacancy)


# sup = [{'Яндекс': 1740, 'МегаФон': 3127, 'Билайн': 4934, 'Вконтакте': 15478,'Тинькофф':78638,
#         'Сбер Банк': 3529,'Альфа-Банк': 80,'Почта России': 4352,'Ozon': 2180,'Wildberries ': 87021}]
#
# ex = WorkJson()
# ex.save_json(sup, config.PATH_COMPANY)

