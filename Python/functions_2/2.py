def min_num(num):
    return min(num)


user_list=list(map(int, input('Введите пять целых чисел через пробел: ').split()))

print('Минимальное число: ', min_num(user_list))