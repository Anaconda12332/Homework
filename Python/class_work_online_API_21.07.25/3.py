import requests


names = ['kennethreitz', 'microsoft', 'google']
result = []

for i in names:
    url = f'https://api.github.com/users/{i}/repos'
    headers = {'Acept': 'application/vnd.github.v3+json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for repo in data:
            name = repo['name']
            stargazers_count = repo['stargazers_count']
            result.append({
                'Пользователь': i,
                'name': name,
                'star': stargazers_count
            })
    else:
        print('Ошибка', response.status_code)

for i in result:
    print(i)
