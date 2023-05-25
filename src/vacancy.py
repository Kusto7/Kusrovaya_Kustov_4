import json


class Vacancy:
    all_vacancy = {'AllVacancy': []}

    def __init__(self, name_profession: str, salary: int, url: str, requirement: str):
        self.vacancy = None
        self.name_profession = name_profession
        if salary == 0:
            self.salary = "З/П не указана"
        else:
            self.salary = salary
        self.url = url
        self.requirement = requirement

    @classmethod
    def file_vacancies_clear(cls):
        try:
            with open('all_vacancy.json', 'w', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            pass

    def vacancy_to_save_file(self):
        self.vacancy = {'Профессия': self.name_profession,
                        'Заработная плата': self.salary,
                        'Ссылка на вакансию': self.url,
                        'Требования к работе': self.requirement
                        }
        Vacancy.all_vacancy['AllVacancy'].append(self.vacancy)

    @classmethod
    def json_file_vacancy(cls):
        with open('all_vacancy.json', 'a', encoding='utf-8') as file:
            json.dump(Vacancy.all_vacancy, file, indent=2, ensure_ascii=False)
