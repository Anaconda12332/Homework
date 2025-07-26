import requests

upl = 'https://countries.trevorblades.com/'

qerry = '''
{
    countries {
        name
        continent {
            name
        }
    }
}
'''

response = requests.post(upl, json={'query': qerry})
if response.status_code == 200:
    data = response.json()
    for country in data['data']['countries']:
        print(f'Страна: {country["name"]}')
        print(f'Континент: {country["continent"]["name"]}', '\n')
else:
    print('ошибка', response.status_code)
