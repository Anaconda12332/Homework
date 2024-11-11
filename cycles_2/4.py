def a(num):
    return f'Сумма чисел:  {sum(all)}', f'Максимум чисел: {max(all)}', f'Минимум чисел: {min(all)}'

all=[]
while True:
    user_input=float(input('Введите число: '))
    all.append(user_input)
    print( *a(user_input), sep='\n'  )  if user_input != 7 else print('Good bye!')
    if user_input == 7.0:
        break