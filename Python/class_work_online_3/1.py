"""
данные о человеке имя возраст
user.pkl

список чисел
кортеж строк
.dumps - байты
print()

+json
user.json
"""
import pickle
import json


'''
pickle

'''

person = {'Name': 'Alex', 'Age': 12}

person_p = pickle.dumps(person)

with open('user.pkl', 'wb') as file:
    pickle.dump(person, file)


numb = [1, 2, 3]
numb_p = pickle.dumps(numb)

with open('user.pkl', 'ab+') as file:
    pickle.dump(numb, file)


tuple_of_strings = (
    '1',
    '2',
    '3'
)
tuple_of_strings_p = pickle.dumps(tuple_of_strings)

with open('user.pkl', 'ab+') as file:
    pickle.dump(tuple_of_strings, file)


'''
json

'''

person = {'Name': 'Alex', 'Age': 12}
person_j = json.dumps(person, ensure_ascii=False, indent=4)

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(person, file, ensure_ascii=False, indent=4)


numb = [1, 2, 3]
numb_j = json.dumps(numb, ensure_ascii=False, indent=4)

with open('user.json', 'a', encoding='utf-8') as file:
    json.dump(numb, file, ensure_ascii=False, indent=4)

tuple_of_strings = (
    '1',
    '2',
    '3'
)
tuple_of_strings_j = json.dumps(tuple_of_strings, ensure_ascii=False, indent=4)

with open('user.json', 'a', encoding='utf-8') as file:
    json.dump(tuple_of_strings, file, ensure_ascii=False, indent=4)

print(person_p)
print(numb_p)
print(tuple_of_strings_p)

print(person_j)
print(numb_j)
print(tuple_of_strings_j)
