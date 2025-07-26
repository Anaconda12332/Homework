import requests
"""
Составьте GraphQL-запрос, который по коду страны возвращает:

Название страны
Столицу
Валюту
Список языков
Выведите на экран полученные данные.
"""

upl = 'https://countries.trevorblades.com/'

code = 'RU'
qerry = f'''
{{
    country(code: "{code}") {{
        name
        capital
        currency
        languages {{
            name
        }}
    }}
}}
'''
lang = []

response = requests.post(upl, json={'query': qerry})
if response.status_code == 200:
    data = response.json()
    data = data['data']['country']
    print(data)

else:
    print('ошибка', response.status_code)
