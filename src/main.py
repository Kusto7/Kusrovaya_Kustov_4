import os

from src.utils_vacancy import add_vacancies_superjob, add_vacancies_hh, save_all_vacancy_to_file

SUPERJOB_API_KEY = os.environ.get('SUPERJOBAPI')

if __name__ == "__main__":
    add_vacancies_hh()
    add_vacancies_superjob()
    save_all_vacancy_to_file()


