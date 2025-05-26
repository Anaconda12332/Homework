# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.
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
def prime_numbers(start, stop):
    prime = []
    for i in range(start, stop+1):
        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a += 1
        if a <= 2:
            prime.append(i) if i != 1 else None
    return prime


prime_numbers(1, 50)
