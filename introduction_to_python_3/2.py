import math
user_input=list(map(float, (input('Введите четыре числа через пробел: ').split())))

user_prod=math.prod(user_input)
print(f'Произведение чисел {user_input} равно: {round(user_prod, 1)}')