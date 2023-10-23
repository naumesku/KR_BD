import json
from work_json import WorkJson
from utils import all_vacancies_json
from data.config import PATH_COMPANY, PATH_VACANCIES

all_vacancies_json(PATH_COMPANY, PATH_VACANCIES)

work = WorkJson()
for line in work.get_vacancies(PATH_VACANCIES):
    print(line)
