from abc import ABC, abstractmethod
import os
import requests

SUPERJOB_API_KEY = os.environ.get('SUPERJOBAPI')  # Ключ API с сайта SuperJob


class Get_service_API(ABC):

    """Абстрактный класс для подключения"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Get_service_API):

    """Класс для подключения по API к сайту HH.ru"""

    def get_vacancies(self):
        user_param_count = int(input("Сколько вакансий загрузить?"))
        name_job = input('Введите ключевые слова для поиска. Обязательно EN.')
        print('Хорошо, загружаю вакансии. Подожди, пожалуйста.')
        params = {
            'text': name_job,
            'area': 1,
            'per_page': user_param_count
        }
        response = requests.get('https://api.hh.ru/vacancies', params)
        return response.json()


class SuperJobAPI(Get_service_API):

    """Класс для подключения по API к сайту SuperJob.ru"""

    def get_vacancies(self):
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        user_param_count = int(input("Сколько вакансий загрузить?"))
        name_job = input('Введите ключевые слова для поиска. Обязательно EN.')
        print('Хорошо, загружаю вакансии. Подожди, пожалуйста.')
        params = {
            'count': user_param_count,
            'town': 4,
            'keyword': name_job
            }
        response = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        return response.json()
