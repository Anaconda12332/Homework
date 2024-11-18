user_input=int(input('Введите начало диапазона: '))
user_input_2=int(input('Введите конец диапазона: '))

for i in range(user_input, user_input_2 + 1):
    for b in range(1, 11):
        print(f'{i} * {b} = {i * b}', end='\t')
    print()