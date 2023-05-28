import json

from src.ApiConnect import SuperJobAPI, HeadHunterAPI
from src.vacancy import Vacancy

ALL_VACANCY = []


def add_vacancies_superjob():
    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies()
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
    hh_vacancies = hh_api.get_vacancies()
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
        vacancy.vacancy_to_create()
    Vacancy.json_file_vacancy()


def filter_vacancy(salary, keyword):
    with open('all_vacancy.json', 'r', encoding='utf-8') as file:
        data_all_vacancy = json.load(file)
        del_vacancy = 0
        while True:
            for vacancy in data_all_vacancy['AllVacancy']:
                if vacancy['Заработная плата'] == 'З/П не указана':
                    continue
                elif vacancy['Заработная плата'] >= salary:
                    if keyword in vacancy['Требования к работе']:
                        info_vacancy = f"\nНазвания вакансии — {vacancy['Профессия']}\n" \
                                       f"Заработная плата — {vacancy['Заработная плата']}\n" \
                                       f"Требования — {vacancy['Требования к работе']}\n" \
                                       f"Ссылка на вакансию: {vacancy['Ссылка на вакансию']}\n"
                        data_all_vacancy['AllVacancy'].pop(del_vacancy)
                        return info_vacancy
                else:
                    del_vacancy += 1
                    print('Не нашел подходящую вакансию, давай снизим требования.')


def user_interaction():
    print('Привет! Эта программа может показать тебе нужные вакансии \n'
          'Я буду задавать нужные вопросы для отбора вакансий \n'
          'Если готов, нажми Enter')
    user_input = input()
    if user_input == '':
        print("С каких платформ ты хочешь посмотреть вакансии? SuperJob или HH.ru? \n"
              "Если хочешь собрать информацию с двух платформ, набери: «С двух» \n"
              "Если нужна конкретная платформа, укажи её. Например: «Супер», «ХХ», «Super», «HH»")
        while True:
            user_choice_platform = input().lower()
            if user_choice_platform in ['супер', 'super']:
                add_vacancies_superjob()
                break
            elif user_choice_platform in ['хх', 'hh']:
                add_vacancies_hh()
                break
            elif user_choice_platform == "с двух":
                add_vacancies_superjob()
                add_vacancies_hh()
                break
            else:
                print('Проверь написание платформы.')
        print('Хорошо, загружаю вакансии. Подожди, пожалуйста.')
        save_all_vacancy_to_file()
        print('Теперь давай более детально уточним, что тебе интересно.')
        user_salary = input('Укажи минимальную ЗП, которую ты хочешь. Ничего не указывай, если не важно.')
        user_keyword = input('Укажи любые слова, которые важны для поиска вакансии в требованиях \n'
                             'Например: «SQL», «Django» и т.д.')
        if user_salary == '':
            user_salary = 0
            print(filter_vacancy(int(user_salary), user_keyword))
        else:
            print(filter_vacancy(int(user_salary), user_keyword))
        while True:
            print('\nПоказываю следующую вакансию?')
            user_answer = input('YES/NO').lower()
            if user_answer in ['yes']:
                print(filter_vacancy(int(user_salary), user_keyword))
            else:
                print('Всего хорошего!')
                break
    elif user_input is not None:
        print('Так у нас ничего не получится.')
