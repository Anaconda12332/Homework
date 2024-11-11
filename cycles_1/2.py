def a(num, num2):
    all=[]
    num_7=[]
    num_5=[]
    for i in range(user_input, user_input_2 + 1):
        all.append(i)
        if i %7 ==0:
            num_7.append(i)
        if i %5 ==0:
            num_5.append(i)
    return all, all[::-1], num_7, len(num_5) 

user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

print('Все числа диапазона:', *a(user_input, user_input_2)[0])
print('Все числа диапазона в убывающем порядке:', *a(user_input, user_input_2)[1])
print('Все числа кратные 7:', *a(user_input, user_input_2)[2])
print('Количество чисел, кратных 5:', a(user_input, user_input_2)[3])