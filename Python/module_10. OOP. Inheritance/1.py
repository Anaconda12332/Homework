class Device:
    def __init__(self, name, brand, model, power, guarantee):
        self.name = name
        self.brand = brand
        self.model = model
        self.power = power
        self.guarantee = guarantee

    def info(self):
        print(f'{self.name} - {self.brand}({self.model}).\n'
              f'Мощность - {self.power} Вт.\nГарантия - {self.guarantee}.')


class CoffeMachine (Device):
    def __init__(self, *args):
        super().__init__('Кофемашина', *args)

    def info(self):
        super().info()
        print('Полностью автоматическая эспрессо-кофемашина!\n')


class Blender (Device):
    def __init__(self, *args):
        super().__init__('Блендер', *args)

    def info(self):
        super().info()
        print('Блендер обладает прочным ножом из нержавеющей стали'
              'с 4 острыми лезвиями.\n')


class MeatGrinder (Device):
    def __init__(self, *args):
        super().__init__('Мясорубка', *args)

    def info(self):
        super().info()
        print('Мясорубка это производительная бытовая техника для'
              'измельчения сырых и обработанных продуктов, натирания и'
              'шинковки,\nа также приготовления колбас и кеббе.\n')


Phillips = CoffeMachine('"Phillips"', 'Серия 2200', 1500, '2г')
Bosch = Blender('"Bosch"', 'Серия MSM6B100', 280, '1г')
Axion = MeatGrinder('"Axion"', 'Серия М 33.03', 230, '3г')

Phillips.info()
Bosch.info()
Axion.info()
