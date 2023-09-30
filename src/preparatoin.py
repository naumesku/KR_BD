import json
from data import config
from API_classes import HH,SJ
from datetime import datetime

class MixinPreparatoin:
    '''Класс-миксин для валидации. Подготавливает общеий список вакансий (или ваканчию от пользователя) с необходимыми данными'''

    def preparation_data_api(self, search_text):
        '''Получает данные в формате Json от 2 API-классов, и возвращает общий список словарей с только необходимыми параметрами'''
        self.search_text = search_text
        all_vacancy = []
        data_hh = HH(self.search_text)
        vacancy_hh = data_hh.get_response()
        data_SJ = SJ(self.search_text)
        vacancy_SJ = data_SJ.get_response()
        for vacancy in vacancy_hh["items"]:
            try:
                all_vacancy.append(dict(id=int(vacancy['id']), name=vacancy.get('name'), date_publishedt=vacancy['published_at'][:10],
                        salary_from = (self.currency_exchange(vacancy['salary']['from'], vacancy['salary']['currency'])) if vacancy.get('salary') else "не указана",
                        salary_to = (self.currency_exchange(vacancy['salary']['to'], vacancy['salary']['currency'])) if vacancy.get('salary') else "не указана",
                        responsibility=vacancy['snippet']['responsibility'], town=vacancy['area']['name'],
                        url=vacancy['alternate_url']))
            except TypeError:
                with open(config.PATH_LOG, "a", encoding="UTF-8") as file:
                    file.write(json.dumps(vacancy, ensure_ascii=False))
                continue
        for vacancy in vacancy_SJ["objects"]:
            try:
                all_vacancy.append(dict(id=vacancy['id'], name=vacancy.get('profession'), date_publishedt=(datetime.utcfromtimestamp(vacancy['date_published']).strftime('%Y-%m-%d %H:%M:%S'))[:10],
                            salary_from=(self.currency_exchange(vacancy['payment_from'], vacancy['currency']))if vacancy.get('payment_from') else "не указана",
                            salary_to=(self.currency_exchange(vacancy['payment_to'], vacancy['currency']))if vacancy.get('payment_from') else "не указана",
                            responsibility=(vacancy['work'] if vacancy.get('work') else "не указаны"), town=vacancy['town']['title'],
                            url=vacancy['link']))
            except TypeError:
                #Записываем вакансии с "битыми" данными в лог-файл, если таковые будут
                with open(config.PATH_LOG, "a", encoding="UTF-8") as file:
                    file.write(json.dumps(vacancy, ensure_ascii=False))
                continue
        return all_vacancy

    def currency_exchange (self, salary, currenty):
        '''Получает данные о сумме и валюте, и возвращает сумму конвертируемую в рубли при необходимости'''
        if salary != None and salary != 0:
            if currenty == "RUR" or "rub":
                data_change = salary
            else:
                data_change = salary * config.currency_change[currenty.upper()]
        else:
            data_change = "не указана"

        return data_change

    def preparation_data_user(self):
        '''Получает данные от пользователя, и возвращает ваакансию с необходимыми параметрами'''
        while True:
            try:
                id_user = int(input("Введите id вакансии (целое число): "))
                name_user = input("Введите название вакансии: ")
                year = int(input("Введите год даты публикации вакансии в формате: 'ГГГГ': "))
                month = int(input("Введите месяц даты публикации вакансии в формате: 'ММ': "))
                day = int(input("Введите день даты публикации вакансии в формате: 'ДД': "))
                if not 0 < year <= 2023 or not 0 < month < 13 or not 0 < day < 32:
                    print ("Не верный ввод. Попробуйте снова")
                    continue
                else:
                    date_publishedt_user = f"{year}-{month}-{day}"
                salary_from_user = int(input("Введите min заработок вакансии (целое число): "))
                salary_to_user = int(input("Введите max заработок вакансии (целое число): "))
                responsibility_user = input("Введите описание вакансии: ")
                town_user = input("Введите Город: ")
                url_user = input("Введите ссылку на вакансию: ")

                new_vacancy = dict(id=id_user,
                                   name=name_user,
                                   date_publishedt=date_publishedt_user,
                                   salary_from=salary_from_user,
                                   salary_to=salary_to_user,
                                   responsibility=responsibility_user,
                                   town=town_user,
                                   url=url_user)
                return new_vacancy
            except ValueError:
                #Срабатывает при проявлении ошибки ввода данных, цикл запускается заново
                print("Не верный ввод. Попробуйте ещё раз")
                continue
