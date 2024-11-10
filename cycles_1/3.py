user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

user_list= [i for i in range(user_input, user_input_2 + 1)]

for i in user_list:
    if i %3 ==0 and i %5 ==0:
        print('Fizz Buzz', end=', ')
    elif i %3 ==0:
        print('Fizz', end=', ')

    elif i %5 ==0:
        print('Buzz', end=', ')
    
    else:
        print(i, end=', ')