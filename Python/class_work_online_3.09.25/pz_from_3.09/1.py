"""
работа с общим складом
ограниченное количество ресурсов 5 едениц
поток = сотрудник, пытается взять ресурс, поработать с ним и вернуть
его обратно
нужна синхронизация
lock Для количества выполненных операция
rlock Для функции, которая вызывает внутри себя другую функцию и
обе их используют одну и ту же блокировку
semaphore Ограничить число потоков
bounded semaphore поменять на
thread
вывести сообщение с именем потока и номером операции
взять ресурс, подождать
вернуть ресурс, обновить общий счетчик
"""
from threading import Thread, Lock, RLock, BoundedSemaphore, current_thread
import time


def worker(resources):
    with sema:
        thread_name = current_thread().name
        print(f'[{thread_name}]: начал работу')
        with lock:
            global count
            count += 1
            print(f'[{thread_name}]: номер операции {count}')

            num = resources.pop(0)
            result = recursive_function(num)
            print(f'[{thread_name}]: результат вычислений:', result)
            if len(resources) < MAXSIZE:
                resources.append(result)
                time.sleep(0.5)
            else:
                print('Хранилище переполнено')


def recursive_function(nums, count=1):
    with rlock:
        result = nums * 2
        if count == 5:
            return result
        else:
            return recursive_function(result, count + 1)


sema = BoundedSemaphore(2)
lock = Lock()
rlock = RLock()
warehouse_resources = [1, 2, 3, 4, 5]
MAXSIZE = 5
count = 0

threads = []

for i in range(1, 6):
    t = Thread(target=worker, name=f'Процесс {i}', args=(warehouse_resources,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('\nВсе потоки завершили работу')
print(f'Результат: {warehouse_resources}\nКоличество операций: {count}')
