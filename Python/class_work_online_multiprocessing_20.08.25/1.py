"""
1
запускать два процесса
первый считает от 1 до 10, печатает числа
второй считает от 10 до 1, печатает числа
каждый выводит результат с задержкой в 0.5 сек
"""
from multiprocessing import Process
import time


def count(name):
    print(f"процесс {name} запущен")
    if name == 2:
        for i in reversed(range(1, 11)):
            print(f'процесс {name}', i)
            time.sleep(0.5)
    else:
        for i in range(1, 11):
            print(f'процесс {name}', i)
            time.sleep(0.5)
    print(f'процесс {name} завершен')


if __name__ == '__main__':
    process = []
    for i in range(1, 3):
        p = Process(target=count, args=(i,))
        p.start()
        process.append(p)

    for p in process:
        p.join()
