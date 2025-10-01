"""
Необходимо написать асинхронное приложение, которое:
Загружает данные с нескольких API-эндпоинтов (список URL будет задан).
Делает это конкурентно (параллельно с помощью корутин).
Использует пул соединений для экономии ресурсов.
Устанавливает таймауты на каждый запрос, чтобы избежать зависаний.
Собирает результаты всех успешных запросов в единый список (или файл JSON)
и выводит статистику:
количество успешных ответов;
количество ошибок (например, таймаутов или HTTP-ошибок);
среднее время отклика.

2. Исходные данные
Пример списка тестовых URL (можно использовать публичные API или заглушки):
URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    # … добавьте ещё 10–15 URL для нагрузки
]

3. Требования к реализации
Выберите клиент:
либо aiohttp,
либо httpx в асинхронном режиме.

Настройте пул соединений:
например, ограничьте количество одновременных подключений (5–10).

Настройте таймауты:
общий таймаут на выполнение запроса (например, 5 секунд),
таймаут на подключение (например, 2 секунды).

Реализуйте обработку ошибок:
отлавливайте TimeoutError и ошибки HTTP (4xx, 5xx),
учитывайте их в статистике.
Используйте конкурентное выполнение (asyncio.gather или TaskGroup).

По завершении работы:
сохраните успешные ответы в JSON-файл,
выведите статистику (успехи, ошибки, среднее время отклика).
"""
import asyncio
import json
import aiohttp
import time

time_list = []


def lead_time(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        time_list.append(end - start)
        return result
    return wrapper


def save_json(data):
    with open('pz_from_29.09_aiohttp/result.json', 'w') as f:
        json.dump(data, f, indent=4)


@lead_time
async def fetch_url(session, url):
    try:
        async with asyncio.timeout(3):
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return {'url': url, 'data': data, 'status': 'success'}

    except asyncio.TimeoutError:
        return {'url': url, 'error': 'TimeoutError', 'status': 'error'}
    except aiohttp.ClientResponseError as e:
        return {'url': url, 'error': f'HTTPError: {e.status}', 'status': 'error'}
    except aiohttp.ClientError as e:
        return {'url': url, 'error': f'ClientError: {str(e)}', 'status': 'error'}
    except Exception as e:
        return {'url': url, 'error': f'Unexpected: {str(e)}', 'status': 'error'}


async def main():
    urls = [
        'https://httpbin.org/status/404',
        'https://httpbin.org/anything',
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5",
        "https://jsonplaceholder.typicode.com/posts/6",
        "https://jsonplaceholder.typicode.com/posts/7",
        "https://jsonplaceholder.typicode.com/posts/8",
        "https://jsonplaceholder.typicode.com/posts/9",
        'https://httpbin.org/delay/10',
        'https://httpbin.org/delay/2',
        'https://nonexistent.domain',
        'https://httpbin.org/json'
    ]

    connector = aiohttp.TCPConnector(limit=5)
    timeout = aiohttp.ClientTimeout(total=5, sock_read=3)
    success = []
    errors = []

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        if result['status'] == 'success':
            success.append(result['data'])
        else:
            errors.append(result['error'])

    save_json(success)
    print('Статистика:')
    print('Успехи:', len(success))
    print('Ошибки:', len(urls) - len(success), errors)
    print('Среднее время отклика:', round(sum(time_list) / len(time_list), 3), 'секунд')


asyncio.run(main())
