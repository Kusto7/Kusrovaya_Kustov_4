from src.ApiConnect import SuperJobAPI, HeadHunterAPI
from src.vacancy import Vacancy


ALL_VACANCY = []


def add_vacancies_superjob():
    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies("Python")
    for info in superjob_vacancies['objects']:
        name_profession = info['profession']
        # salary = "".join(f"{info['payment_from']} - {info['payment_to']} {info['currency']}.")
        salary = info['payment_from']
        url = info['link']
        requirement = info['candidat']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        ALL_VACANCY.append(vacancy)
    return ALL_VACANCY


def add_vacancies_hh():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")
    for info in hh_vacancies['items']:
        name_profession = info['name']
        # if info['salary'] is None:
        #     salary = 0
        # else:
        #     salary = "".join(f"{info['salary']['from']} - {info['salary']['to']} {info['salary']['currency']}.")
        if info['salary'] is None:
            salary = 0
        else:
            salary = info['salary']['from']
        url = info['alternate_url']
        requirement = info['snippet']['requirement']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        ALL_VACANCY.append(vacancy)
    return ALL_VACANCY


def save_all_vacancy_to_file():
    Vacancy.file_vacancies_clear()
    for vacancy in ALL_VACANCY:
        vacancy.vacancy_to_save_file()
    Vacancy.json_file_vacancy()

