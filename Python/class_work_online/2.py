from collections import deque


class Orders:
    def __init__(self):
        self.container = deque(maxlen=5)
        self.all_orders = 0
        self.normal_orders = 0
        self.priority_orders = 0

    def add_order(self, item):
        self.all_orders += 1
        self.normal_orders += 1
        self.container.append(item)

    def add_priority_oder(self, item):
        self.all_orders += 1
        self.priority_orders += 1
        self.container.appendleft(item)

    def server_order(self):
        while self.container:
            container = self.container.popleft()
            self.normal_orders -= 1
            self.all_orders -= 1
            print(f'Обслуживается {container}')
            print(f'Колличество  оставшихся заказов: {self.all_orders}')

            if self.priority_orders > 0:
                self.priority_orders -= 1
                print(f'Колличество оставшихся приоритетных заказов: '
                      f'{self.priority_orders}')

    def show_orders(self):
        if self.container:
            print(f'Очередь составляет - {len(self.container)} человека')
            print(f'Колличество заказов: {self.all_orders}')
            print(f'Колличество приоритетных заказов: {self.priority_orders}')
        else:
            print('Очередь пуста!')


person = Orders()
person.add_order('Anna')
person.add_order('Alice')
person.add_order('Bob')

person.add_priority_oder('Oliver')

person.show_orders()

person.server_order()
person.show_orders()
