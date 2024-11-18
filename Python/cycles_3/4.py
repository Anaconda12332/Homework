user_input=input('Введите число: ')

trans_table=str.maketrans('', '', '36')

print(user_input.translate(trans_table))