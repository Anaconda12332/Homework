
"""
система обработки различных геометрических фигур (круг, прямоугольник,
треугольник)
разные операции (вычисление площади, периметра, "рисование в консоли")

Circle, Rectangle, Triangle

фигуры реализовывают интерфейс Shape
def accept(self, visitor):

интерфейс ShapeVisitor
def visit_circle(self, circle):
def visit_rectangle(self, rectangle):
def visit_triangle(self, triangle):

реализовать два конкретных посетителя
AreaCalculator, ShapePrinter
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def accept(self, visitor):
        return visitor.visit_triangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

    @abstractmethod
    def visit_triangle(self, triangle):
        pass


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return math.pi * circle.radius ** 2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

    def visit_triangle(self, triangle):
        return triangle.base * triangle.height / 2


class ShapePrinter(ShapeVisitor):
    def visit_circle(self, circle):
        return f"круг радиусом {circle.radius}"

    def visit_rectangle(self, rectangle):
        return f"прямоугольник шириной {rectangle.width
                                        } и высотой {rectangle.height}"

    def visit_triangle(self, triangle):
        return f"треугольник основанием {triangle.base
                                         } и высотой {triangle.height}"


class SVGExporter(ShapeVisitor):
    def visit_circle(self, circle):
        return f"<circle cx='{circle.radius}' cy='{circle.radius
                                                   }' r='{circle.radius}' />"

    def visit_rectangle(self, rectangle):
        return f"<rect x='0' y='0' width='{rectangle.width
                                           }' height='{rectangle.height}' />"

    def visit_triangle(self, triangle):
        return f"<polygon points='0,0 {triangle.base
                                       },0 {triangle.base / 2
                                            },{triangle.height}' />"


shapes = [
    Circle(radius=5),
    Rectangle(width=10, height=20),
    Triangle(base=10, height=10)
]

area_calculator = AreaCalculator()
shape_printer = ShapePrinter()
svg_exporter = SVGExporter()

for shape in shapes:
    print(shape.accept(area_calculator))
    print(shape.accept(shape_printer))
    print(shape.accept(svg_exporter))
