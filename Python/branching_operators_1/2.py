def operation(*numbers):
    match sign:
        case '1':
            return max(*numbers)
        case '2':
            return min(*numbers)
        case '3':
            return round((sum(*numbers)) / len(*numbers), 2)
        
user_input=list(map(float, input('Введите три числа через пробел: ').split()))

sign=input('1-Максимум\n2-Минимум\n3-Среднее арифметическое\nУкажите операцию: ')

print(operation(user_input))