# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

from abc import ABC, abstractmethod
import json
import pickle


class Operation(ABC):
    @abstractmethod
    def actions(self):
        pass


class Stadium(Operation):
    def __init__(self, user_length, user_width):
        self.length = user_length
        self.width = user_width
        self.dict = {
            'length ': user_length,
            'width': user_width
        }

    def actions(self):
        return self.dict


class Save:
    def save_json(self, parameters) -> str:
        packed = json.dumps(parameters, ensure_ascii=False)
        print(f'Ваш файл сохранен в формате JSON:\n{packed}')
        return packed

    def save_picle(self, parameters) -> str:
        packed = pickle.dumps(parameters)
        print(f'Ваш файл сохранен в формате Picle:\n{packed}')
        return packed


class Load:
    def load_json(self, packed) -> dict:
        params_new = json.loads(packed)
        print(f'Ваш файл загружен из формата JSON:\n{params_new}')
        return params_new

    def load_picle(self, packed) -> dict:
        params_new = pickle.loads(packed)
        print(f'Ваш файл загружен из формата Picle:\n{params_new}')
        return params_new


stadium = Stadium('105 метров', "68 метров")
save = Save()
load = Load()

parameters = stadium.actions()

save_json = save.save_json(parameters)
save_picle = save.save_picle(parameters)

load_json = load.load_json(save_json)
load_picle = load.load_picle(save_picle)
