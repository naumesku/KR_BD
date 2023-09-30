class PerformanceVacancies():
    """Класс для представления вакансии"""
    #
    def __init__(self, data_vacancy: dict) -> None:
        self.data_vacancy = data_vacancy

        self.vacancy_id = self.data_vacancy.get('id')
        self.vacancy_name = self.data_vacancy.get('name')
        self.date_publishedt = self.data_vacancy.get('date_publishedt')
        self.salary_from = self.data_vacancy.get('salary_from')
        self.salary_to = self.data_vacancy.get('salary_to')
        self.salary_currency = "руб."
        self.responsibility = self.data_vacancy.get('responsibility')
        self.town = self.data_vacancy.get('town')
        self.url = self.data_vacancy.get('url')

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        return (f'''
        id: {self.vacancy_id}
        Вакансия: {self.vacancy_name}
        Город: {self.town}
        Дата публикации: {self.date_publishedt}
        Заработная плата от: {self.salary_from} до: {self.salary_to} {self.salary_currency}
        Обязанности: {self.responsibility}
        Ссылка на вакансию: {self.url}
        ''')

class SortVacancies():
    """Класс для сортировки списка вакансий по заданному параметру"""

    def sort_vacancies(self, user_param, all_vacancy, reverse=True):
        """Принимает список вакансий, сортирует его по заданному параметру, возвращет измененный список"""
        self.all_vacancy = all_vacancy
        self.user_param = user_param
        operations_sorted = sorted(self.all_vacancy, key=lambda vacancy: vacancy[self.user_param], reverse=reverse)
        return operations_sorted
