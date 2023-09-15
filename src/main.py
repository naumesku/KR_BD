import requests
from pprint import pprint

word_search = "python"
VACANCIES_URL = "https://api.hh.ru/vacancies"
head = {"User-Agent": "naumesku@gmail.com"}
parameters = {"text": word_search, "area": 2, "date_from": "2023-09-13"}
response = requests.get(url=VACANCIES_URL, params=parameters, headers=head)

pprint(response.json())
