"""
Пользователь с клавиатуры вводит путь к файлу.
После чего запускаются три потока. Первый поток заполняет файл
случайными числами. Два других потока
ожидают заполнения. Когда файл заполнен оба потока
стартуют. Первый поток находит все простые числа, второй поток
факториал каждого числа в файле. Результаты
поиска каждый поток должен записать в новый файл. На
экран необходимо отобразить статистику выполненных
операций.
"""

import random
import threading
import time

file_name = '2/' + input('Введите имя файла: ').strip()
event = threading.Event()


def full_list():
    print('1 поток запущен')
    with open(file_name, 'w') as file:
        for i in range(10):
            file.write(str(random.randint(1, 100)) + '\n')
            print(f'Идет заполнение файла {(i+1) * 10}%', end='\r')
            time.sleep(0.3)
    print()
    event.set()


def simple_numbers():
    event.wait()
    print('2 поток запущен')
    simple_set = set()
    with open(file_name, 'r') as file:
        print('Идет поиск простых чисел')
        for line in file:
            number = int(line)
            simple_set.add(number) if is_simple(number) else None

    with open('2/simple.txt', 'w') as simple_file:
        for number in simple_set:
            simple_file.write(str(number) + '\n')
    print('Простые числа найдены')


def is_simple(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


def factorial_numbers():
    event.wait()
    print('3 поток запущен')
    with open(file_name, 'r') as file:
        print('Идет поиск факториалов')

        for line in file:
            number = int(line)
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            with open('2/factorial.txt', 'a') as factorial_file:
                factorial_file.write(str(factorial) + '\n')
    print('Факториалы найдены')


thread_1 = threading.Thread(target=full_list)
thread_2 = threading.Thread(target=simple_numbers)
thread_3 = threading.Thread(target=factorial_numbers)

thread_1.start(),
thread_2.start(),
thread_3.start()

thread_1.join(),
thread_2.join(),
thread_3.join()
