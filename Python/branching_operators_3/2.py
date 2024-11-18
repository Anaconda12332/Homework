user_input=float(input('Укажите число: '))
user_degree=float(input('Укажите степень от 0 до 7: '))

result= round(user_input ** user_degree, 2) 

print(result) if user_degree <=7 else print('Ошибка, укажите степень от 0 до 7!')