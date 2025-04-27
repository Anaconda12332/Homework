# """
# метакласс PrintMeta
# каждый раз при создании нового класса выводит
# Класс <ИмяКласса> создан.
# """

# class Myclass1(type):
#     def __new__(cls, name, bases, dct):
#         print(f"{name} создан")
#         return super().__new__(cls, name, bases, dct)

# class a(metaclass=Myclass1):
#     pass



# """
# метакласс UpperAttrMeta
# преобразует все имена атрибутов в верхний регистр
# """

# class Myclass2(type):
#     def __new__(cls, name, bases, dct):
#         uppers = {}
#         for key, value in dct.items():
#             if not key.startswith('__'):
#                 uppers[key.upper()]=value
#             else:
#                 uppers[key]=value

#         return super().__new__(cls, name, bases, uppers)
    
# class b(metaclass=Myclass2):
#     ff = 'q'
    
#     def method(self):
#         return 'a'

# print(b.FF)


# 2

# Задание 2 Создайте класс Дробь (или используйте уже ранее созданный вами). 
# Используя перегрузку операторов ре ализуйте для него арифметические операции 
# для работы с дробями (операции +, -, *, /).

# class fraction(type):
#     def __init__(self, name, a, b):
#         self.name = name
#         self.a = a
#         self.b = b
#     def __add__(a, b):
#         return f" {a[1] * b[0]} + {a[0] * b[1]} / {a[1]*b[1]}"
    
# class a(metaclass=fraction):
#     aa = (1, 2)
#     ba = (1, 2)
#     # def ac (a, b):
#     #     return a + b

# print(a.__add__)

class fraction(self, name, a, b):
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b
    def __add__(a, b):
        return f" {a[1] * b[0]} + {a[0] * b[1]} / {a[1]*b[1]}"
    
class a(metaclass=fraction):
    aa = (1, 2)
    ba = (1, 2)


print(fraction.(1, 2)__add__)