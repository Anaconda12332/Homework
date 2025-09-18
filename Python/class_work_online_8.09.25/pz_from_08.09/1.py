"""
есть производитель , который кладёт задачи (строки) в очередь
есть несколько потребителей, которые берут задачи из очереди и обрабатывают их
производитель должен положить в очередь ограниченное количество задач.
например, 10
после завершения добавления задач производитель кладёт в очередь специальные
маркеры завершения, чтобы сигнализировать потребителям о конце работы
потребители должны завершить работу после получения маркера None
"""
from threading import Thread, Condition
import threading
import random
from queue import Empty, Queue
import time


def producer(condition, buffer, strings):
    name = threading.current_thread().name
    for i in strings:
        with condition:
            while buffer.full():
                print('[Queue] Буфер полон, ожидание...')
                condition.wait()
            buffer.put(i)
            print(f'{name} добавил {i} в буфер')
            condition.notify()
            time.sleep(random.uniform(0.2, 0.6))
    for _ in range(3):
        buffer.put(None)
    print(f'{name} завершил работу')


def consumer(condition, buffer):
    name = threading.current_thread().name
    while True:
        with condition:
            while True:
                try:
                    result = buffer.get_nowait()
                    break
                except Empty:
                    print(f'{name} ожидает...')
                    condition.wait()
            if result is None:
                print(f'{name} завершил работу')
                buffer.task_done()
                break

            print(f'{name} извлек {result}')
            buffer.task_done()
            condition.notify()
            time.sleep(random.uniform(0.2, 0.6))


def main():
    condition = Condition()
    buffer = Queue(maxsize=5)
    strings = [str(i) for i in range(1, 11)]
    consumers = []

    t1 = Thread(target=producer, name='[Producer]', args=(condition, buffer, strings))
    for i in range(1, 4):
        t_consumer = Thread(target=consumer, name=f'[Consumer {i}]', args=(condition, buffer))
        consumers.append(t_consumer)

    t1.start()
    for i in consumers:
        i.start()

    t1.join()
    for i in consumers:
        i.join()

    buffer.join()
    print('Все процессы завершены')


if __name__ == '__main__':
    main()
