"""
2
список из 5 чисел, два процесса
первый вычисляет квадраты чисел и печатает их
второй вычисляет кубы чисел и печатает их
"""
from multiprocessing import Process


def square(numb):
    print('начало процесса вычисления квадрата из {0}'.format(numb))
    print(numb ** 2)


def cube(numb):
    print('начало процесса вычисления кубов из {0}'.format(numb))
    print(numb ** 3)


if __name__ == '__main__':
    numbs = [1, 2, 3, 4, 5]
    process = []
    for numb in numbs:
        p1 = Process(target=square, args=(numb,))
        p2 = Process(target=cube, args=(numb,))
        p1.start()
        p2.start()
        process.append(p1)
        process.append(p2)

    for p in process:
        p1.join()
