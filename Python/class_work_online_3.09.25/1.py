"""
создать список заказов (числа от 1 до 10)
для каждого заказа создать поток, который:
    - выводит сообщение
    - показывает имя потока

после запуска всех потоков
    - вывести количество активных потоков
    - вывести список всех активных потоков

дождаться завершения всех потоков
снова показать количество активных потоков
"""
from threading import Thread
import threading
import time


def order_processing(order_number):
    time.sleep(0.5)
    print(f'[{t.name}]: Заказ с номером {order_number}')


threads = []
order_list = [i for i in range(1, 11)]

for order in order_list:
    t = Thread(target=order_processing, args=(order,))
    t.start()
    threads.append(t)

print(f'Количество активных потоков: {threading.active_count()}')
print(f'Список активных потоков: \n{threading.enumerate()}\n')

for t in threads:
    t.join()
print(f'Количество активных потоков: {threading.active_count()}')
