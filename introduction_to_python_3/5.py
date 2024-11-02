user_input=input('Введите четырехзначное число: ')

result=int(''.join(reversed(user_input)))
print(result)