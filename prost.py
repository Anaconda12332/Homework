days={1: 'Понедельник',2: 'Вторник',3: 'Среда',4: 'Четверг',5: 'Пятница',6: 'Суббота',7: 'Воскресенье'}

us=int(input(':'))

a=[i for i in range(1, 366, 7)]

if us in a:
    print(days[1])
elif us -1 in a:
    print(days[2])
elif us -2 in a:
    print(days[3])
elif us -3 in a:
    print(days[4])
elif us -4 in a:
    print(days[5])
elif us -5 in a:
    print(days[6])
elif us -6 in a:
    print(days[7])