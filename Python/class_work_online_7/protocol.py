"""
модуль проверки данных
json файлы
csv файлы
api ответы

определить интерфейс валидатора

DataValidator
    validate

EmailValidator - валидация - проверка наличия и формат "email"
AgeValidator - валидация "age" - наличие, положительное число, меньше 0 - 120
UsernameValidator - валидация "username" - наличие, длинна больше 3 символов
до 20, наличие только буквенно-цифровых символов

run_validators(data: dict, validators: List[DataValidator]) -> List[str]
"""
import re
from typing import Protocol


class DataValidator(Protocol):
    def validate(self) -> None:
        ...


class EmailValidator:
    def validate(self, data) -> bool:
        email = data.get('email', '')
        return isinstance(email, str) and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


class AgeValidator:
    def validate(self, data) -> bool:
        age = data.get('age')
        return isinstance(age, int) and 0 <= age <= 120


class UsernameValidator:
    def validate(self, data) -> bool:
        username = data.get('username')
        return isinstance(username, str) and username.isalnum() and 3 <= len(username) <= 20


def run_validators_errors(data: dict, validators: list):
    errors = []
    for validator in validators:
        if not validator.validate(data):
            errors.append(f"Ошибка валидации: {validator.__class__.__name__}")
    return errors


validators = [EmailValidator(), AgeValidator(), UsernameValidator()]

test_right = {
    "email": 'email@gmail.com',
    "age": 12,
    "username": 'Goodname'
}

test_bad = {
    "email": 'email@gmail.',
    "age": '12',
    "username": 'Bad name'
}

for index, data in enumerate([test_right, test_bad], start=1):
    print(f'Данные {index}:')
    result = run_validators_errors(data, validators)
    if not result:
        print('Данные валидны')
    else:
        for error in result:
            print(error)
    print()
