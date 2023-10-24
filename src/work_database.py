import psycopg2
import json
from data.config import PARAMS_BD, PATH_VACANCIES, PATH_COMPANY

class CREATE_DB():
    '''Класс для создания и наполнения базы данных и таблиц ы ней'''

    def __init__(self) -> None:
        self.params = PARAMS_BD
        self.database_name = 'vacansies_hh'

    def create_database(self):
        """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

        conn = psycopg2.connect(dbname='postgres', **self.params)

        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute(f"DROP DATABASE {self.database_name}")
            cur.execute(f"CREATE DATABASE {self.database_name}")
            conn.commit()
        conn.close()

        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute('''
            CREATE TABLE companies(
                    company_id INT PRIMARY KEY, company_title VARCHAR(35) NOT NULL);
            CREATE TABLE vacancies (
                    vacacy_id INT PRIMARY KEY,
                    company_id INT REFERENCES companies(company_id),
                    vacacy_title VARCHAR(155) NOT NULL,
                    salary_from INT,
                    vacacy_url TEXT);
                    ''')
            conn.commit()
        conn.close()

    def filling_table(self, path,  table_name):
        '''Наполняет таблицу данными из json файла'''
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            with open(path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
                for line in data:
                    values = ("%s," * len(line))[:-1]
                    cur.execute(f"INSERT INTO {table_name} VALUES ({values})", tuple(line.values()))
                    conn.commit()
