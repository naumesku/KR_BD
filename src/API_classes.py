import requests
from pprint import pprint

class API:
    """Родительский класс для работы с АПИ"""

    def __init__(self, url: str, headers: str, params: dict) -> None:
        self.url = url
        self.headers = headers
        self.params = params
        self.response = requests.get(url=self.url, headers=self.headers, params=self.params)


    def __str__(self) -> str:
        """Выводит в консоль информацию для пользователя."""
        return str(f"{self.url})")

    def __repr__(self) -> str:
        """Выводит в консоль информацию для разработчика."""
        pass



class HH(API):
    def __init__(self, url: str, headers: str, params: dict) -> None:
        super().__init__(url, headers, params)



class superjob(API):
    def __init__(self, url: str, headers: str, params: dict) -> None:
        super().__init__(url, headers, params)
