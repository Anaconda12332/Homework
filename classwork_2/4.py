def zp(numb):
    if numb < 550:
        return 0.03
    elif 500 < numb < 1000:
        return 0.05
    else:
        return 0.08
    

a={}

user_input=list(input('Введите имя менеджера: '))

user_input_2=list(map(float, (input('Введите его уровень продаж: ').split())))



for i, b in zip (user_input, user_input_2):
    print(i, b)
    a.update({i: b})
    
print(a)


result= 200 + zp(user_input_2)

print(result)