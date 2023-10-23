from utils import all_vacancies_json, create_database
from data.config import PATH_VACANCIES, PATH_COMPANY

def main():
    all_vacancies_json(PATH_COMPANY, PATH_VACANCIES)
    #Наполняем актуальными вакансиями файл vacancies.json

    create_database(PATH_COMPANY, 'companies', PATH_VACANCIES, 'vacancies')
    #Создаем базу данных и таблицы и наполняем актуальными данными таблицы

    #
    # text_search = str(input("Введите слово или фразу для поиска: "))
    #     # Ищем вакансии.
    #     # Сохраняем в файл.
    #     # Выводим без сотрировки
    # users_work (text_search)
    # # Запускаем программу для работы с пользователем

if __name__ == "__main__":
    main()
