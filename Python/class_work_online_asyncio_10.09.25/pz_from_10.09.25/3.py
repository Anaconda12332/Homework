"""Часть 3. Использование asyncio.gather
Напишите функцию async def gather_demo(), которая запускает do_work("A", 2)
и do_work("B", 1) с помощью asyncio.gather.
Замерьте время выполнения и сравните его с предыдущими частями.

Вопрос:
Чем gather отличается от ручного создания задач?
    -он автоматизирует процесс создания задач и ждет их завершения, результат
    выпрлнения вовзращается в виде списка
В каких случаях gather удобнее?
    -когда нужно выполнить несколько однотипных задач одновременно
"""
import asyncio
import time


async def do_work(name, delay):
    print(f"Начало работы {name}")
    await asyncio.sleep(delay)
    print(f'Завершение работы {name}')
    return name


async def gather_demo():
    start = time.perf_counter()
    data = [("A", 2), ("B", 1)]

    tasks = [asyncio.create_task(do_work(*n)) for n in data]
    print("Задачи запущены")
    await asyncio.gather(*tasks)

    end = time.perf_counter()
    print(f'Общее время выполнения: {end - start:.3f} секунды')


asyncio.run(gather_demo())
