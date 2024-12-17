def simple(num):
    simple_list=[]

    for i in num:
        if i==2 or i==3 or i==5 or i==7:
            simple_list.append(i)
        elif i %2 !=0 and i %3 !=0 and i %5 != 0 and i %7 !=0:
            simple_list.append(i) if i  !=1 else None

            
    return 'Количество простых чисел:', len(simple_list)

user_input=list(map(int, input('Введите целые числе через пробел: ').split()))

print(*simple(user_input))
