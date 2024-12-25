def academic(grade):
    a=1
    while a:
        menu=input("1. Вывод оценок 2. Пересдача экзамена 3. Степендия 4. Итоговый список: ")
        match menu:
            case '1':
                print("Список оценок: ", *grade)
            case '2':
                retake=list(map(int, (input("Введите номер элемента из списка и новую оценку: ").split())))
                grade[retake[0]]=retake[1]
            case '3':
                scholarship=[]
                for i in grade:
                    if i >= 10.7:
                        scholarship.append('+')
                    else:
                        scholarship.append('-')
                # print(dict(zip(grade, scholarship)))
                print(*grade,'\n',*scholarship)
            case '4':
                end=int(input("1. По возрастанию 2. По убыванию: "))
                print(*sorted(grade)) if end ==1 else  print(*sorted(grade, reverse=True))
                a=0

user_input=list(map(int, input("Введите список оценок от 1 до 12: ").split()))
academic(user_input)

    
    
    
   
 