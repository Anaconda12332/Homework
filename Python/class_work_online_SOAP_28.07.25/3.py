"""
С помощью TVMaze API выгрузите данные о всех эпизодах сериала
"Сверхъестественное", который выходил с 2005 по 2020 гг.
Найдите серии с минимальным и максимальным средними рейтингами,
а также постройте столбчатую диаграмму со средними рейтингами каждого сезона.
Проанализируйте полученный график и сделайте выводы.
"""
import requests

url = 'https://api.tvmaze.com/search/shows?q=supernatural'

episodes = []

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data[0]['show']['name'] == 'Supernatural':
        data_id = data[0]['show']['id']

    url_id = f'https://api.tvmaze.com/shows/{data_id}/episodes'
    response_2 = requests.get(url_id)
    if response_2.status_code == 200:
        data_2 = response_2.json()
        for series in data_2:
            episodes.append({series['name']: {
                            'season': series['season'],
                            'number': series['number'],
                            'airdate': series['airdate'],
                            'rating': series['rating']['average']
                            }})
    else:
        print('ошибка', response.status_code)

else:
    print('ошибка', response.status_code)

for series in episodes:
    print(series)
