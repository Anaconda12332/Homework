"""
Event
несколько рабочих процессов, которые выводят что жу и останавливаются
в ожидании сигнала от главного процесса
главный ждет 3 сек потом event.set()
рабочие продолжают, выводят и выполняют простую операцию - **
"""
from multiprocessing import Process, Event
import time


def square(event, nums, i):
    print(f'Процесс {i} ждет события')
    event.wait()
    for num in nums:
        print(f'Процесс {i} возводит {num} в квадрат и получает {num ** 2}')
        time.sleep(0.5)


if __name__ == '__main__':
    event = Event()
    nums = [1, 2, 3, 4, 5]

    process = [Process(target=square, args=(event, nums, i)) for i in range(5)]

    for p in process:
        p.start()

    time.sleep(3)
    event.set()

    for p in process:
        p.join()

    print('Все процессы завершены')
