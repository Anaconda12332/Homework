import requests


url = f'https://api.github.com/users'
headers = {'Acept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Ошибка', response.status_code)
