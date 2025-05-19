"""
словарь с данными пользователя
список чисел
кортеж строк

сохранить в один .pkl
в .json

считать .pkl (load) + print
считать .json (load) + print

pickle.dumps() + pickle.loads()
json.dumps() + json.loads()
"""
import pickle
import json


person = {'Name': 'Alex', 'Age': 12}

numb = [1, 2, 3]

tuple_of_strings = (
    '1',
    '2',
    '3'
)

with open('user.pkl', 'wb') as file:
    pickle.dump((person, numb, tuple_of_strings), file)

with open('user.pkl', 'rb') as file:
    person_pkl, numb_pkl, tuple_of_strings_pkl = pickle.load(file)


print(person_pkl, numb_pkl, tuple_of_strings_pkl)

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(
        {
            'person': person,
            'numb': numb,
            'tuple_of_strings': tuple_of_strings
        },
        file,
        ensure_ascii=False,
        indent=4
    )

with open('user.json', 'r', encoding='utf-8') as file:
    json_format = json.load(file)

print(json_format['person'])
print(json_format['numb'])
print(json_format['tuple_of_strings'])


string = (1, 2, 3)
string_p = pickle.dumps(string)
print(pickle.loads(string_p))

string = (1, 2, 3)
string_j = json.dumps(string)
print(json.loads(string_j))
