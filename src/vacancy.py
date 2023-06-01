import json
import sys


class Vacancy:

    """Класс для работы с вакансиями"""

    all_vacancy = {'AllVacancy': []}  # Для корректного создания json файла
    del_vacancy = 0  # Для удаления вакансии из файла

    def __init__(self, name_profession: str, salary: int, url: str, requirement: str):
        self.vacancy = None
        self.name_profession = name_profession
        if not isinstance(salary, int):
            self.salary = "З/П не указана"
        elif salary == 0:
            self.salary = "З/П не указана"
        elif salary < 10000:
            self.salary = "З/П не указана"
        else:
            self.salary = salary
        self.url = url
        self.requirement = requirement

    @classmethod
    def file_vacancies_clear(cls):

        """Метод для очистки файла перед работой"""

        try:
            with open('all_vacancy.json', 'w', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            pass

    def vacancy_to_create(self):

        """Метод для создания объектов для json файла"""

        self.vacancy = {'Профессия': self.name_profession,
                        'Заработная плата': self.salary,
                        'Ссылка на вакансию': self.url,
                        'Требования к работе': self.requirement
                        }
        Vacancy.all_vacancy['AllVacancy'].append(self.vacancy)

    @classmethod
    def json_file_vacancy(cls):

        """Метод для записи информации в json файл"""

        with open('all_vacancy.json', 'a', encoding='utf-8') as file:
            json.dump(Vacancy.all_vacancy, file, indent=2, ensure_ascii=False)

    @classmethod
    def save_all_vacancy_to_file(cls, ALL_VACANCY):

        """Общий метод для включения остальных методов по очистке, создании и сохранении информации"""

        Vacancy.file_vacancies_clear()
        for vacancy in ALL_VACANCY:
            vacancy.vacancy_to_create()
        Vacancy.json_file_vacancy()

    @classmethod
    def del_vacancy_in_file(cls, data_all_vacancy):

        """Метод для удаления вакансии из файла"""

        with open('all_vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(data_all_vacancy, file, ensure_ascii=False)

    @classmethod
    def filter_vacancy(cls, salary, keyword):
        """Метод для фильтрации вакансий в файле"""

        with open('all_vacancy.json', 'r', encoding='utf-8') as file:
            data_all_vacancy = json.load(file)
            try:
                while True:
                    for vacancy in data_all_vacancy['AllVacancy']:
                        info_vacancy = f"\nНазвания вакансии — {vacancy['Профессия']}\n" \
                                       f"Заработная плата — {vacancy['Заработная плата']}\n" \
                                       f"Требования — {vacancy['Требования к работе']}\n" \
                                       f"Ссылка на вакансию: {vacancy['Ссылка на вакансию']}\n"
                        try:
                            if keyword.lower() in vacancy['Требования к работе'].lower():
                                try:
                                    if vacancy['Заработная плата'] >= salary:
                                        data_all_vacancy['AllVacancy'].pop(Vacancy.del_vacancy)
                                        Vacancy.del_vacancy_in_file(data_all_vacancy)
                                        Vacancy.del_vacancy += 1
                                        return info_vacancy
                                except TypeError:
                                    print('\nЭта вакансия, которая не попадает под критерий зарплаты.')
                                    return info_vacancy
                            else:
                                data_all_vacancy['AllVacancy'].pop(Vacancy.del_vacancy)
                                Vacancy.del_vacancy_in_file(data_all_vacancy)
                                Vacancy.del_vacancy += 1
                        except AttributeError:
                            pass
            except IndexError:
                print('Не нашёл подходящую вакансию. Попробуй загрузить больше вакансий или снизить требования.')
                sys.exit()
