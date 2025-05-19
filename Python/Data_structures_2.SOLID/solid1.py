from abc import ABC, abstractmethod
from collections import deque


class ListOperation(ABC):
    @abstractmethod
    def Execute(self, container: deque, item=None, extra=None):
        pass


class Appends(ListOperation):
    def Execute(self, container: deque, item, extra=None):
        if item in container:
            print(f"Добавленное число {item} уже существует в списке!")
        else:
            container.append(item)
        print(f'Обновленный список: {', '.join(map(str, container))}')


class DellItem(ListOperation):
    def Execute(self, container: deque, item, extra=None):
        container2 = deque([x for x in container if x != item])
        container.clear()
        container.extend(container2)
        print(f'Все вхождения числа {item} были удалены!\n'
              f'Обновленный список: {', '.join(map(str, container))}')


class Show(ListOperation):
    def Execute(self, container: deque, item, extra=None):

        if item == 1:
            new_list = deque()
            revers = []
            for i in container:
                new_list.append(i)
            while new_list:
                revers.append(new_list.pop())
            print(f'Развернутый список: {', '.join(map(str, revers))}')
        elif item == 2:
            print(f'Список: {', '.join(map(str, container))}')
        else:
            print('Некорректный ввод!')


class Check(ListOperation):
    def Execute(self, container: deque, item, extra=None):

        if item in container:
            print(f'Число {item} есть в списке!')
        else:
            print(f'Числа {item} нет в списке!')


class Replace(ListOperation):
    def Execute(self, container: deque, item, extra):
        new_value, replase_value = extra
        new_list = [*container]

        if replase_value == '1':
            for i in new_list:
                if i == item:
                    new_list[new_list.index(item)] = new_value
        elif replase_value == '2':
            new_list[new_list.index(item)] = new_value
        container.clear()
        for i in new_list:
            container.append(i)
        print(f'Обновленный список: {', '.join(map(str, container))}')


class UserList:
    def __init__(self, user_list):
        self.container = deque()
        self.user_list = user_list
        for i in self.user_list:
            self.container.append(i)

    def GetConteiner(self):
        return self.container

    def Start(self, actions: ListOperation, item=None, extra=None):
        return actions.Execute(self.GetConteiner(), item, extra)


class Menu:
    def __init__(self, user_list: UserList):
        self.user_list = user_list

    def run(self):
        count = 1
        while count:
            select = input('Какое действие вы хотите выпонить?\n'
                           '1-Добавить элемент в список\n'
                           '2-Удалить все вхождения элемента из списка\n'
                           '3-Показать список\n'
                           '4-Проверить есть ли элемент в списке\n'
                           '5-Заменить элемент списка\n'
                           'Для выхода из меню нажмите "7"\n'
                           'Укажите цифру: ')
            match select:
                case '1':
                    listU.Start(Appends(), int(input('Укажите число '
                                                     'для добавления: ')))
                case '2':
                    listU.Start(DellItem(), int(input('Укажите число для '
                                                      'удаления: ')))
                case '3':
                    listU.Start(Show(), int(input('Показать список с конца - 1\n'
                                                  'Показать список с начала - 2\n'
                                                  'Укажите цифру: ')))
                case '4':
                    listU.Start(Check(), int(input('Укажите число для '
                                                   'проверки: ')))
                case '5':
                    item = int(input('Укажите число, которое '
                                     'хотите заменить: '))
                    new_value = int(input(f'Укажите число на которое нужно '
                                          f'заменить число {item}: '))
                    replase_value = input('Заменить все вхождения:? - 1\n'
                                          'Заменить только первое вхождение '
                                          '- 2\nУкажите цифру: ')                    
                    listU.Start(Replace(), item, extra=(new_value, replase_value))
                case '7':
                    count = 0


listU = UserList(list(map(int, (input('Укажите числа через '
                                      'пробел: ').split()))))
Menu = Menu(listU)
Menu.run()
