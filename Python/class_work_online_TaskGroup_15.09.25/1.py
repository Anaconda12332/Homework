"""
Вы — разработчик сервиса, который должен параллельно выполнять несколько сетевых и вычислительных задач. 
Вам нужно:

Создать асинхронные функции:
fetch_url(url) — делает HTTP-запрос к указанному адресу (через aiohttp). 
Если сервер возвращает ошибку (например, 404), это должно приводить к исключению.
compute_division(a, b) — выполняет деление a / b с искусственной задержкой (asyncio.sleep). 
Если b == 0, возникает ZeroDivisionError.

В функции main:
Создайте список URL, в котором будут как корректные сайты (например, https://httpbin.org/get), 
так и некорректные (например, https://httpbin.org/status/404, https://nonexistent.domain).
Запустите параллельно несколько задач: загрузку страниц (fetch_url) 
и несколько вычислений (compute_division) с разными параметрами.
Используйте TaskGroup для управления задачами.

Реализуйте обработку ошибок:
Если при загрузке страниц произойдёт ошибка, её нужно поймать с помощью except* aiohttp.ClientError.
Если при делении произойдёт ошибка, её нужно поймать с помощью except* ZeroDivisionError.
Для каждой пойманной ошибки выведите сообщение с её описанием.
Убедитесь, что при падении нескольких задач вы видите все ошибки, а не только первую.
"""
import asyncio
import aiohttp


async def fetch_url(sessoin, url):
    async with sessoin.get(url) as response:
        response.raise_for_status()
        return response.text()


async def compute_division(a, b):
    await asyncio.sleep(1)
    return a / b


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://nonexistent.domain",
    ]

    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.TaskGroup() as tg:
                tasks1 = [tg.create_task(fetch_url(session, url)) for url in urls]
                tasks2 = [tg.create_task(compute_division(10, i)) for i in range(4)]
    
    except* aiohttp.ClientError as e:
        print(f"Ошибка при загрузке страницы: {e}")

    except* ZeroDivisionError as e:
        print(f"Ошибка при делении: {e}")
    else:
        print('Все задачи выполнены успешно')

asyncio.run(main())
