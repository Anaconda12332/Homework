class Ship:
    def __init__(self, name, length, width, speed):
        self.name = name
        self.length = length
        self.width = width
        self.speed = speed

    def info(self):
        print(f'Корабль - {self.name}:\nДлина - {self.length} м.\n'
              f'Ширина - {self.width} м.\nСкорость - {self.speed} уз.')


class Frigate(Ship):
    def info(self):
        super().info()
        print('Современный фрегат — сторожевой корабль, '
              'класс военно-морских кораблей.\n')


class Destroyer(Ship):
    def info(self):
        super().info()
        print('Эсминец — это быстрый, маневренный, долговечный военный '
              'корабль, предназначенный для сопровождения более крупных судов '
              '\nв составе флота, конвоя или авианосной боевой группы и их '
              'защиты от широкого спектра общих угроз.\n')


class Cruiser(Ship):
    def info(self):
        super().info()
        print('Крейсер - класс боевых надводных кораблей, способных '
              'выполнять задачи независимо от основного флота.\n')


frigate = Frigate('"Фрегат"', 163.5, 19, 32)
destroyer = Destroyer('"Эсминец"', 145, 16, 32)
cruiser = Cruiser('"Крейсер"', 172.8, 16.7, 31.5)

frigate.info()
destroyer.info()
cruiser.info()
