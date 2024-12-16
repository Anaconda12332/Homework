def shapes(lenn, sign, bools):
    if bools == False:
        return [[sign if i==0 or i == lenn-1 or j == 0 or j== lenn-1 else " " for j in range(lenn) 
                ]for i in range(lenn)]

    elif bools == True:
        return [["*" for i in range(lenn)]for j in range(lenn)]


user_lenn=int(input("Введите длину стороны квадрата: ") )
user_sign=input("Введите знак заполнитель: ")
user_bools=bool(int(input("Введите условие для заполения, где:"+"\n"+" 1-Заполненый квадрат, 0-Полый квадрат: "))) 

for i in shapes(user_lenn, user_sign, user_bools):

    print(*i)