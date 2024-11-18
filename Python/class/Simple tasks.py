#1

sm=float(input('Введите сантиметры: '))
print(sm /  100)

#2

m=float(input('Введите кг: '))
print(m /  100)

#3

m=float(input('Введите кг: '))
print(m /  1000)

#4

m=float(input('Введите метры: '))
print(m /  1000)


#5

days=243
print('С какого то момента прошло: {}'.format(days // 7))

#6

n= 111111
chas= n / 3600
miin= chas-round(chas)
sek= (miin-round(miin)) / 60

print(chas, miin, sek)

#исправить

#7

print(543// 130)

#8

k=int(input(': '))

if k % 7 == 0:
    print('Понедельник')

elif (k-1) % 7 == 0:
     print('Вторник')
elif (k-2) % 7 == 0:
     print('Среда')
elif (k-3) % 7 == 0:
     print('Четверг')
elif (k-4) % 7 == 0:
     print('Пятница')
elif (k-5) % 7 == 0:
     print('Суббота')
elif (k-6) % 7 == 0:
     print('Воскресенье')
