"""
Создайте реализацию паттерна Builder. Протестируйте
работу созданного класса.
"""

"""
Создайте систему для построения пиццы, используя паттерн Builder. У вас должны быть следующие классы:

Pizza: класс, представляющий пиццу. Он должен иметь атрибуты для теста, соуса, сыра и начинки.

PizzaBuilder: абстрактный класс, представляющий строителя. Он должен иметь 
методы для установки теста, соуса, сыра и начинки, а также метод get_pizza, 
который возвращает построенную пиццу.

ConcretePizzaBuilder: конкретный класс строителя, который реализует методы для 
установки теста, соуса, сыра и начинки.

Director: класс, который использует строителя для построения пиццы. 
Он должен иметь метод construct_pizza, который использует строителя для построения пиццы.
"""
from abc import ABC, abstractmethod


class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None

    def __str__(self):
        return f'[Pizza]: {', '.join(self.__dict__.values())}'


class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def add_name(self, ingredients):
        pass

    @abstractmethod
    def add_dough(self, ingredients):
        pass

    @abstractmethod
    def add_sauce(self, ingredients):
        pass

    @abstractmethod
    def add_cheese(self, ingredients):
        pass

    @abstractmethod
    def add_toppings(self, ingredients):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class ConcretePizzaBuilder(PizzaBuilder):
    def add_name(self, name):
        self.pizza.name = name

    def add_dough(self, ingredients):
        self.pizza.dough = ingredients

    def add_sauce(self, ingredients):
        self.pizza.sauce = ingredients

    def add_cheese(self, ingredients):
        self.pizza.cheese = ingredients

    def add_toppings(self, ingredients):
        self.pizza.toppings = ingredients

    def get_pizza(self):
        return self.pizza


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def standart_pizza(self):
        self.builder.add_name('Стандартная пицца')
        self.builder.add_dough('Стандартное тесто')
        self.builder.add_sauce('Стандартный сосус')
        self.builder.add_cheese('Два вида сыра')
        self.builder.add_toppings('Курица')

    def vegetarian_pizza(self):
        self.builder.add_name('Вегетарианская пицца')
        self.builder.add_dough('Пышное тесто')
        self.builder.add_sauce('Стандартный сосус')
        self.builder.add_cheese('Три вида сыра')
        self.builder.add_toppings('Грибы')

    def spicy_pizza(self):
        self.builder.add_name('Острая пицца')
        self.builder.add_dough('Тонкое тесто')
        self.builder.add_sauce('Перец чили')
        self.builder.add_cheese('Сыр моцарелла')
        self.builder.add_toppings('Пеперони')


new_pizaa = ConcretePizzaBuilder()
director = Director(new_pizaa)

director.standart_pizza()
print(new_pizaa.get_pizza())
print('-' * 90)

director.vegetarian_pizza()
print(new_pizaa.get_pizza())
print('-' * 90)

director.spicy_pizza()
print(new_pizaa.get_pizza())
print('-' * 90)
