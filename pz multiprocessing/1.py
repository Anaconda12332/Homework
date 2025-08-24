"""
производитель кладет от 1 до 10
потребитель берет числа из очереди и печатает их квадрат
когда производитель закончит, кладет STOP
"""
from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(1, 11):
        q.put(i)
        print(f'Производитель кладет {i}')
        time.sleep(1)
    q.put('STOP')


def consumer(q):
    while True:
        num = q.get()
        if num == 'STOP':
            break
        print(f'Потребитель берет {num}')
        print(f'[Потребитель] квадрат: {num ** 2}')


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Все процессы завершены')
