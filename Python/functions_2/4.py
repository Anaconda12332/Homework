def dell(us_list, num):
    quantity=0
    while num in us_list:
            us_list.remove(num)
            quantity +=1
    return f'Количество удаленных элементов: {quantity}' 


user_list=list(map(int, input('Введите целые числа через пробел: ').split()))
user_num=int(input('Укажите целое число, которое нужно удалить: '))
       
print(dell(user_list, user_num))

