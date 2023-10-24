import psycopg2
from data.config import PARAMS_BD

class DBManager():
    '''Класс для поиска вакансий на сайте HH.ru по id_работодателя '''
    def __init__(self) -> None:
        self.params = PARAMS_BD
        self.database_name = 'vacansies_hh'
        self.conn = psycopg2.connect(dbname=self.database_name, **self.params)

    def cursor(self, reqest):
        # Получает запрос, подключается в БД, выдает результат
        with  self.conn.cursor() as cur:
            cur.execute(f'{reqest}')
            rows = cur.fetchall()
            for row in rows:
                print(row)
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        # Получает список всех компаний и количество вакансий у каждой компании
        self.cursor('''SELECT company_title, COUNT(*) AS quin
                    FROM companies JOIN vacancies USING (company_id)
                    GROUP BY company_id''')

    def get_all_vacancies(self):
        # Получает список всех вакансий
        self.cursor('''SELECT company_title, vacacy_title, salary_from ,vacacy_url FROM companies 
                    JOIN vacancies USING (company_id)''')

    def get_avg_salary(self):
        # Получает среднюю зарплату по вакансиям
        self.cursor('''SELECT AVG(salary_from) FROM vacancies
                    WHERE salary_from IS NOT NULL''')

    def get_vacancies_with_higher_salary(self):
        # Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        self.cursor('''SELECT company_title, vacacy_title, salary_from ,vacacy_url FROM companies 
                JOIN vacancies USING (company_id)
                WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)''')

    def get_vacancies_with_keyword(self, user_request):
        # Получает список всех вакансий, в названии которых содержатся переданные в метод слова
        self.cursor(f'''SELECT company_title, vacacy_title, salary_from ,vacacy_url FROM companies 
                    JOIN vacancies USING (company_id)
                    WHERE vacacy_title LIKE '%{user_request}%' ''')