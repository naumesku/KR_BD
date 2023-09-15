

class Vacancies:
    """Родительский класс для работы с АПИ"""

    def __init__(self, url: str, headers: str, params: dict) -> None:
        self.url = url
        self.headers = headers
        self.params = params
        self.response = requests.get(url=self.url, headers=self.headers, params=self.params)