import requests


name = 'octocat'
url = f'https://api.github.com/users/{name}/repos'
headers = {'Acept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for repo in data:
        print(f'- {repo['name']} (⭐ {repo['stargazers_count']})')
else:
    print('Ошибка', response.status_code)
