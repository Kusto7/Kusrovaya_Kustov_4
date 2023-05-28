from abc import ABC, abstractmethod
import json
import os
import requests

SUPERJOB_API_KEY = os.environ.get('SUPERJOBAPI')


class Get_service_API(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Get_service_API):

    def get_vacancies(self, name_job=None):
        user_param_count = int(input("Сколько вакансий загрузить?"))
        # user_param_town = input("Из какого города загрузить вакансии?").lower
        # response = requests.get('https://api.hh.ru/areas/').json()
        # for town in response['objects']:
        #     if user_param_town == town['title'].lower():
        #         user_param_town = town['id']
        #     else:
        #         continue
        # if user_param_town is None:
        #     print('Не удалось найти город, выбираю регион Москва')
        #     user_param_town = 4
        # else:
        #     pass
        name_job = input('Введите ключевые слова для поиска. Обязательно EN.')
        params = {
            'text': name_job,
            'area': 1,
            'per_page': user_param_count
        }
        response = requests.get('https://api.hh.ru/vacancies', params)
        return response.json()


class SuperJobAPI(Get_service_API):

    def get_vacancies(self):
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        # while True:
        #     try:
        #         user_param_count = int(input("Сколько вакансий загрузить?"))
        #     except ValueError:
        #         print("Мне нужно число.")
        #         continue
        #     else:
        #         id_town = user_param_count
        #         break
        user_param_count = int(input("Сколько вакансий загрузить?"))
        # user_param_town = input("Из какого города загрузить вакансии?").lower
        # response = requests.get('https://api.superjob.ru/2.0/%s' % 'towns/', headers=headers).json()
        # for town in response['objects']:
        #     if user_param_town == town['title'].lower():
        #         user_param_town = town['id']
        #     else:
        #         continue
        # if user_param_town is None:
        #     print('Не удалось найти город, выбираю регион Москва')
        #     user_param_town = 4
        # else:
        #     pass
        name_job = input('Введите ключевые слова для поиска. Обязательно EN.')
        params = {
            'count': user_param_count,
            'town': 4,
            'keyword': name_job
            }
        response = requests.get('https://api.superjob.ru/2.0/%s' % 'vacancies/', params, headers=headers)
        return response.json()

# hh_api = HeadHunterAPI()
# # superjob_api = SuperJobAPI()
# #
# # # Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
# # superjob_vacancies = superjob_api.get_vacancies("Python")
# #
# # # print(hh_vacancies)
# # for i in superjob_vacancies['objects']:
# #     print(i['profession'])
# # # print(superjob_vacancies['objects'][1]['profession'])
#
# print(hh_vacancies)
