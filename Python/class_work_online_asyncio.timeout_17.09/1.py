"""
Загружать данные с нескольких URL параллельно.
Выполнять вычисления (например, деление чисел, где может
возникнуть ZeroDivisionError).
Использовать локальные таймауты для каждой подзадачи (например, 3 секунды).
Использовать глобальный таймаут для всей группы задач (например, 10 секунд).
Обрабатывать ошибки через ExceptionGroup:
aiohttp.ClientError для сетевых ошибок.
ZeroDivisionError для вычислений.
asyncio.TimeoutError для превышения таймаута подзадачи.
Гарантировать, что после отмены задач выполняется finally, чтобы закрыть
соединения или завершить вычисления.
"""
import asyncio
import aiohttp


async def worker(session, url):
    try:
        async with asyncio.timeout(3):
            print('[Worker] Загрузка:', url)
            async with session.get(url) as response:
                response.raise_for_status()
                print('[Worker] Загружен:', url,)
                return await response.text()

    finally:
        print('[Finally] Ресурсы освобождены:', url)


async def division(a, b):
    try:
        async with asyncio.timeout(3):
            result = a / b
            print(f'[Division] Выполнение деления {a} / {b} с результатом {result}')
            return result

    finally:
        print(f'[Finally] Деление {a} / {b} завершено')


async def main():
    urls = [
        'https://example.com',
        "https://httpbin.org/delay/5",
        "https://httpbin.org/delay/2",
    ]
    numbers = [
        (1, 2),
        (3, 0),
        (4, 5),
        (6, 0),
    ]

    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.timeout(10):
                async with asyncio.TaskGroup() as tg:
                    for url in urls:
                        tg.create_task(worker(session, url))
                    for a, b in numbers:
                        tg.create_task(division(a, b))

    except* aiohttp.ClientError as e:
        for exs in e.exceptions:
            print('[Ошибка]:', exs)

    except* ZeroDivisionError as e:
        for exs in e.exceptions:
            print('[Ошибка]:', exs)

    except* asyncio.TimeoutError as e:
        for exs in e.exceptions:
            print(f"[Ошибка]: {exs.__class__.__name__}")

    finally:
        print('[Finally] Выполнение закончено. Все ресурсы освобождены.')

asyncio.run(main())
