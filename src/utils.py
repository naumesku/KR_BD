import json
import API_classes
from work_json import WorkJson
from work_vacancies import SortVacancies, PerformanceVacancies
from work_database import CREATE_DB
from data.config import PATH_COMPANY, PATH_VACANCIES
from configparser import ConfigParser

def all_vacancies_json(path_companies,path_vacansies ):
    '''Сохраняет вакансии всех компаний из файла "path_companies" в файл json "path_vacansies"'''

    ex = WorkJson()
    ex.clean_json(PATH_VACANCIES)
    # Удаляем данные из json - файла

    with open(path_companies, 'r', encoding='UTF-8') as f:
        data_companies = json.load(f)
        vacancy_hh_all = []
        for i in data_companies:
            data_hh = API_classes.HH_API(i['company_id'])
            vacancy_company = data_hh.preparation_api_json()
            vacancy_hh_all.extend(vacancy_company)
        ex.save_json(vacancy_hh_all, path_vacansies)

def create_database(path_companies, name_table_companies, path_vacansies, name_table_vacansies):
    '''Создает базу данных с таблицами и заполняет их'''
    db = CREATE_DB()
    db.create_database()
    db.filling_table(path_companies, name_table_companies)
    db.filling_table(path_vacansies, name_table_vacansies)






def users_work(data_search):
    '''Функция для работы с пользователем'''
    work_js = WorkJson()
    # Создаем экземпляр класса для работы с Json - файлом
    work_js.sav_json(work_js.preparation_data_api(data_search))
    # Запускаем поиск и сохраняем данные в файл

    while True:
        all_vacancy_list = work_js.get_vacancies()
        # Загружаем актуальный список вакансий из Json - файла
        if len(all_vacancy_list) != 0:
            try:
                choice_action = int(input("""Программа может :
                    0 - вывести список по умолчанию
                    1 - сотировать по заработной плате (сначала "большие"),
                    2 - сотировать по городу,
                    3 - сотировать по дате размещения (сначала "свежие")
                    4 - удалять вакансии по ID
                    5 - добавить вакансию
                    6 - показать вакансии только с сайта SJ.ru
                    7 - показать вакансии только с сайта HH.ru
                    8 - показать топ 20 вакансий 
                    9 - выход из программы 

                    Выберите действие (цифра от 0 до 9) и нажмите "Enter": """))

                if choice_action == 0:
                    answer_vacancy_list = all_vacancy_list

                elif choice_action == 1:
                    sort_data = SortVacancies()
                    actual_vacancy_list = [line for line in all_vacancy_list if isinstance(line['salary_from'], int)]
                    answer_vacancy_list = sort_data.sort_vacancies('salary_from', actual_vacancy_list)

                elif choice_action == 2:
                    sort_data = SortVacancies()
                    answer_vacancy_list = sort_data.sort_vacancies('town', all_vacancy_list, False)

                elif choice_action == 3:
                    sort_data = SortVacancies()
                    answer_vacancy_list = sort_data.sort_vacancies('date_publishedt', all_vacancy_list)

                elif choice_action == 4:
                    user_id = int(input("\nВведите id для удаления: "))
                    work_js.del_vacancies(user_id)
                    answer_vacancy_list = work_js.get_vacancies()

                elif choice_action == 5:
                    work_js.add_vacancies(work_js.preparation_data_user())
                    answer_vacancy_list = work_js.get_vacancies()
                    print("Вакансия добавлена.")

                elif choice_action == 6:
                    answer_vacancy_list = [line for line in all_vacancy_list if "superjob.ru" in line['url']]

                elif choice_action == 7:
                    answer_vacancy_list = [line for line in all_vacancy_list if "hh.ru" in line['url']]

                elif choice_action == 8:
                    sort_data = SortVacancies()
                    actual_vacancy_list = [line for line in all_vacancy_list if isinstance(line['salary_from'], int)][
                                          :20]
                    answer_vacancy_list = sort_data.sort_vacancies('salary_from', actual_vacancy_list)

                elif choice_action == 9:
                    print("Программа завершена.")
                    break
                else:
                    print("Операцию на этот номер пока не назначили. Попробуйте ещё раз")
                    continue

                print_resalt(answer_vacancy_list)

            except ValueError:
                print("Не верный ввод, вводимые данные должны быть целым числом. Попробуйте ещё раз")
                continue
        else:
            print("Поиск не дал результатов. Попробуйте запустить программу снова с более точным запросом.")
            break


def print_resalt(vacancy_list):
    '''Выводит результат запроса пользовотеля на экран'''
    for line_vacancy in vacancy_list:
        print(PerformanceVacancies(line_vacancy).__str__())

