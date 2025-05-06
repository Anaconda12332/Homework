class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def bring_out(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def add_str(self, item):
        print('Внимание! Максимальная длина стека: 4')
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            count = 0
            current = self.head
            while current.next:
                count += 1
                if count >= 3:
                    print('Стек переполнен!')
                    break
                else:
                    current = current.next
            if not current.next:
                current.next = new_node
        self.bring_out()

    def off_last(self):
        if not self.head:
            print('Стек пуст!')
        else:
            current = self.head
            if not current.next:
                self.head = None
            else:
                while current and current.next.next:
                    current = current.next
                current.next = None
            self.bring_out()

    def size(self):
        if not self.head:
            print('Стек пуст!')
        else:
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            print(f'Стек сожержит {count} элементов!')

    def is_empty(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        if not self.head:
            print('Стек пуст!')
        elif count == 4:
            print('Стек полон!')
        else:
            print('Стек не пуст!')

    def cleen(self):
        self.head = None
        print('Стек успешно отчищен!')
        self.bring_out()

    def get(self):
        if self.head:
            current = self.head
            while current.next.next:
                current = current.next
            current = current.next
            print(f'Последнее добавленное значение: {current.data}')
        else:
            print('Стек пуст!')


item = LinkedList()

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
            item.add_str(input('Укажите строку для добавления: '))
        case '2':
            item.off_last()
        case '3':
            item.size()
        case '4':
            item.is_empty()
        case '5':
            item.cleen()
        case '6':
            item.get()
        case '8':
            count = 0
