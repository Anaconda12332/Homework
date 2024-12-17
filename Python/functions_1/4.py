def min_num(num):
    return min(num)


user_input=list(map(float, input('Введите пять чисел через пробел: ').split()))

print('Минимальное число: ', min_num(user_input))