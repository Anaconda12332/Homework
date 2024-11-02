import math
def all_numders(*user_imput):
    return math.prod(user_imput), sum(user_imput)

user_imput=list(map(float, (input('Введите три числа, разделенные пробелом: ').split())))

result= all_numders(*user_imput)[0], all_numders(*user_imput)[1]
print(f"Произведение чисел {user_imput} равно: {round(result[0], 1)}\nСумма чисел {user_imput} равна: {result[1]}")