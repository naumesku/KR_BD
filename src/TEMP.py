import json
from work_json import WorkJson
from utils import all_vacancies_json
from data.config import PATH_COMPANY, PATH_VACANCIES

from db_manager import DBManager

db = DBManager()
# db.get_vacancies_with_higher_salary()
# db.get_all_vacancies()
# db.get_companies_and_vacancies_count()
db.get_vacancies_with_keyword("сборщик")

