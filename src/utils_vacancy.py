from src.ApiConnect import SuperJobAPI, HeadHunterAPI
from src.vacancy import Vacancy

ALL_VACANCY = []  # Глобальная переменная для сохранения всех вакансий с двух сайтов.


def add_vacancies_superjob():

    """Функция для создания объектов класса Vacancy от сайта SuperJob.ru"""

    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies()
    for info in superjob_vacancies['objects']:
        name_profession = info['profession']
        salary = info['payment_from']
        url = info['link']
        requirement = info['candidat']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        ALL_VACANCY.append(vacancy)
    return ALL_VACANCY


def add_vacancies_hh():

    """Функция для создания объектов класса Vacancy от сайта HH.ru"""

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies()
    for info in hh_vacancies['items']:
        name_profession = info['name']
        if info['salary'] is None:
            salary = 0
        else:
            salary = info['salary']['from']
        url = info['alternate_url']
        requirement = info['snippet']['requirement']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        ALL_VACANCY.append(vacancy)
    return ALL_VACANCY


def user_interaction():

    """Функция для работы с пользователем"""

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
        Vacancy.save_all_vacancy_to_file(ALL_VACANCY)
        print('Теперь давай более детально уточним, что тебе интересно.')
        user_salary = input('Укажи минимальную ЗП, которую ты хочешь. Ничего не указывай, если не важно.')
        user_keyword = input('Укажи любые слова, которые важны для поиска вакансии в требованиях \n'
                             'Например: «SQL», «Django» и т.д.')
        if user_salary == '':
            user_salary = 0
            print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
        else:
            print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
        while True:
            print('\nПоказываю следующую вакансию?')
            user_answer = input('YES/NO').lower()
            if user_answer in ['yes']:
                print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
            else:
                print('Всего хорошего!')
                break
    elif user_input is not None:
        print('Так у нас ничего не получится.')
