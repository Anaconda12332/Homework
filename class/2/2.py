def a(n, n_q):
    all=[]
    num_7=[]
    num_5=[]
    for i in range(user_input, user_input_2 + 1):
        all.append(i)
        if i %7 ==0:
            num_7.append(i)
        if i %5 ==0:
            num_5.append(i)
    return all, all[::-1], num_7, sum(num_5) 

user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

print(*(a(user_input, user_input_2)))