def number(a):
    if a > 0:
        return('Number is positive')
    elif a < 0:
        return('Number is negative')
    else:
        return('Number is equal to zero')

user_input=float(input('Введите число: '))

print(number(user_input))