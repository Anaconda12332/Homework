
def numbers(*numb):
    if numb[0] == numb[1]:
        return f'Числа {numb} равны!'
    else:
        return sorted(numb)
    
user_input=list(map(float, (input('Введите два числа через пробел: ')).split()))

print(numbers(*user_input))
