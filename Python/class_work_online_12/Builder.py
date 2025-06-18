"""
Builder
создание туристических туров
набор компонентов тура:
проживание
экскурсии
транспорт
питание
страховка

Tour объект сборки
TourBuilder интерфейс сборки
    add_acommodation()
    add_excursions()
    add_transport()
    add_meals()
    add_insurance()
    get_result()

StandardTourBuilder конкретный билдер собирает обект Tour
TourDirector задает порядок шагов билдера
"""
from abc import ABC, abstractmethod

"""
вариант 1
"""


# class Tour:
#     def __init__(self):
#         self.acommodation = None
#         self.excursions = None
#         self.transport = None
#         self.meals = None
#         self.insurance = None

#     def __str__(self):
#         return str(f'[Tour]: Проживание: {self.acommodation}\n'
#                    f'Экскурсии: {self.excursions}\n'
#                    f'Транспорт: {self.transport}\n'
#                    f'Питание: {self.meals}\n'
#                    f'Страховки: {self.insurance}\n')


# class TourBuilder(ABC):
#     def __init__(self):
#         self.tour = Tour()

#     @abstractmethod
#     def add_acommodation(self):
#         pass

#     @abstractmethod
#     def add_excursions(self):
#         pass

#     @abstractmethod
#     def add_transport(self):
#         pass

#     @abstractmethod
#     def add_meals(self):
#         pass

#     @abstractmethod
#     def add_insurance(self):
#         pass

#     def get_result(self):
#         return self.tour


# class StandardTourBuilder(TourBuilder):
#     def add_acommodation(self):
#         self.tour.acommodation = 'Отель 5*'

#     def add_excursions(self):
#         self.tour.excursions = 'Экскурсии в город'

#     def add_transport(self):
#         self.tour.transport = 'Автобус'

#     def add_meals(self):
#         self.tour.meals = 'Завтраки'

#     def add_insurance(self):
#         self.tour.insurance = 'Страховка онлайн'


# class TourDirector:
#     def __init__(self, builder):
#         self.builder = builder

#     def minimal_tyre(self):
#         self.builder.add_acommodation()
#         self.builder.add_transport()

#     def full_tyre(self):
#         self.builder.add_acommodation()
#         self.builder.add_excursions()
#         self.builder.add_transport()
#         self.builder.add_meals()
#         self.builder.add_insurance()


# bilder = StandardTourBuilder()
# director = TourDirector(bilder)

# director.minimal_tyre()
# minimal_tyre = bilder.get_result()
# print(minimal_tyre)
# print('-'*20)

# director.full_tyre()
# full_tyre = bilder.get_result()
# print(full_tyre)

"""
вариант 2
"""


class Tour:
    def __init__(self):
        self.options = []

    def add_options(self, options):
        self.options.append(options)

    def __str__(self):
        return str(f'[Tour]: {self.options}')


class TourBuilder(ABC):
    def __init__(self):
        self.tour = Tour()

    @abstractmethod
    def add_acommodation(self):
        pass

    @abstractmethod
    def add_excursions(self):
        pass

    @abstractmethod
    def add_transport(self):
        pass

    @abstractmethod
    def add_meals(self):
        pass

    @abstractmethod
    def add_insurance(self):
        pass

    def get_result(self):
        return self.tour


class StandardTourBuilder(TourBuilder):
    def add_acommodation(self, options):
        self.tour.acommodation = self.tour.add_options(options)

    def add_excursions(self, options):
        self.tour.excursions = self.tour.add_options(options)

    def add_transport(self, options):
        self.tour.transport = self.tour.add_options(options)

    def add_meals(self, options):
        self.tour.meals = self.tour.add_options(options)

    def add_insurance(self, options):
        self.tour.insurance = self.tour.add_options(options)


class TourDirector:
    def __init__(self, builder):
        self.builder = builder

    def minimal_tyre(self):
        self.builder.add_acommodation('Отель 5*')
        self.builder.add_transport('Автобус')

    def full_tyre(self):
        self.builder.add_acommodation('Отель 5*')
        self.builder.add_excursions('Экскурсии в город')
        self.builder.add_transport('Автобус')
        self.builder.add_meals('Завтраки')
        self.builder.add_insurance('Страховка онлайн')


bilder = StandardTourBuilder()
director = TourDirector(bilder)

director.minimal_tyre()
minimal_tyre = bilder.get_result()
print(minimal_tyre)
print('-'*20)

director.full_tyre()
full_tyre = bilder.get_result()
print(full_tyre)
