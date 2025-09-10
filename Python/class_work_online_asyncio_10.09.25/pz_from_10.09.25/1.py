"""
Часть 1. Последовательное выполнение (await)
Напишите функцию async def do_work(name, delay), которая:
печатает сообщение о начале работы;
делает await asyncio.sleep(delay);
печатает сообщение о завершении;
возвращает имя задачи.
Напишите функцию async def sequential_demo(), которая вызывает do_work("A", 2)
и do_work("B", 1) последовательно с помощью await.
Замерьте общее время выполнения этой функции (используйте time.perf_counter).

Вопрос:
Сколько времени заняла программа?
    -Программа заняла 3.020 секунды.
Почему выполнение заняло именно столько времени?
    -Потому что корутины выполнялись последовательно с задержкой 2+1 секунды
"""
import asyncio
import time


async def do_work(name, delay):
    print(f"Начало работы {name}")
    await asyncio.sleep(delay)
    print(f'Завершение работы {name}')
    return name


async def sequential_demo():
    start = time.perf_counter()
    for name, delay in [("A", 2), ("B", 1)]:
        await do_work(name, delay)
    end = time.perf_counter()
    print(f'Общее время выполнения: {end - start:.3f} секунды')


async def main():
    await sequential_demo()

asyncio.run(main())
