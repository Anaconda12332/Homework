def sepen(u_list, u_sepen):
    new_list=[]
    for i in u_list:
        new_list.append(i ** u_sepen)
    return new_list

user_list=list(map(int, input('Введите список через пробел: ').split()))
user_sepen=int(input('Укажите степень: '))

print(sepen(user_list, user_sepen))