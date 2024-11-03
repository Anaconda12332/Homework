def converter(num):
    match choice:
        case '1':
            return round(num / 1609, 8)
        case '2':
            return round(num * 39.37, 8)
        case '3':
            return round(num * 1.094, 8)

user_input=float(input('Укажите количество метров: '))

choice=input('1-Миля\n2-Дюйм\n3-Ярд\nУкажите единицу измерения для конвертации: ')

print(converter(user_input))