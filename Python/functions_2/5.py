def association(list_1, list_2):
    return list_1+list_2

user_list=list(map(int, input('Введите первый список целых чисел через пробел: ').split()))
user_list_2=list(map(int, input('Введите второй список целых чисел через пробел: ').split()))

print(association(user_list, user_list_2))
