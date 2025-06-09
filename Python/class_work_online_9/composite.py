"""
вычислительная система
вложенные
(2+3)*(4-1)
число - лист
операция - компонент

class Expression def evaluate
классы-листья Number
классы-композиты
Addition, Subtraction, Multiplication, Division принимают два дочерних
выражения, которые реализуют интерфейс Expression

"""
# expr = Multiplication(
#     Addition(Number(2), Number(3)),
#     Subtraction(Number(4), Number(1))
# )
# print(expr.evaluate()) #15
