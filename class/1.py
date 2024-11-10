
user_input=int(input('Введите первое число: '))
user_input_2=int(input('Введите второе число: '))

a=[i for i in range(user_input, user_input_2 + 1) if i %2 == 0]
b=[i for i in range(user_input, user_input_2 + 1) if i %2 != 0]
d=[i for i in range(user_input, user_input_2 + 1) if i %9 == 0]


print(f'Сумма четных чисел: {sum(a)}\nСумма нечетных чисел: {sum(b)}\nСумма чисел, кратных 9: {sum(d)}')
print(f'Среднее арифметическое четных чисел: ', sum(a) / len(a))
print(f'Среднее арифметическое нечетных чисел: ', sum(b) / len(b))
print(f'Среднее арифметическое чисел, кратных 9: ', sum(d) / len(d))