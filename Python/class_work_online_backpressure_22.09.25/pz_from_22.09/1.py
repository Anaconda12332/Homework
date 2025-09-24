"""
асинхронная обработка данных с управлением backpressure

производитель-потребитель

производители генерируют "данные-1"... со случайной задержкой
    если очередь заполнена, то потребитель ждет

потребители извлекают данные из очереди и обрабатывают их за случайное время
    lock для общего счетчика обработанных данных

event для сигнализации об окончании заполнения очереди производителями
потребители после обработки всех элементов очереди завершатся

condition при освобождении места в очереди уведомлять ожидающих потребителей

итоговая статистика
"""
import asyncio
import random

lock = asyncio.Lock()
event = asyncio.Event()
condition = asyncio.Condition()
counter = 0


async def producer(queue, name):
    for i in range(1, 11):
        async with condition:
            while queue.qsize() == queue.maxsize:
                print(f'[Производитель {name}]: Очередь заполнена')
                await condition.wait()
            item = f"данные-{i}"
            await queue.put(item)
            print(f'[Производитель {name}]: Положил в очередь:', item)
            condition.notify()
        await asyncio.sleep(random.uniform(0.5, 1.5))
    event.set()
    print(f'[Производитель {name}]: Завершил работу')


async def consumer(queue, name):
    global counter
    while True:
        async with condition:
            if queue.qsize() == 0 and event.is_set():
                print(f'[Потребитель {name}]: Завершение работы')
                break
            while queue.qsize() == 0:
                print(f'[Потребитель {name}]: Очередь пуста')
                await condition.wait()
            item = await queue.get()
            async with lock:
                counter += 1
            print(f'[Потребитель {name}]: Забрал из очереди:', item)
            queue.task_done()
            condition.notify()
        await asyncio.sleep(random.uniform(0.5, 1.5))


async def main():
    queue = asyncio.Queue(maxsize=5)

    producer_task = [asyncio.create_task(producer(queue, i)) for i in range(1, 4)]
    consumer_task = [asyncio.create_task(consumer(queue, i)) for i in range(1, 3)]

    await asyncio.gather(*producer_task)
    await queue.join()

    await asyncio.gather(*consumer_task)

    print('Всего обработано данных:', counter)

asyncio.run(main())
