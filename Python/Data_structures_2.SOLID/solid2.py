from abc import ABC, abstractmethod
from collections import deque


class StackOperation(ABC):
    @abstractmethod
    def Execute(self, container: deque, item=None):
        pass


class AddStr(StackOperation):
    def Execute(self, container: deque, item):
        if len(container) == container.maxlen:
            print('Внимание стек полон!')
        else:
            container.append(item)
        print(f'Обновленный стек: {', '.join(map(str, container))}')


class Size(StackOperation):
    def Execute(self, container: deque, item=None):
        print(f'Стек сожержит {len(container)} элементов')


class DellLast(StackOperation):
    def Execute(self, container: deque, item=None):
        if container:
            container.pop()
            print(f'Обновленный стек: {', '.join(map(str, container))}') if len(container) > 0 else print('Значение удалено, стек пуст!')
        else:
            print('Стек пуст!')


class IsEmpty(StackOperation):
    def Execute(self, container: deque, item=None):
        if not container:
            print('Стек пуст!')
        elif len(container) == 2:
            print('Стек полон!')
        else:
            print('Стек не пуст!')


class Cleen(StackOperation):
    def Execute(self, container: deque, item=None):
        container.clear()
        print('Стек успешно отчищен!')


class ShowLastItem(StackOperation):
    def Execute(self, container: deque, item=None):
        if container:
            print(f'Последнее добавленное значение: {container[-1]}')
        else:
            print('Стек пуст!')


class Stack:
    def __init__(self, max=2):
        self.container = deque(maxlen=max)

    def GetConteiner(self):
        return self.container

    def StartWhithItem(self, actions: StackOperation, item=None):
        return actions.Execute(self.GetConteiner(), item)


class Menu:
    def __init__(self, item: Stack):
        self.item = item

    def run(self):
        count = 1
        while count:
            select = input('Какое действие вы хотите выпонить?\n'
                           '1-Добавить элемент в список\n'
                           '2-Выталкнуть строку из стека\n'
                           '3-Получить размер стека\n'
                           '4-Проверить пуст ли стек\n'
                           '5-Отчистить стек\n'
                           '6-Получить последнее значение без выталкивания\n'
                           'Для выхода из меню нажмите "8"\n'
                           'Укажите цифру: ')
            match select:
                case '1':
                    item.StartWhithItem(AddStr(), input('Укажите строку для '
                                                        'добавления: '))
                case '2':
                    item.StartWhithItem(DellLast())
                case '3':
                    item.StartWhithItem(Size())
                case '4':
                    item.StartWhithItem(IsEmpty())
                case '5':
                    item.StartWhithItem(Cleen())
                case '6':
                    item.StartWhithItem(ShowLastItem())
                case '8':
                    count = 0


item = Stack()
Menu = Menu(item)
Menu.run()
