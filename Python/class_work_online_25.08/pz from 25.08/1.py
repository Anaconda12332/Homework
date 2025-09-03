"""
берёт список чисел [5, 7, -3, 8, 10]
запускает пул процессов для вычисления факториала каждого числа
если число отрицательное - выбрасывается исключение
результаты успешных вычислений собираются в список через callback
ошибки обрабатываются отдельно через error_callback
"""
from multiprocessing import Pool


def factorial(n):
    if n < 0:
        raise ValueError("Факториал не может быть вычислен для отрицательного числа")
    else:
        return 1 if n == 0 else n * factorial(n - 1)


def append_result(list_result):
    def wrapper(result):
        print(f"Факториал получен {result}")
        list_result.append(result)
    return wrapper


def errors(result):
    print('[Ошибка]:', result)


if __name__ == '__main__':
    with Pool(5) as p:
        list_num = [5, 7, -3, 8, 10]
        list_result = []

        for n in list_num:
            p.apply_async(factorial, args=(n,), callback=append_result(list_result), error_callback=errors)
        p.close()
        p.join()
    print('Список фракториалов:', list_result)
