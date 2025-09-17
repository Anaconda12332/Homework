"""
Вам нужно реализовать асинхронную программу, которая:
Загружает содержимое с нескольких URL-адресов (например,
страницы https://httpbin.org/delay/X, где X — это задержка).
Одновременно выполняет не более трёх запросов. Для ограничения
используйте asyncio.Semaphore.

Для каждого успешно завершённого запроса выводит сообщение вида:
Успешно загружено: <url>, длина ответа = <число символов>

Если при загрузке возникает ошибка (aiohttp.ClientError или таймаут), нужно
обработать её и вывести сообщение:
Ошибка при загрузке: <url>, причина: <текст ошибки>

После завершения всех запросов программа должна вывести общее количество
успешно обработанных URL и количество ошибок.
"""
import asyncio
from asyncio import Semaphore
import aiohttp


async def fetch(session, url, sema):
    try:
        async with sema:
            print(f'[Fetch] Начало загрузки: {url}')
            async with asyncio.timeout(10):
                async with session.get(url) as response:
                    response.raise_for_status()
                    result = await response.text()
                    print(f'[Fetch result] Успешно загружено: {url}, длина ответа = {len(result)}')
    finally:
        print('[Fetch finally] Завершение загрузки. Освобождение ресурсов...')


async def main():
    urls = [f'https://httpbin.org/delay/{i}' for i in range(1, 6)]
    count_errors = 0
    count_completed = 0
    sema = Semaphore(3)

    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.timeout(20):
                async with asyncio.TaskGroup() as tg:
                    tasks = [tg.create_task(fetch(session, url, sema)) for url in urls]

    except* Exception as e:
        for exs in e.exceptions:
            count_errors += 1
            print(f'[Ошибка]: {exs.__class__.__name__}')

    finally:
        print('\n[Finally] Ресурсы освобождены.')
        for task in tasks:
            if task.done() and not task.cancelled() and not task.exception():
                count_completed += 1
        print(f'[Finally] Общее количество успешно обработанных URL: {count_completed}')
        print(f'[Finally] Количество ошибок: {count_errors}')

asyncio.run(main())
