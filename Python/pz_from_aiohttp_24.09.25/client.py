import asyncio
import aiohttp


async def say_hello(session):
    async with session.get('http://localhost:8080/') as response:
        mess = await response.json()
        print(mess['message'])
        await asyncio.sleep(0.5)


async def items_get(session):
    async with session.get('http://localhost:8080/items') as response:
        print(await response.json())


async def items_post(session):
    for i in range(1, 4):
        data = {'name': f'{i}'}
        async with session.post('http://localhost:8080/items', json=data) as response:       
            print(await response.json())


async def items_id(session):
    for i in range(4):
        async with session.get(f'http://localhost:8080/items/{i}') as response:
            print(await response.json())


async def items_delete(session):
    async with session.delete(f'http://localhost:8080/delete/{0}') as response:
        print(await response.json())


async def main():
    async with aiohttp.ClientSession() as session:
        await say_hello(session)
        await items_post(session)
        await items_get(session)
        await items_id(session)
        await items_delete(session)
    print('Клиент завершил работу')

asyncio.run(main())
