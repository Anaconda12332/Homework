import math

def prod_u(num):
    return math.prod(num)

user_list=list(map(int, input('Введите целые числа через пробел: '). split()))

print('Произведение чисел равно:',prod_u(user_list))