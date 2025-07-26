import requests
from token_1 import TOKEN

token = TOKEN
url = 'https://api.github.com/users/octocat'
headers = {"Authorization": f"token {token}"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print('Логин: ', data['login'])
    print('Публичное имя: ', data['name'])
    print('Количество публичных репозиториев: ', data['public_repos'])
    print("Количество подписчиков: ", data['followers'])
else:
    print('Ошибка', response.status_code)
