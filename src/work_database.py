import psycopg2, json
from data.config import PARAMS_BD, PATH_VACANCIES, PATH_COMPANY



def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

    conn = psycopg2.connect(dbname='postgres', **params)

    with conn.cursor() as cur:
        conn.autocommit = True
        cur.execute(f"DROP DATABASE {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")
        conn.commit()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE companies(
                company_id INT PRIMARY KEY, company_title VARCHAR(35) NOT NULL);

        CREATE TABLE vacacies (
                vacacy_id INT PRIMARY KEY,
                company_id INT REFERENCES companies(company_id),
                vacacy_title VARCHAR(55) NOT NULL,
                salary_from INT,
                vacacy_url TEXT);
                ''')
        conn.commit()
    conn.close()

create_database("vacacies_hh", PARAMS_BD)


"""Скрипт для заполнения данными таблиц в БД Postgres."""
def filling_table(path_file, params: dict, database_name: str, table):
    '''Наполняет таблицу данными из csv файла'''
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        with open(PATH_COMPANY, 'r', encoding='UTF-8') as f:
            data_companies = json.load(f)
            # print(data.values())
            for name, id in data_companies.items():
                values = ("%s," * len(data_companies))[:-1]
                cur.execute(f"INSERT INTO {table} VALUES ({values})", data.values())
                conn.commit()


    
    
    
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="qqqzzz") as conn:
        with conn.cursor() as cur:
            with open(path, 'r') as csv_file:
                csv_data = csv.reader(csv_file)
                next(csv_data)
                for line in csv_data:
                    values = ("%s," * len(line))[:-1]
                    cur.execute(f"INSERT INTO {table} VALUES ({values})", line)
                    conn.commit()
    conn.close()

if __name__ == '__main__':
    filling_table(PATH_CUSTOMERS_DATA, "customers")
    filling_table(PATH_EMPLOYEES, "employees")
    filling_table(PATH_ORDERS, "orders"

