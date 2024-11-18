def number(a):
    if a > 0:
        return('Number is positive') 
    elif a < 0:
        return('Number is negative')
    else:
        return('Number is equal to zero')

while True:
    user_input=float(input('Введите число: '))
    print(number(user_input)) if user_input != 7 else print('Good bye!')
    if user_input == 7.0:
        break