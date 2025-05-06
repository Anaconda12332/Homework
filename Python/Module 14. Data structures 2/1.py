class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            current = None
            for i in iterable:
                node = Node(i)
                if not self.head:
                    self.head = node
                    current = self.head
                else:
                    current.next = node
                    current = node

    def bring_out(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next and current.data != data:
                current = current.next
            if not current.next and current.data != data:
                current.next = new_node
                print(f'Число {data} добавлено в список!')
            else:
                print(f'Число {data} уже есть в списке!')
        self.bring_out()

    def dell_all_item(self, key):
        if not self.head:
            print('Список пуст')
            return
        else:
            check = 0
            while self.head and self.head.data == key:
                self.head = self.head.next
                check = 1
            current = self.head
            while current and current.next:
                if current.next.data == key:
                    current.next = current.next.next
                    check = 1
                else:
                    current = current.next
            if check == 0:
                print(f'Числа {key} нет в списке!')
        self.bring_out()

    def show(self):
        if not self.head:
            print('Список пуст')
        else:
            answer = input('Показать список с конца - 1\n'
                           'Показать список с начала - 2\nУкажите цифру: ')
            if answer == '1':
                previous = None
                current = self.head
                while current:
                    next_node = current.next
                    current.next = previous
                    previous = current
                    current = next_node
                self.head = previous
                while previous:
                    print(previous.data, end=" -> ")
                    previous = previous.next
                print("None")
            elif answer == '2':
                self.bring_out()
            else:
                print('Некорректный ввод!')

    def check(self, key):
        if not self.head:
            print('Список пуст')
        else:
            current = self.head
            while current:
                if current.data == key:
                    print(f'Число {key} есть в списке!')
                    break
                current = current.next
            if current is None:
                print(f'Числа {key} нет в списке!')

    def replace(self, key):
        if not self.head:
            print('Список пуст')
        else:
            answer = int(input(f'Укажите число на которое нужно '
                               f'заменить число {key}: '))
            select = input('Заменить все вхождения:? - 1\n'
                           'Заменить только первое вхождение - 2\n'
                           'Укажите цифру: ')

            if select == '1':
                current = self.head
                while current:
                    if current.data == key:
                        current.data = answer
                    current = current.next
            elif select == '2':
                current = self.head
                while current:
                    if current.data == key:
                        current.data = answer
                        break
                    current = current.next
            self.bring_out()


user_list = LinkedList(list(map(int, (input('Укажите числа через '
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
            user_list.append(int(input('Укажите число для добавления: ')))
        case '2':
            user_list.dell_all_item(int(input('Укажите число для удаления: ')))
        case '3':
            user_list.show()
        case '4':
            user_list.check(int(input('Укажите число для проверки: ')))
        case '5':
            user_list.replace(int(input('Укажите число, которое хотите '
                                        'заменить: ')))
        case '7':
            count = 0
