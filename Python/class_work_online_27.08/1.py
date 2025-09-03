"""
общий счетчик и массив результатов
3 процесса, обрабатывающиъ часть чисел
Array - хранит квадраты чисел
Value - хранит общее количество операций/количество обработанных чисел
Lock
"""
from multiprocessing import Process, Array, Value, Lock


def worker(numbers, result_array, counter, lock, start_index):
    for i, n in enumerate(numbers):
        with lock:
            result_array[start_index + i] = n ** 2
            counter.value += 1


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lock = Lock()
    result_array = Array('i', len(numbers))
    counter = Value('i', 0)

    p1 = Process(target=worker, args=(numbers[:3], result_array, counter, lock, 0))
    p2 = Process(target=worker, args=(numbers[3:6], result_array, counter, lock, 3))
    p3 = Process(target=worker, args=(numbers[6:], result_array, counter, lock, 6))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('Масиив:', result_array[:])
    print('Общее количество операций:', counter.value)
