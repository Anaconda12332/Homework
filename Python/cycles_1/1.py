def us_range(numb, numb2):
    us_list=list(range(numb, numb2 + 1))
    return [i for i in us_list if i %7 == 0]


user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

print(*(us_range(user_input, user_input_2)), sep=', ')