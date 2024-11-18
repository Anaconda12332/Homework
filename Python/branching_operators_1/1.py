import math
def operation(*numbers):
    match sign:
        case '1':
            return sum(*numbers)
        case '2':
            return round(math.prod(*numbers), 2)
        
user_input=list(map(float, input('Введите три числа через пробел: ').split()))

sign=input('1-Сумма\n2-Произведение\nУкажите операцию: ')

print(operation(user_input))