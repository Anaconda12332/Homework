"""
5
два процесса, бесконечный цикл, каждый печатает что работает
главный процесс ждет 3 секунды и завершает 1 процесс, через еще 3 секунды
завершает второй
"""
from multiprocessing import Process, current_process
import time


def work():
    while True:
        print(f'{current_process().name} работает')
        time.sleep(1)


if __name__ == '__main__':
    t_start = time.time()
    p = Process(target=work)
    p2 = Process(target=work)

    p.start()
    p2.start()

    time.sleep(3)
    if p.is_alive():
        p.terminate()
        print('Процесс 1 завершен')
    time.sleep(3)
    if p2.is_alive():
        p2.terminate()
        print('Процесс 2 завершен')

    t_end = time.time()
    print(f'Процессы отработали {round(t_end - t_start, 3)} секунд')
