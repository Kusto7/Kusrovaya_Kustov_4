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
        params = {
            'text': name_job,
            'area': 1,
            'per_page': 10
        }
        response = requests.get('https://api.hh.ru/vacancies', params)
        return response.json()


class SuperJobAPI(Get_service_API):

    def get_vacancies(self, name_job=None):
        params = {
            'count': 10,
            'town': 4,
            'keyword': name_job
        }
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
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
