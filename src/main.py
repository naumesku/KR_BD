from utils import all_vacancies_json, create_database, users_work
from data.config import PATH_VACANCIES, PATH_COMPANY

def main():
    all_vacancies_json(PATH_COMPANY, PATH_VACANCIES)
    #Наполняем актуальными вакансиями файл vacancies.json

    create_database(PATH_COMPANY, 'companies', PATH_VACANCIES, 'vacancies')
    #Создаем базу данных и таблицы и наполняем актуальными вакансиями

    print('Вакансии загружены в базу данных (валюта "РУБ")')

    users_work()
    #Начинаем работу с пользователем

if __name__ == "__main__":
    main()
