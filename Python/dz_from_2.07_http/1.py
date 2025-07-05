"""
agify.io
запрашивает ввод имени
get http://api.agify.io?name=<вееденное имя>
получает json ответ
вывод
try except
обработка корректного ввода имени
"""
import requests


name = input("Введите имя: ").capitalize()
while not name:
    print('Ошибка ввода')
    name = input("Введите имя: ").capitalize()

try:
    response = requests.get('http://api.agify.io', params={'name': name})
    data = response.json()
    print(f'Имя: {data["name"]}\nПредпологаемый возраст: {data["age"]}\nИмя встречается {data["count"]} раза')

except Exception as e:
    print(f"[Ошибка]: {e}")
