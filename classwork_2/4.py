def zp(numb):
    if numb < 500:
        return 0.03
    elif 500 < numb < 1000:
        return 0.05
    else:
        return 0.08
    

user_input=list(input('Введите имя менеджера: ').split())
user_input_2=list(map(int, (input('Введите его уровень продаж: ').split())))
best=max(user_input_2)
result_zp=[]

for i in user_input_2:
    if i == best:
        result_zp.append(200 + 200 + 200 * zp(i))
    else:
        result_zp.append(200 + 200 * zp(i))


user_dict_zp=dict(zip(user_input, result_zp))
user_dict=dict(zip(user_input_2, user_input))


print(f'Зарплата менеждеров: {user_dict_zp}')
print(f'Лучший менеджер: {user_dict[best]}')