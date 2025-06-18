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
        *
       / \
     +     -
     / \  / \
    2   3 4   1
"""
from abc import ABC, abstractmethod

# expr = Multiplication(
#     Addition(Number(2), Number(3)),
#     Subtraction(Number(4), Number(1))
# )
# print(expr.evaluate()) #15

""""""


class Expression(ABC):
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Number(Exception):
    def __init__(self, number):
        self.number = number

    def evaluate(self):
        return self.number

    def __str__(self):
        return str(self.number)


class Addition(Expression):
    def __init__(self, left: Exception, right: Exception):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def __str__(self):
        return f'({self.left} + {self.right})'


class Subtraction(Expression):
    def __init__(self, left: Exception, right: Exception):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

    def __str__(self):
        return f'({self.left} - {self.right})'


class Multiplication(Expression):
    def __init__(self, left: Exception, right: Exception):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def __str__(self):
        return f'({self.left} * {self.right})'


class Division(Expression):
    def __init__(self, left: Exception, right: Exception):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

    def __str__(self):
        return f'({self.left} / {self.right})'


expr = Multiplication(
    Addition(Number(2), Number(3)),
    Subtraction(Number(4), Number(1))
)

expr2 = Division(
                Multiplication(
                                Addition(Number(2), Number(3)),
                                Subtraction(Number(4), Number(1)),
                ),
                Multiplication(
                                Addition(Number(2), Number(3)),
                                Subtraction(Number(4), Number(3)),
                ))

print(expr, '=', expr.evaluate())
print(expr2, '=', expr2.evaluate())
