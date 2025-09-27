import asyncio
from aiohttp import web


list_items = []
lock = asyncio.Lock()


async def say_hello(request):
    return web.json_response({"message": "Добро пожаловать в наш сервис!"})


async def items_get(request):
    async with lock:
        global list_items
        if list_items:
            return web.json_response({"items": list_items})
        else:
            return web.json_response({"items": []})


async def items_post(request):
    data = await request.json()
    item = data.get('name')

    async with lock:
        global list_items
        if item is None:
            return web.json_response({'error': 'Неверный индекс'}, status=400)
        if item not in list_items:
            list_items.append(item)
            return web.json_response({'message': f"Получил: {item}"})
        return web.json_response({'error': f'Элемент {item} уже существует'}, status=400)


async def find_item_id(request):
    try:
        item_id = int(request.match_info['id'])
    except ValueError:
        return web.json_response({"error": "Неверный формат индекса"}, status=400)

    async with lock:
        global list_items
        if 0 <= item_id < len(list_items):
            return web.json_response({'message': f"index {item_id} -> item {list_items[item_id]}"})
        else:
            return web.json_response({"error": f"Элемент с индексом {item_id} не найден"}, status=404)


async def items_delete_id(request):
    try:
        data = int(request.match_info['id'])
    except ValueError:
        return web.json_response({"error": "Неверный формат индекса"}, status=400)

    async with lock:
        global list_items
        if 0 <= data < len(list_items):
            del_item = list_items.pop(data)
            return web.json_response({'message': f"Удалено: {del_item}"})
        else:
            return web.json_response({"error": "Элемент не найден"}, status=404)


app = web.Application()
app.add_routes([
    web.get('/', say_hello),
    web.get('/items', items_get),
    web.post('/items', items_post),
    web.get('/items/{id}', find_item_id),
    web.delete('/delete/{id}', items_delete_id)
])

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
