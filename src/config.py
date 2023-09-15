
VACANCIES_URL = "https://api.hh.ru/vacancies"
# Базовый URL для сайта HH.ru

headers = {"User-Agent": "naumesku@gmail.com"}
# Заголовок для сайта HH.ru - обязательное требование



head = {"User-Agent": "naumesku@gmail.com"}
parameters = {"text": word_search, "area": 2, "date_from": "2023-09-13"}
response = requests.get(url=VACANCIES_URL, params=parameters, headers=head)

pprint(response.json())