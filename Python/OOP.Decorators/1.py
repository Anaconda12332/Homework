# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.
# 2, 3, 5, 7, 11,
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        times = stop - start
        print('Список простых чисел:\n', *result)
        print(f'Для выполнения функции потребовалось: {times:.10f} секунд!')
        return result
    return wrapper


@decorator
def prime_numbers():
    prime = []
    for i in range(2, 1001):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count <= 2:
            prime.append(i)
    return prime


prime_numbers()
