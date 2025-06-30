"""
вы работаете с библиотекой, которую нельзя модифицировать напрямую (например,
она закрыта или поставляется в бинарном виде). Ваша задача — изменить
поведение функции этой библиотеки, не трогая исходный код библиотеки.
# external_library.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

Импортируйте функции greet и add из внешнего модуля external_library.

С помощью монкипатчинга:
Переопределите функцию greet, чтобы она всегда возвращала строку:
"Access denied."
Переопределите функцию add, чтобы она логировала аргументы в файл log.txt
и возвращала результат сложения.
Реализуйте восстановление исходного поведения обеих функций после выполнения
патчинга (используйте сохранение оригинальных функций).
"""
from external_library import greet, add

original_greet = greet
original_add = add


def patch_greet(name):
    return "Access denied."


def patch_add(a, b):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Выполнено сложение {a} и {b}\n")
    return original_add(a, b)


greet = patch_greet
add = patch_add

print(greet("John"))
print(add(1, 2))

greet = original_greet
add = original_add

print('\nПроверка восстановления поведения:')
print(greet("John"))
print(add(1, 2))
