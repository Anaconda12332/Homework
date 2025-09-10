"""Часть 4. задание
Добавьте третью задачу do_work("C", 3).
Сравните выполнение при:
последовательном await,
ручном create_task,
использовании gather.
Постройте таблицу:

Метод	Общее время выполнения	Порядок завершения задач
await
create_task
gather

Часть 5. Вопросы
Почему await в последовательном варианте не дал конкурентности?
    -Потому что await do_work(name, delay) запускает только одну корутину за
    раз и ждет ее полного выполнения, поскольку в очереди еще не существует
    других задач, на которые можно переключиться.
В чём разница между create_task и gather?
    -create_task - создает задачу вручную и добавляет ее в event loop,
    явлется более гибким, а gather - запускает пул однотипных задач
    и ждет их выполнения сразу.
Почему asyncio.run обычно вызывается только один раз в программе?
    -потому что asyncio.run создает цикл событий, который контролирует
    выполнение всех переданных задач и второй просто не нужен.
Как вы объясните словами: «где именно происходит асинхронность»?
    -асинхронность происходит в момент вызова await в корутине.
"""
import asyncio
import time
from prettytable import PrettyTable


async def do_work(name, delay):
    print(f"Начало работы {name}")
    await asyncio.sleep(delay)
    print(f'Завершение работы {name}')
    return name


async def sequential_demo():
    start = time.perf_counter()
    result_name = []

    print("Задачи запущены")
    for name, delay in [("A", 2), ("B", 1), ("C", 3)]:
        result_name.append(await do_work(name, delay))

    end = time.perf_counter()
    result_time = end - start
    print(f'Общее время выполнения: {result_time:.3f} секунды\n')
    return result_time, result_name


async def tasks_demo():
    start = time.perf_counter()
    result_name = []

    task1 = asyncio.create_task(do_work("A", 2))
    task2 = asyncio.create_task(do_work("B", 1))
    task3 = asyncio.create_task(do_work("C", 3))

    print("Задачи запущены")
    for completed_task in asyncio.as_completed([task1, task2, task3]):
        result = await completed_task
        result_name.append(result)

    end = time.perf_counter()
    result_time = end - start
    print(f'Общее время выполнения: {result_time:.3f} секунды\n')
    return result_time, result_name


async def gather_demo():
    start = time.perf_counter()
    data = [("A", 2), ("B", 1), ("C", 3)]

    tasks = [asyncio.create_task(do_work(*n)) for n in data]
    print("Задачи запущены")

    result_name = await asyncio.gather(*tasks)

    end = time.perf_counter()
    result_time = end - start
    print(f'Общее время выполнения: {result_time:.3f} секунды\n')
    return result_time, result_name


async def main():
    result_time, result_name = await sequential_demo()
    result_time2, result_name2 = await tasks_demo()
    result_time3, result_name3 = await gather_demo()

    table = PrettyTable()

    table.field_names = ["Метод", "Общее время выполнения", "Порядок завершения задач"]

    table.add_row(["await", f"{result_time:.3f}", f"{result_name[0]} -> {result_name[1]} -> {result_name[2]}"]),
    table.add_row(['create_task', f"{result_time2:.3f}", f"{result_name2[0]} -> {result_name2[1]} -> {result_name[2]}"]),
    table.add_row(['gather', f"{result_time3:.3f}", f"{result_name3[1]} -> {result_name3[0]} -> {result_name[2]}"]),

    print('Статистика выполнения:')
    print(table)

asyncio.run(main())
