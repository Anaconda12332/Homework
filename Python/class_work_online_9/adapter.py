"""
реализовано
Rectangle (координаты левого верхнего угла, ширину и высоту)

надо добавить
LegacySquare (координаты центра и длина стороны)

Rectangle
    x
    y
    width
    height
LegacySquare
    cx
    cy
    side

создать интерфейс или базовый класс Drawable с draw()
Rectangle реализует Drawable
Reactangle.draw()

SquareAdapter принимает объект LegacySquare и реализует интерфейс Drawable
"""
from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Drawable):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        print(f"Прямоугольник с координатами ({self.x},{self.y}) и шириной {self.width} и высотой {self.height}")


class LegasySqyare:
    def __init__(self, cx, cy, side):
        self.cx = cx
        self.cy = cy
        self.side = side


class SquareAdapter(Drawable):
    def __init__(self, square):
        self.square = square

    def draw(self):
        x = self.square.cx - self.square.side / 2
        y = self.square.cy - self.square.side / 2
        print(f"Квадрат с координатами ({x},{y}) и стороной {self.square.side}")


shapes = [
    Rectangle(0, 0, 100, 50),
    SquareAdapter(LegasySqyare(50, 50, 40))
]

for shape in shapes:
    shape.draw()
