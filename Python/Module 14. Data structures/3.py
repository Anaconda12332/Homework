from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def __str__(self):
        return ', '.join(map(str, self.container))

    def add_str(self, item):
        self.container.append(item)
        print(f'Обновленный стек: {self}')

    def size(self):
        print(f'Стек сожержит {len(self.container)} элементов')

    def off_last(self):
        if self.container:
            self.container.pop()
            print(f'Обновленный стек: {self}') if len(
                self.container) > 0 else print('Значение удалено, стек пуст!')
        else:
            print('Стек пуст!')

    def is_empty(self):
        if not self.container:
            print('Стек пуст!')
        else:
            print('Стек не пуст!')

    def cleen(self):
        self.container.clear()
        print('Стек успешно отчищен!')

    def show(self):
        if self.container:
            print(f'Последнее добавленное значение: {self.container[-1]}')
        else:
            print('Стек пуст!')


item = Stack()
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
            item.show()
        case '8':
            count = 0
