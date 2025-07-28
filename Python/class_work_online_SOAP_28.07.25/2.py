import requests
"""
С помощью TVMaze API выгрузите все данные о шоу, где в названии есть слово
"друзья" (friends). На основании полученных данных постройте
Sunburst-диаграмму с иерархией Язык → Жанр → Название.
"""
url = 'https://api.tvmaze.com/search/shows?q=friends'


shows = []

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for show in data:
        shows.append({show['show']['name']: {
                        'name': show['show']['name'],
                        'language': show['show']['language'],
                        'genres': show['show']['genres'],
                        'premiered': show['show']['premiered'],
                        'runtime': show['show']['runtime']
                    }})

    print('Количество шоу:', len(shows))

else:
    print('ошибка', response.status_code)

for i in shows:
    for key, value in i.items():
        print(f'{key}: {value}')
