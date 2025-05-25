# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицыв качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

from abc import ABC, abstractmethod
import json


class DictOperation(ABC):
    @abstractmethod
    def execute(self, dict, extra=None):
        pass


class Appends(DictOperation):
    def execute(self, dict, extra):
        key, value = extra
        dict[key] = value
        print(f'Обновленный словарь:\n{dict}')
        return dict


class DellItem(DictOperation):
    def execute(self, dict, extra):
        if extra in dict:
            key = extra
            del dict[key]
            print(f'Обновленный словарь:\n{dict}')
        else:
            print('Ошибка: Такой страны нет в словаре!')
        return dict


class Check(DictOperation):
    def execute(self, dict, extra):
        if extra in dict:
            print(f'Столица {dict[extra]}')
        else:
            print(f'Страны {extra} нет в списке!')
        return dict


class Change(DictOperation):
    def execute(self, dict, extra):
        key, value = extra
        if key in dict:
            dict[key] = value
            print(f'Обновленный словарь:\n{dict}')
        else:
            print(f'Страны {key} нет в списке!')
        return dict


class SaveJson(DictOperation):
    def execute(self, dict, extra=None) -> str:
        packed_dict = json.dumps(dict, ensure_ascii=False)
        print(f'Ваш файл сохранен в формате JSON:\n{packed_dict}')
        return packed_dict


class LoadJson(DictOperation):
    def execute(self, dict, extra) -> dict:
        if isinstance(extra, str):
            dict_new = json.loads(extra)
            print(f'Ваш файл загружен из формата JSON:\n{dict_new}')
            return dict_new
        else:
            return dict


class UserDict:
    def __init__(self, user_dict):
        self.dict = user_dict
        self.pack = None

    def get_conteiner(self):
        return self.dict

    def upload_dict(self, new_dict):
        self.dict = new_dict

    def upload_json(self, new_dict):
        self.pack = new_dict

    def start(self, actions: DictOperation, extra=None):
        if isinstance(actions, SaveJson):
            new_dict = actions.execute(self.get_conteiner(), extra)
            self.upload_json(new_dict)
        elif isinstance(actions, LoadJson):
            new_dict = actions.execute(self.get_conteiner(), extra=self.pack)
            self.upload_dict(new_dict)
        else:
            new_dict = actions.execute(self.get_conteiner(), extra)
            self.upload_dict(new_dict)


class Menu:
    def __init__(self, user_dict: UserDict):
        self.user_dict = user_dict

    def run(self):
        count = 1
        while count:
            select = input('Какое действие вы хотите выпонить?\n'
                           '1-Добавить элемент в словарь\n'
                           '2-Удалить элемент из словаря\n'
                           '3-Найти значение по ключу\n'
                           '4-Заменить элемент в словаре\n'
                           'Для сохранения данных(JSON) нажмите "5"\n'
                           'Для загрузки данных(JSON) нажмите "6"\n'
                           'Для выхода из меню нажмите "0"\n'
                           'Укажите цифру: ')
            match select:
                case '1':
                    country = input('Укажите страну для добавления: ')
                    capital = input('Укажите столицу для добавления: ')
                    obj.start(Appends(), extra=(country, capital))

                case '2':
                    obj.start(DellItem(), input('Укажите страну для '
                                                'удаления: '))
                case '3':
                    obj.start(Check(), input('Укажите страну для '
                                             'получения столицы: '))
                case '4':
                    country = input('Укажите страну для '
                                    'замены столицы: ')
                    capital_new = input('Укажите новую столицу: ')
                    obj.start(Change(), extra=(country, capital_new))
                case '5':
                    obj.start(SaveJson())
                case '6':
                    obj.start(LoadJson())
                case '0':
                    count = 0


user_dict = {
    'Великобритания': 'Лондон',
    'Ирландия': 'Дублин',
    'Германия': 'Берлин',
    'Нидерланды': 'Амстердам',
    'Бельгия': 'Брюссель'
}

obj = UserDict(user_dict)
Menu = Menu(obj)
Menu.run()
