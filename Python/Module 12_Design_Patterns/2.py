"""
Создайте приложение для приготовления пасты. Приложение должно уметь
создавать минимум три вида пасты. Классы различной пасты должны иметь следующие
методы:
■ Тип пасты;
■ Соус;
■ Начинка;
■ Добавки.
Для реализации используйте порождающие паттерны.
"""
from abc import ABC, abstractmethod


class TypeOfPasta(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Sauce(ABC):
    @abstractmethod
    def get_sauce(self):
        pass


class Filling(ABC):
    @abstractmethod
    def get_filling(self):
        pass


class Additives(ABC):
    @abstractmethod
    def get_additives(self):
        pass


class Bolognese(TypeOfPasta):
    def get_type(self):
        return 'Болоньезе'


class MeatSauce(Sauce):
    def get_sauce(self):
        return 'Мясной соус'


class Beef(Filling):
    def get_filling(self):
        return 'Говядина'


class Tomatoes(Additives):
    def get_additives(self):
        return 'Томаты'


class Carbonara(TypeOfPasta):
    def get_type(self):
        return 'Карбонара'


class DemiGlaceSauce(Sauce):
    def get_sauce(self):
        return 'Демиглас соус'


class Bacon(Filling):
    def get_filling(self):
        return 'Бекон'


class Cream(Additives):
    def get_additives(self):
        return 'Сливки'


class Farfalle(TypeOfPasta):
    def get_type(self):
        return 'Фарфалле'


class СreamySauce(Sauce):
    def get_sauce(self):
        return 'Сливочный соус'


class Salmon(Filling):
    def get_filling(self):
        return 'Лосось'


class Spinach(Additives):
    def get_additives(self):
        return 'Шпинат'


class CreatePasteFactory(ABC):
    @abstractmethod
    def create_type(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_filling(self):
        pass

    @abstractmethod
    def create_additives(self):
        pass


class BolognesePaste(CreatePasteFactory):
    def create_type(self):
        return Bolognese()

    def create_sauce(self):
        return MeatSauce()

    def create_filling(self):
        return Beef()

    def create_additives(self):
        return Tomatoes()


class CarbonaraPaste(CreatePasteFactory):
    def create_type(self):
        return Carbonara()

    def create_sauce(self):
        return DemiGlaceSauce()

    def create_filling(self):
        return Bacon()

    def create_additives(self):
        return Cream()


class FarfallePaste(CreatePasteFactory):
    def create_type(self):
        return Farfalle()

    def create_sauce(self):
        return СreamySauce()

    def create_filling(self):
        return Salmon()

    def create_additives(self):
        return Spinach()


def create_paste(pasta: CreatePasteFactory):
    types = pasta.create_type()
    sause = pasta.create_sauce()
    filling = pasta.create_filling()
    additives = pasta.create_additives()

    print(types.get_type())
    print(sause.get_sauce())
    print(filling.get_filling())
    print(additives.get_additives())
    print('-' * 30)


bolognese = BolognesePaste()
carbonara = CarbonaraPaste()
farfalle = FarfallePaste()

create_paste(bolognese)
create_paste(carbonara)
create_paste(farfalle)
