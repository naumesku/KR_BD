import psycopg2
from data.config import PARAMS_BD

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
