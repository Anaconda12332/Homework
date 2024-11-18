user_input = list(range(int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))))

simple = []

for i in user_input:
    divider = 1
    for b in range(1, i+1):
        if i % b == 0:
            divider += 1      
    if divider <= 3:  
        simple.append(int(i))  if i != 1 else None     
print('Простые числа в введенном диапазоне: ', *simple)