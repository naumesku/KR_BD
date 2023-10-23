import json
from data import config
import API_classes

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



# sup = [{'company_name': 'Яндекс', 'company_id': 1740},
#        {'company_name': 'МегаФон', 'company_id':3127},
#        {'company_name': 'Билайн', 'company_id':4934},
#        {'company_name': 'Вконтакте', 'company_id':15478},
#        {'company_name': 'Тинькофф', 'company_id':78638},
#        {'company_name': 'Сбер Банк', 'company_id':3529},
#        {'company_name': 'Альфа-Банк', 'company_id':80},
#        {'company_name': 'Почта России', 'company_id':4352},
#        {'company_name': 'Ozon', 'company_id':2180},
#        {'company_name': 'Wildberries', 'company_id': 87021}]
# #

# ex = WorkJson()
# ex.save_json(sup, config.PATH_COMPANY)
# for i in sup:
#     print(i['company_id'])
#     data_hh = API_classes.HH_API(i['company_id'])
#     vacancy_hh = data_hh.preparation_api_json()
#     ex.save_json(vacancy_hh, config.PATH_VACANCIES)
