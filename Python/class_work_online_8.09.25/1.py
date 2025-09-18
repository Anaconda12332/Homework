"""
производитель-потребитель
общий список buffer, хранит максимум 5 элементов
производитель добавляет в список числа от 1 до 20
    если буфер заполнен, производитель ждет
    после добавления числа производитель уведомляет потребителя

потребитель извлекает элементы из буфера
    если буфер пуст, потребитель ждет до тех пор, пока не появится новый
    элемент (производитель добавляет)
    после извлечения элемента потребитель уведомляет производителя

threading.current_thread().name для отладки
"""
from threading import Thread, Condition
import threading
import random
from queue import Empty, Queue
import time


def producer(condition, buffer):
    for i in range(1, 21):
        with condition:
            while buffer.full():
                print('Буфер полон, ожидание...')
                condition.wait()
            buffer.put(i)
            print(f'Производитель {threading.current_thread().name} добавил {i} в буфер')
            condition.notify()
            time.sleep(random.uniform(0.2, 0.6))
    print('Производитель завершил работу')


def consumer(condition, buffer):
    for _ in range(1, 21):
        with condition:
            while True:
                try:
                    result = buffer.get_nowait()
                    break
                except Empty:
                    print(f'Потребитель {threading.current_thread().name} ожидает...')
                    condition.wait()

            print(f'Потребитель {threading.current_thread().name} извлек {result}')
            buffer.task_done()
            condition.notify()
            time.sleep(random.uniform(0.2, 0.6))

    print('Потребитель завершил работу')


def main():
    condition = Condition()
    buffer = Queue(maxsize=5)
    t1 = Thread(target=producer, name='[Producer]', args=(condition, buffer))
    t2 = Thread(target=consumer, name='[Consumer]', args=(condition, buffer))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    buffer.join()
    print('Все процессы завершены')


if __name__ == '__main__':
    main()




# buffer = []
# MAX_SIZE = 5

# condition = Condition()

# def producer():
#     for i in range(1, 21):
#         with condition:
#             while len(buffer) == MAX_SIZE:
#                 print(f"Производитель [{threading.current_thread().name}] ожидает")
#                 condition.wait()

#             buffer.append(i)
#             print(f"Производитель [{threading.current_thread().name}] добавил элемент {i} в {buffer}")
#             condition.notify()

#         time.sleep(random.uniform(0.2, 0.6))

# def consumer():
#     for _ in range(20):
#         with condition:
#             while not buffer:
#                 print(f"Потребитель [{threading.current_thread().name}] ожидает")
#                 condition.wait()

#             item = buffer.pop(0)
#             print(f"Потребитель [{threading.current_thread().name}] извлек из {buffer} элемент {item}")
#             condition.notify()

#         time.sleep(random.uniform(0.3, 0.7))

# def main():
#     t1 = Thread(target=producer, name="Producer")
#     t2 = Thread(target=consumer, name="Consumer")

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print("Все потоки завершили работу")

# if __name__ == "__main__":
#     main()
