import requests

"""
1 часть
https://api.thecatapi.com/v1
получить случайное изображение кошки
    get https://api.thecatapi.com/v1/image/search
    статус код 
    полученные данные
    только ссылку на изображение из json ответа - список с одним словарем, внутри "url"

2 limit в параметках. 5 случайных изображений кошек, выводить только список ссылок
3 корректный код (timeout ошибки...)
"""


def search_cats(limit=10, timeout=3):
    try:
        params = {'limit': limit}
        response = requests.get("https://api.thecatapi.com/v1/images/search", params=params, timeout=timeout)
        response.raise_for_status()
        print('статус код:', response.status_code)
        data = response.json()
        url = [cat['url'] for cat in data]
        print(*url, sep='\n')

    except requests.exceptions.HTTPError as http_err:
        print(f"ошибка HTTP {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"ошибка соединения {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"таймаут {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"другая ошибка {err}")


search_cats()
