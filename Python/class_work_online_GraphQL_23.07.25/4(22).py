import requests
from token_1 import TOKEN

url_google_repos = 'https://api.github.com/users/google/repos'
repos = []
page = 1

token = TOKEN
headers = {"Authorization": f"token {token}"}

while True:
    response = requests.get(
        url=url_google_repos,
        headers=headers,
        params={'per_page': 100, 'page': page}
    )
    if response.status_code == 200:
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    else:
        print('ошибка', response.status_code)

print(f'Количество репозиториев: {len(repos)}')
