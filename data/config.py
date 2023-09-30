from pathlib import Path

PATH_VACANCIES = Path(__file__).parent.joinpath("vacancies.json")
# Путь до json-файла с вакансиями

PATH_LOG = Path(__file__).parent.joinpath("log.txt")
# Путь до txt-файла с  ошибочными вакансиями

HH_VACANCIES_URL = "https://api.hh.ru/vacancies"
# Базовый URL для сайта HH.ru
HH_HEADERS = {"User-Agent": "naumesku@gmail.com"}
# Заголовок для сайта HH.ru - обязательное требование
COUNT_HH = 100
#Количество вакансий для поиска на сайте HH.ru

BASES_ID_SJ = 2996
# Базовый ID для сайта SJ.ru
SECRET_KEY_SJ = "v3.r.111847284.4352b84a837eb770efe1e81582e6a49a021cac26.f32f2ba64ad2dd647ad8173eef63ed25154ee812"
# Секретный ключ для сайта SJ.ru
SJ_VACANCIES_URL = "https://api.superjob.ru/2.0/vacancies/"
# Базовый URL для сайта HH.ru
SJ_HEADERS = {"X-Api-App-Id": SECRET_KEY_SJ}
# Заголовок для сайта HH.ru - обязательное требование
COUNT_SJ = 100
#Количество ваканссий для поиска на сайте SJ

#Котировки для конвертации валют
currency_change = {
        "AUD": 0.01620564,
        "AZN": 0.0177006,
        "GBP": 0.0084734,
        "AMD": 4.0319979,
        "BYR": 0.03391957668,
        "BR": 0.03391957668,
        "Br": 0.03391957668,
        "BYN": 0.03391957668,
        "BGN": 0.01914894,
        "BRL": 0.0512547,
        "HUF": 3.78179067789,
        "VND": 250.5154355,
        "HKD": 0.081277,
        "GEL": 0.0279867,
        "DKK": 0.0729847,
        "AED": 0.03824267,
        "USD": 0.01041212,
        "EUR": 0.00978009,
        "EGP": 0.3216675,
        "INR": 0.86478259,
        "IDR": 160.3155009,
        "KZT": 4.955745,
        "CAD": 0.014041788,
        "QAR": 0.0379001785,
        "KGS": 0.9236595,
        "CNY": 0.076095,
        "MDL": 0.188905,
        "NZD": 0.017567,
        "NOK": 0.111731469,
        "PLN": 0.0448887,
        "RON": 0.04863387,
        "XDR": 0.00790822,
        "SGD": 0.0142292,
        "TJS": 0.114122,
        "THB": 0.376282,
        "TRY": 0.281402,
        "TMT": 0.03644248,
        "UZS": 126.923848,
        "SO'M": 0.007873,
        "UAH": 0.384575,
        "CZK": 0.2393226,
        "SEK": 0.116402375,
        "CHF": 0.00943338,
        "RSD": 1.14505958,
        "ZAR": 0.1962558,
        "KRW": 13.91893058,
        "JPY": 1.5372459
}