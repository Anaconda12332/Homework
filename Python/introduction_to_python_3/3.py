def converter(meters):
    return meters * 100, meters * 10, meters * 1000, meters / 1609
      

user_input=float(input("Введите метры: "))
result=converter(user_input)

print(f'Сантиметры: {result[0]}\nДециметры: {result[1]}\nМиллиметры: {result[2]}\nМили: {round(result[3], 7)}')