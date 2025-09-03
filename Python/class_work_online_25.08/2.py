"""
производитель, кладет в JoinableQueue список чисел
потребитель, берет из JoinableQueue список чисел, квадрат, выводит результат
после обработки каждой задачи потребитель вызывает task_done()
join()
"""
from multiprocessing import Process, JoinableQueue


def consumer(q):
    while True:
        num = q.get()
        if num == 'END':
            print('Consumer: END')
            q.task_done()
            break
        print(f'Consumer: {num ** 2}')
        q.task_done()


def producer(q):
    for i in range(10):
        q.put(i)
        print(f'Producer: {i}')
    q.put('END')


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    q.join()

    p1.join()
    p2.join()
