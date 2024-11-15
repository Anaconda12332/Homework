#days={1: 'Понедельник',2: 'Вторник',3: 'Среда',4: 'Четверг',5: 'Пятница',6: 'Суббота',7: 'Воскресенье'}

us=int(input(':'))

a=[i for i in range(1, 366, 7)]

if us in a:
    print('понедельник')
elif us -1 in a:
    print('вт')
elif us -2 in a:
    print('ср')
elif us -3 in a:
    print('чт')
elif us -4 in a:
    print('пт')
elif us -5 in a:
    print('сб')
elif us -6 in a:
    print('вс')