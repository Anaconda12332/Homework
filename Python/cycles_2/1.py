
user_input=int(input('Введите первое число: '))
user_input_2=int(input('Введите второе число: '))

even=[i for i in range(user_input, user_input_2 + 1) if i %2 == 0]
odd=[i for i in range(user_input, user_input_2 + 1) if i %2 != 0]
num_9=[i for i in range(user_input, user_input_2 + 1) if i %9 == 0]


print(f'Сумма четных чисел: {sum(even)}\nСумма нечетных чисел: {sum(odd)}\nСумма чисел, кратных 9: {sum(num_9)}')
print(f'Среднее арифметическое четных чисел: ', sum(even) / len(even))
print(f'Среднее арифметическое нечетных чисел: ', sum(odd) / len(odd))
print(f'Среднее арифметическое чисел, кратных 9: ', sum(num_9) / len(num_9))