"""
4
запускает три процесса, каждый из которых проверяет, есть ли простые числа в
своем диапазоне
1 от 2 до 10000
2 от 10001 до 20000
3 от 20001 до 30000
каждый процесс выводит количество найденных простых чисел
"""
from multiprocessing import Process, current_process


def prost(num_one, num_two):
    count = 0
    for i in range(num_one, num_two + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                count += 1
    print(f'процесс {current_process().name} нашел {count} простых числа')


if __name__ == '__main__':
    ranges = [
        (2, 10000),
        (10001, 20000),
        (20001, 30000)
    ]
    process = []
    for i, j in enumerate(ranges, start=1):
        p = Process(target=prost, args=j, name=str(i))
        process.append(p)
        p.start()
        print(f'процесс {i} запущен')

    for p in process:
        p.join()
