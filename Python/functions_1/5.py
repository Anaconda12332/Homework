import math

def prod_u(num, num_2):
    return math.prod(range(num, num_2+1)) if num_2 > num else math.prod(range(num_2, num+1)) 

user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

print('Произведение чисел равно:', prod_u(user_input, user_input_2))