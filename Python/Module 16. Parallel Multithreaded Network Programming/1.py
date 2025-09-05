"""
Задание 1
При старте приложения запускаются три потока.
Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения. Когда список
заполнен оба потока запускаются. Первый поток находит
сумму элементов списка, второй поток среднеарифметическое
значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран.
"""
import random
import threading
import time

numbers = []
event = threading.Event()


def full_list():
    print('1 поток запущен')
    for i in range(10):
        numbers.append(random.randint(1, 100))
    time.sleep(0.5)
    print('Список заполнен:', numbers)
    event.set()


def sum_list():
    print('2 поток ожидает')
    event.wait()
    print('2 поток запущен')
    summ = sum(numbers)
    print('Сумма найдена:', summ)


def average():
    print('3 поток ожидает')
    event.wait()
    print('3 поток запущен')
    if numbers:
        average = sum(numbers) / len(numbers)
        print('Среднеарифметическое найдено:', average)


thread_1 = threading.Thread(target=full_list)
thread_2 = threading.Thread(target=sum_list)
thread_3 = threading.Thread(target=average)

thread_1.start(),
thread_2.start(),
thread_3.start()

thread_1.join(),
thread_2.join(),
thread_3.join()
