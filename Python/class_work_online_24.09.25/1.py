"""
Вам нужно написать программу, которая будет скачивать содержимое нескольких
веб-страниц и сравнивать скорость выполнения при использовании:
Синхронного клиента requests.
Асинхронного клиента aiohttp.
Асинхронного клиента httpx.
Список адресов возьмите следующий:

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]

Реализовать три функции:
fetch_requests(urls) — выполняет загрузку всех страниц синхронно
через requests.
fetch_aiohttp(urls) — выполняет загрузку всех страниц параллельно
через aiohttp.
fetch_httpx(urls) — выполняет загрузку всех страниц параллельно через httpx.

Для каждой функции измерить время выполнения (time.time()
или asyncio.get_event_loop().time()).
Сравнить результаты: какой способ оказался самым быстрым.

Обработать возможные ошибки:
таймаут,
сетевые ошибки (ClientError у aiohttp, httpx.RequestError у httpx).

Итоговый вывод должен содержать таблицу или список
"""
import time
import requests
import asyncio
import aiohttp
import httpx


def fetch_requests(url):
    try:
        response = requests.get(url)
        print(f'[fetch_requests]: {url}: Длинна ответа: {len(response.text)}')
    except Exception as e:
        print('Ошибка', e)


async def fetch_aiohttp(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            print(f'[fetch_aiohttp]: {url}: Длинна ответа: {len(text)}')
    except aiohttp.ClientError as e:
        print('Ошибка:', e)


async def fetch_httpx(client, url):
    try:
        response = await client.get(url)
        print(f'[fetch_httpx]: {url}: Длинна ответа: {len(response.text)}')
    except httpx.RequestError as e:
        print('Ошибка:', e)


async def manager(urls):
    start_time = time.time()
    for url in urls:
        fetch_requests(url)
    end_time = time.time()

    start_time2 = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_aiohttp(session, url)) for url in urls]
        await asyncio.gather(*tasks)
    end_time2 = time.time()

    timeout = httpx.Timeout(10.0, connect=10.0)
    start_time3 = time.time()
    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks2 = [fetch_httpx(client, url) for url in urls]
        await asyncio.gather(*tasks2)
    end_time3 = time.time()

    result_1 = end_time - start_time
    result_2 = end_time2 - start_time2
    result_3 = end_time3 - start_time3
    return result_1, result_2, result_3


async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    result_1, result_2, result_3 = await manager(urls)
    print(f"[fetch_requests]: {result_1:.2f} секунд")
    print(f"[fetch_aiohttp]: {result_2:.2f} секунд")
    print(f"[fetch_httpx]: {result_3:.2f} секунд")

asyncio.run(main())


"""
import requests
#import aiohttp
#import httpx
#import asyncio
import time

def fetch_requests(urls):
    start_time = time.time()
    results = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            text = response.text
            results.append(len(text))
            print(f"requests Загружено {url}: {len(text)}")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса {url}: {e}")
    end_time = time.time()
    return end_time - start_time, results

async def fetch_one_aiohttp(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            text = await response.text()
            print(f"aiohttp Загружено {url}: {len(text)}")
            return len(text)
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса {url}: {e}")
    except asyncio.TimeoutError:
        print(f"Таймаут для {url}")

async def fetch_aiohttp(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one_aiohttp(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        return end_time - start_time, results

async def fetch_one_httpx(client, url):
    try:
        response = await client.get(url, timeout=10)
        response.raise_for_status()
        text = response.text
        print(f"httpx Загружено {url}: {len(text)}")
        return len(text)

    except httpx.RequestError as e:
        print(f"Ошибка запроса {url}: {e}")
    except asyncio.TimeoutError:
        print(f"Таймаут для {url}")
    except httpx.HTTPStatusError as e:
        print(f"httpx ошибка при загрузке {url}: {e}")

async def fetch_httpx(urls):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one_httpx(client, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    end_time = time.time()
    return end_time - start_time, results

async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    time_requests, _ = fetch_requests(urls)
    time_aiohttp, _ = await fetch_aiohttp(urls)
    time_httpx, _ = await fetch_httpx(urls)

    print(f"Время выполнения requests: {time_requests:.2f} секунд")
    print(f"Время выполнения aiohttp: {time_aiohttp:.2f} секунд")
    print(f"Время выполнения httpx: {time_httpx:.2f} секунд")
"""
