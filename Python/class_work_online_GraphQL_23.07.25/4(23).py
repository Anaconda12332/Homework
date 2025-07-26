import requests
"""
Составьте запрос, который возвращает список с языками, на которых
говорят во всех странах. Постройте круговую диаграмму, отображающую
Топ-10 используемых языков среди всех стран.
"""

upl = 'https://countries.trevorblades.com/'

qerry = '''
{
    countries {
        languages {
            name
        }
    }
}
'''
lang = []

response = requests.post(upl, json={'query': qerry})
if response.status_code == 200:
    data = response.json()
    for i in data['data']['countries']:
        for language in i['languages']:
            lang.append(language['name'])
else:
    print('ошибка', response.status_code)

for i in lang:
    print(i)
