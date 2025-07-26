import requests
from token_1 import TOKEN

token = TOKEN
names = ['kennethreitz', 'microsoft', 'google']
result = []

for i in names:
    url = f'https://api.github.com/users/{i}/repos'
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for repo in data:
            name = repo['name']
            stargazers_count = repo['stargazers_count']
            result.append({
                'Пользователь': i,
                'name': name,
                'stars': stargazers_count
            })
    else:
        print('Ошибка', response.status_code)

for i in result:
    print(i)
