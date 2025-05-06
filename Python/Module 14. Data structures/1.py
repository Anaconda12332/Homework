from collections import deque


class UserList:
    def __init__(self, user_list):
        self.container = deque()
        self.user_list = user_list
        for i in self.user_list:
            self.container.append(i)

    def __str__(self):
        return ', '.join(map(str, self.container))

    def appends(self, item):
        if item in self.container:
            print(f"Добавленное число {item} уже существует в списке!")
        else:
            self.container.append(item)
        print(f'Обновленный список: {self}')

    def dell_item(self, item):
        self.container = deque([x for x in self.container if x != item])
        print(f'Все вхождения числа {item} были удалены!\n'
              f'Обновленный список: {self}')

    def show(self):
        answer = input('Показать список с конца - 1\n'
                       'Показать список с начала - 2\nУкажите цифру: ')
        if answer == '1':
            new_list = deque()
            revers = []
            for i in self.container:
                new_list.append(i)
            while new_list:
                revers.append(new_list.pop())
            print(f'Развернутый список: {', '.join(map(str, revers))}')
        elif answer == '2':
            print(f'Список: {self}')
        else:
            print('Некорректный ввод!')

    def check(self, item):
        if item in self.container:
            print(f'Число {item} есть в списке!')
        else:
            print(f'Числа {item} нет в списке!')

    def replace(self, item):
        new_list = [*self.container]

        answer = int(input(f'Укажите число на которое нужно '
                           f'заменить число {item}: '))
        select = input('Заменить все вхождения:? - 1\n'
                       'Заменить только первое вхождение - 2\nУкажите цифру: ')

        if select == '1':
            for i in new_list:
                if i == item:
                    new_list[new_list.index(item)] = answer
        elif select == '2':
            new_list[new_list.index(item)] = answer
        self.container.clear()
        for i in new_list:
            self.container.append(i)
        print(f'Обновленный список: {self}')


listU = UserList(list(map(int, (input('Укажите числа через '
                                      'пробел: ').split()))))


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
            listU.appends(int(input('Укажите число для добавления: ')))
        case '2':
            listU.dell_item(int(input('Укажите число для удаления: ')))
        case '3':
            listU.show()
        case '4':
            listU.check(int(input('Укажите число для проверки: ')))
        case '5':
            listU.replace(int(input('Укажите число, которое хотите '
                                    'заменить: ')))
        case '7':
            count = 0
