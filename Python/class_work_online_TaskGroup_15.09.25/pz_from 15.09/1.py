"""
Вы создаёте программу, которая:
Загружает данные с нескольких URL (некоторые URL корректные, некоторые
вызывают ошибки).
Параллельно выполняет вычисления (например, деление чисел, где могут
возникнуть ошибки деления на ноль).
Использует TaskGroup для управления всеми задачами.
Корректно собирает все ошибки в ExceptionGroup.
Гарантирует, что при падении одной задачи остальные корректно отменяются, а
ресурсы освобождаются.
urls = [
    "https://httpbin.org/get",        # корректный
    "https://httpbin.org/status/404", # вызовет ошибку 404
    "https://httpbin.org/delay/5",    # имитация долгой загрузки
]


Создайте функцию async fetch_url(session, url), которая:
Загружает страницу с помощью aiohttp.
Если URL возвращает ошибку, она выбрасывается наружу (не ловим внутри).
В блоке finally закрываем соединение (или выводим сообщение о завершении).

Создайте функцию async compute_division(a, b), которая:
Выполняет a / b.
Если b == 0, выбрасывается ZeroDivisionError.
Использует await asyncio.sleep(...) для имитации долгих вычислений.
В блоке finally печатает, что вычисление завершено.

В main() используйте asyncio.TaskGroup для запуска:
Задач на загрузку URL.
Задач на вычисления (например, деление нескольких чисел,
где есть деление на ноль).
Оберните TaskGroup в блок try/except* для обработки ошибок:
except* aiohttp.ClientError → вывод ошибок HTTP.
except* ZeroDivisionError → вывод ошибок деления на ноль.
except* asyncio.CancelledError → вывод, что оставшиеся задачи были отменены.

Убедитесь, что:
Если одна задача падает, остальные отменяются.
В finally каждой задачи всегда выполняется очистка/закрытие ресурсов.
Все ошибки собираются и выводятся после завершения TaskGroup.
"""
import asyncio
import aiohttp


async def fetch_url(session, url):
    try:
        print('Загружается страница', url)

        async with session.get(url) as response:
            response.raise_for_status()
            print('Загружена страница', url)
    finally:
        print('Закончена обработка', url)


async def compute_division(a, b):
    try:
        if b == 0:
            await asyncio.sleep(1)
            raise ZeroDivisionError('Деление на ноль')
        else:
            await asyncio.sleep(1)
            return a / b
    finally:
        print(f'Вычисление {a} / {b} завершено.')


async def main():
    nums = [
        (10, 2),
        (10, 0),
        (5, 2),
        (5, 0),
    ]
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/5",
    ]
    async with aiohttp.ClientSession() as session:
        try:
            async with asyncio.TaskGroup() as tg:
                for url in urls:
                    tg.create_task(fetch_url(session, url))
                for a, b in nums:
                    tg.create_task(compute_division(a, b))

        except* aiohttp.ClientError as e:
            for exc in e.exceptions:
                print('[Ошибка HTTP]:', exc)
        except* ZeroDivisionError as e:
            for exc in e.exceptions:
                print('[Ошибка]:', exc)
        except* asyncio.CancelledError:
            print('Оставшиеся задачи были отменены')

asyncio.run(main())
