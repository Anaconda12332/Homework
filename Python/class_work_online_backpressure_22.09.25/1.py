"""
асинхронная обработка данных через очередь

producer consumer
2-3 производителя генерируют "данные-1"...
кладут в очередь с задержкой

потребители извлекают и обрабатывают данные с задержкой

очередь maxsize=5

join
task_done
cancel

итоговая статистика
"""
import asyncio


async def producer(queue, name):
    all_tasks = 0
    for i in range(1, 11):
        item = f"данные-{i}"
        await queue.put(item)
        all_tasks += 1
        print(f'[Производитель {name}] положил в очередь:', item)
        await asyncio.sleep(0.5)
    return all_tasks


async def consumer(queue, name):
    while True:
        item = await queue.get()
        print(f'[Потребитель {name}] забрал из очереди:', item)
        await asyncio.sleep(1)
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=5)
    producer_task = [asyncio.create_task(producer(queue, (i))) for i in range(1, 4)]
    consumer_task = [asyncio.create_task(consumer(queue, (i))) for i in range(1,3)]

    result = await asyncio.gather(*producer_task)
    await queue.join()

    for i in consumer_task:
        i.cancel()

    print('Всего обработано данных:', sum(result))

asyncio.run(main())
