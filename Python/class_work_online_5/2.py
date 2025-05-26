from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.add_condiments()
        self.pour()

    def boil_water(self):
        print("кипятим")

    def pour(self):
        print("в кружку")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print("чай")

    def add_condiments(self):
        print("сахар")


class Coffee(Beverage):
    def brew(self):
        print("кофе")

    def add_condiments(self):
        print("молоко")


class HotChocolate(Beverage):
    def brew(self):
        print("какао")

    def add_condiments(self):
        print("молоко")


tea = Tea()
tea.prepare()

print('---------')

coffee = Coffee()
coffee.prepare()

print('---------')

hot_chocolate = HotChocolate()
hot_chocolate.prepare()
