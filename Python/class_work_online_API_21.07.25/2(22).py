import requests
from token_1 import TOKEN

token = TOKEN
name = 'octocat'
url = f'https://api.github.com/users/{name}/repos'
headers = {"Authorization": f"token {token}"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for repo in data:
        print(f'- {repo['name']} (⭐ {repo['stargazers_count']})')
else:
    print('Ошибка', response.status_code)
