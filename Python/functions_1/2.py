def even(num, num_2):
    even_num=[]
    for i in range(num, num_2+1):
        if i %2 ==0:
            even_num.append(i)
    return even_num



user_input=list(map(int, (input('Введите два числа через пробел: ')).split()))

print(f'Четные числа в указанном диапазоне: ', *even(*user_input))