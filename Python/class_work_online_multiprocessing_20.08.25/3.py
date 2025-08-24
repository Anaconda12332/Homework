"""
3
два процесса
первый "таймер", каждую секунду печатает, сколько времени прошло
второй "работа", который за 5 секунд выполняет задачу
(например сумма от 1 до 10кк)
"""
from multiprocessing import Process
import time


def timer():
    t = 0
    while True:
        time.sleep(1)
        t += 1
        print(f"Прошло {t} секунд")


def work():
    count = 1
    for i in range(1, 10000000):
        print(f'{i} + {count} = {count + i}')
        count += i
        time.sleep(5)


if __name__ == '__main__':
    process = []
    p1 = Process(target=timer)
    p2 = Process(target=work)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
