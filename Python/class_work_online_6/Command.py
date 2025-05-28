"""Пример"""
from abc import ABC, abstractmethod
# from collections import deque

# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass

#     @abstractmethod
#     def undo(self):
#         pass

# class Light:
#     def turn_on(self):
#         print("Свет включен")

#     def turn_off(self):
#         print("Свет выключен")

# class TV:
#     def turn_on(self):
#         print("Телевизор включен")

#     def turn_off(self):
#         print("Телевизор выключен")

# class AC:
#     def turn_on(self):
#         print("Кондиционер включен")

#     def turn_off(self):
#         print("Кондиционер выключен")

# class LightOnCommand(Command):
#     def __init__(self, light):
#         self.light = light

#     def execute(self):
#         self.light.turn_on()

#     def undo(self):
#         self.light.turn_off()

# class LightOffCommand(Command):
#     def __init__(self, light):
#         self.light = light

#     def execute(self):
#         self.light.turn_off()

#     def undo(self):
#         self.light.turn_on()

# class TVOnCommand(Command):
#     def __init__(self, tv):
#         self.tv = tv

#     def execute(self):
#         self.tv.turn_on()

#     def undo(self):
#         self.tv.turn_off()

# class TVOffCommand(Command):
#     def __init__(self, tv):
#         self.tv = tv

#     def execute(self):
#         self.tv.turn_off()

#     def undo(self):
#         self.tv.turn_on()

# class ACOnCommand(Command):
#     def __init__(self, ac):
#         self.ac = ac

#     def execute(self):
#         self.ac.turn_on()

#     def undo(self):
#         self.ac.turn_off()

# class ACOffCommand(Command):
#     def __init__(self, ac):
#         self.ac = ac

#     def execute(self):
#         self.ac.turn_off()

#     def undo(self):
#         self.ac.turn_on()

# class MacroCommand(Command):
#     def __init__(self, commands):
#         self.commands = commands

#     def execute(self):
#         for command in self.commands:
#             command.execute()

#     def undo(self):
#         for command in reversed(self.commands):
#             command.undo()

# class RemoteControl:
#     def __init__(self):
#         self.command_history = deque(maxlen=5)

#     def press_button(self, command):
#         command.execute()
#         self.command_history.append(command)

#     def press_undo(self):
#         if self.command_history:
#             command = self.command_history.pop()
#             command.undo()
#         else:
#             print("История пуста, отменять нечего.")

#     def show_history(self):
#         print("\nИстория команд:")
#         for i, cmd in enumerate(self.command_history, 1):
#             print(f"{i}. {cmd.__class__.__name__}")

# light = Light()
# tv = TV()
# ac = AC()

# remote = RemoteControl()

# light_on = LightOnCommand(light)
# tv_on = TVOnCommand(tv)
# ac_on = ACOnCommand(ac)

# light_off = LightOffCommand(light)
# tv_off = TVOffCommand(tv)
# ac_off = ACOffCommand(ac)

# turn_on_all = MacroCommand([light_on, tv_on, ac_on])
# turn_off_all = MacroCommand([light_off, tv_off, ac_off])

# remote.press_button(light_on)
# remote.press_button(tv_on)
# remote.press_button(ac_on)

# remote.show_history()

# remote.press_undo()
# remote.show_history()

# remote.press_button(turn_on_all)
# remote.press_undo()

"""
система обработки заказов в кафе

заказ:
приготовить кофе
приготовить чай
приготовить сэндвич
отменить заказ

инициатор менеджер
получатель кухня

Command: интерфейс, который предоставляет методы для выполнения
команды.

MakeCoffeeCommand, MakeTeaCommand, MakeSandwichCommand:
конкретные команды, которые представляют различные действия,
которые могут быть выполнены.

Kitchen: получатель, который содержит логику выполнения действий.

Waiter: инициатор, который создает и выполняет команды,
а также отменяет заказы, если необходимо.

"""
# from abc import ABC, abstractmethod


class Command(ABC):
    # интрефейс
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Kitchen:
    # получатель, выводит итог
    def make_coffee(self):
        print("Кофе готовится")

    def make_tea(self):
        print("Чай готовится")

    def make_sandwich(self):
        print("Сэндвич готовится")


class MakeCoffeeCommand(Command):
    # команда, вызывает метод кухни
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.make_coffee()

    def undo(self):
        print("Кофе отменен")


class MakeTeaCommand(Command):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.make_tea()

    def undo(self):
        print("Чай отменен")


class MakeSandwichCommand(Command):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.make_sandwich()

    def undo(self):
        print("Сэндвич отменен")


class Waiter:
    # оффициант, хранит историю, получает команды и вызывает их/отменяет
    def __init__(self):
        self.history = []

    def take_order(self, command: Command):
        # запускает метод у команд выше, а те вызовут кухню
        command.execute()
        self.history.append(command)

    def cancel_last_order(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
            # находит название последней команды и вызывает ее метод
        else:
            print("Нет заказов для отмены")


kitchen = Kitchen()

coffee_cmd = MakeCoffeeCommand(kitchen)

waiter = Waiter()

waiter.take_order(coffee_cmd)

waiter.cancel_last_order()
