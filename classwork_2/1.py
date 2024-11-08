user_input=float(input('Введите число в диапазоне от 1 до 100: ')) 

if 1 <= user_input < 100:

    if user_input %3 == 0 and user_input %5 == 0:
        print('Fizz Buzz')

    elif user_input %3 == 0 or user_input %5 == 0:
        if user_input %3 == 0:
            print('Fizz')
        elif user_input %5 == 0:
            print('Buzz')

    else:
        print(user_input)

else:
    print('Ошибка, введите число в диапазоне от 1 до 100!')
    