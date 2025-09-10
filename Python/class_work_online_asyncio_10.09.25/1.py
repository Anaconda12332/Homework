"""
асинхронная система загрузки и обработки данных
корутина-поставщик fetch_data. Имитация asyncio.sleep с разным времен
корутина-обработчик process_data получает реультат загрузки и обрабатывает
его. Подсчет символом
все параллельно, с create_task
gather чтобы дождаться всех задач
"""
import asyncio
import random


async def fetch_data(name):
    print(f'[Производитель {name}] начал работу')
    await asyncio.sleep(random.uniform(0.5, 0.7))
    return f'Data {name * random.randint(1, 100)}'


async def process_data(name):
    print(f'[Обработчик {name}] начал работу')
    result = await fetch_data(name)
    print(f'[Обработчик {name}]: Полученны данные: {result}.', end=' ')
    print(f'Колличесто символов: {len(result)}')


async def main():
    tasks = [asyncio.create_task(process_data(i)) for i in range(1, 5)]
    await asyncio.gather(*tasks)
    print('Задачи завершены')

asyncio.run(main())
