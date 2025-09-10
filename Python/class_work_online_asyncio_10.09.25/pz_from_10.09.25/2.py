"""Часть 2. Запуск через create_task
Напишите функцию async def tasks_demo(), в которой:
создайте две задачи task1 и task2 через asyncio.create_task;
сразу после запуска выведите сообщение «Задачи запущены»;
дождитесь завершения обеих задач через await task1 и await task2.
Замерьте общее время выполнения.

Вопрос:
Чем отличается вывод программы от последовательного запуска?
    -Вывод становится непоследовательным, поскольку задачи запускаются
    параллельно.
Почему общее время меньше?
    -Потому что задачи выполняются параллельно и моменты простоя уменьшаются.
"""
import asyncio
import time


async def do_work(name, delay):
    print(f"Начало работы {name}")
    await asyncio.sleep(delay)
    print(f'Завершение работы {name}')
    return name


async def tasks_demo():
    start = time.perf_counter()

    task1 = asyncio.create_task(do_work("A", 2))
    task2 = asyncio.create_task(do_work("B", 1))

    print("Задачи запущены")
    await task1
    await task2
    end = time.perf_counter()

    print(f'Общее время выполнения: {end - start:.3f} секунды')

asyncio.run(tasks_demo())
