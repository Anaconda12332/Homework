def check(num):
    if ''.join(reversed(num)) == num:
        return True
    else:
        return False
        

user_input=input('Введите число: ')


print(check(user_input))