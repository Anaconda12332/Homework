
def a(numbers):
    if numbers %3 == 0 and numbers %5 == 0:
        return('Fizz Buzz')

    elif numbers %3 == 0 or numbers %5 == 0:
        if numbers %3 == 0:
            return('Fizz')
        elif numbers %5 == 0:
            return('Buzz')

    else:
        return(numbers)



user_input=float(input('Введите число в диапазоне от 1 до 100: ')) 

print(a(user_input)) if 1 <= user_input < 100 else print('Ошибка, введите число в диапазоне от 1 до 100!')


