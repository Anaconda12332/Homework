from abc import ABC, abstractmethod
import json


class Kitchen:
    def __init__(self):
        self.mediator = None
        self.hotdog_one = {
            "bread": 1,
            "tomato": 1,
            "meat": 1,
            "cheese": 1
        }
        self.hotdog_two = {
            "bread": 1,
            "tomato": 1,
            "meat": 1,
            "cheese": 1,
            "ketchup": 1,
            "mayonnaise": 1
        }
        self.hotdog_three = {
            "bread": 1,
            "tomato": 1,
            "meat": 1,
            "cheese": 1,
            "ketchup": 1,
            "salad": 1
        }

    def set_mediator(self, mediator):
        self.mediator = mediator

    def new_ingridients(self, name, ingredient):
        if ingredient:
            new_ingredient = self.__dict__[name].copy()
            new_ingredient.update(ingredient)

            for key in ingredient.keys():
                if key in self.__dict__[name]:
                    new_ingredient[key] += 1
            return new_ingredient

    def preset_hotdog_one(self, user_ingredient=None):
        if user_ingredient:
            result = self.new_ingridients('hotdog_one', user_ingredient)
            self.mediator.notify("Kitchen", "hotdog_one", result)
        else:
            self.mediator.notify("Kitchen", "hotdog_one", self.hotdog_one)

    def preset_hotdog_two(self, user_ingredient=None):
        if user_ingredient:
            result = self.new_ingridients('hotdog_two', user_ingredient)
            self.mediator.notify("Kitchen", "hotdog_two", result)
        else:
            self.mediator.notify("Kitchen", "hotdog_two", self.hotdog_two)

    def preset_hotdog_three(self, user_ingredient=None):
        if user_ingredient:
            result = self.new_ingridients('hotdog_three', user_ingredient)
            self.mediator.notify("Kitchen", "hotdog_three", result)
        else:
            self.mediator.notify("Kitchen", "hotdog_three", self.hotdog_three)

    def user_hotdog(self, ingredients):
        self.mediator.notify("Kitchen", "user_hotdog", ingredients)


class Storage:
    def __init__(self):
        self.mediator = None
        self.storage = {
            "bread": 12,
            "tomato": 12,
            "meat": 12,
            "cheese": 12,
            "ketchup": 12,
            "mayonnaise": 12,
            "sauce": 12,
            "salad": 12
        }

        self.buy_groceries = {}

    def set_mediator(self, mediator):
        self.mediator = mediator

    def minus(self, args):
        if args:
            for item in args:
                if item in self.storage and self.storage[item] >= args[item]:
                    self.storage[item] -= args[item]
                else:
                    raise ValueError(f'В магазине недостаточно {item}!')

    def examination(self):
        for item in self.storage:
            if self.storage[item] <= 5:
                self.buy_groceries[item] = self.storage[item]
        if self.buy_groceries:
            self.mediator.notify("Other_notification", f'В магазине заканчиваются: {self.buy_groceries}\n')


class WriteJson:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def write(self, file_name, event, ingredients):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump({"event": event, "ingredients": ingredients}, file, indent=4)


class Price:
    def __init__(self):
        self.mediator = None

        self.hotdog_one = 100
        self.hotdog_two = 120
        self.hotdog_three = 130
        self.user_hotdog = 100

        self.bread = 5
        self.tomato = 5
        self.meat = 10
        self.cheese = 5
        self.ketchup = 5
        self.mayonnaise = 5
        self.sauce = 5
        self.salad = 5

        self.result = 0

    def set_mediator(self, mediator):
        self.mediator = mediator

    def calc(self, event, args):
        if args:
            for item in args:
                if item in self.__dict__:
                    self.result += self.__dict__[item]
        self.result += self.__dict__[event]

    def sale(self, sale):
        if isinstance(sale, list):
            self.result -= self.result * 0.1

    def clear(self):
        self.result = 0


class Pay(ABC):
    @abstractmethod
    def pay(self, price):
        pass


class Credit(Pay):
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def pay(self, price):
        self.mediator.notify("Other_notification", f"Оплата картой на {price}р принята\n")


class Cash(Pay):
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def pay(self, price):
        self.mediator.notify("Other_notification", f"Оплата наличными на {price}р принята\n", price)


class Accounting:
    def __init__(self):
        self.mediator = None

        self.hotdogs = 0
        self.profit = 0

    def set_mediator(self, mediator):
        self.mediator = mediator

    def account(self, hotdog, price):
        self.hotdogs += len(hotdog) if isinstance(hotdog, list) else 1
        self.profit += price

    def show_account(self):
        self.mediator.notify("Other_notification", f'Отчет:\nПродано: {self.hotdogs} хот догов\nПрибыль: {self.profit} рублей\n')


class Notification:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def retern(self, sender, event, args=None):
        if sender == 'Kitchen':
            if args:
                if event == "user_hotdog":
                    print(f'Пользовательский хот дог "{event}" с ингридиентами {args} приготовлен\n')
                else:
                    print(f'Хот дог "{event}" с доп ингридиентами {args} приготовлен\n')
            else:
                print(f'Хот дог "{event}" приготовлен\n')
        else:
            print(event)


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event=None, args=None):
        pass


class KafeMediator(Mediator):
    def __init__(self, kitchen, storage, price, write_json, accounting, credit, cash, notification, order):
        self.kitchen = kitchen
        self.storage = storage
        self.price = price
        self.write_json = write_json
        self.accounting = accounting
        self.cash = cash
        self.credit = credit
        self.notification = notification
        self.order = order

    def notify(self, sender, event=None, args=None):
        if sender == "Order":
            func = getattr(self.kitchen, args[0])
            func(args[1])

        elif sender == "Order_payment":
            self.price.sale(self.order.last_order)
            self.accounting.account(self.order.last_order, self.price.result)
            self.__dict__[args].pay(self.price.result)
            self.price.clear()

        elif sender == 'Order_show_account':
            self.accounting.show_account()

        elif sender == 'Order_show_storage':
            self.notification.retern('Order_show_storage', f'Продуктов в магазине:\n{self.storage.storage}')

        elif sender == "Kitchen":
            self.storage.minus(args)
            self.notification.retern(sender, event, self.order.user_ingredients)
            self.storage.examination()
            self.write_json.write('LastOrder', event, args)
            self.price.calc(event, self.order.user_ingredients)

        elif sender == "Other_notification":
            self.notification.retern(sender, event)


class Order:
    def __init__(self):
        self.mediator = None
        self.last_order = None
        self.user_ingredients = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def buy_hotdog(self, name, user_ingredients=None):
        self.last_order = name
        self.user_ingredients = user_ingredients

        if isinstance(name, list):
            for item in name:
                self.mediator.notify("Order", "Order", args=[item, user_ingredients])
        else:
            self.mediator.notify("Order", "Order", args=[name, user_ingredients])

    def payment_method(self, method):
        self.mediator.notify("Order_payment", "Payment", method)

    def show_account(self):
        self.mediator.notify("Order_show_account")

    def show_storage(self):
        self.mediator.notify('Order_show_storage')


kitchen = Kitchen()
storage = Storage()
price = Price()
writeJson = WriteJson()
accounting = Accounting()
credit = Credit()
cash = Cash()
notification = Notification()
order = Order()

kafeMediator = KafeMediator(kitchen, storage, price, writeJson, accounting, credit, cash, notification, order)

kitchen.set_mediator(kafeMediator)
storage.set_mediator(kafeMediator)
price.set_mediator(kafeMediator)
writeJson.set_mediator(kafeMediator)
accounting.set_mediator(kafeMediator)
credit.set_mediator(kafeMediator)
cash.set_mediator(kafeMediator)
notification.set_mediator(kafeMediator)
order.set_mediator(kafeMediator)

order.buy_hotdog("preset_hotdog_one")
order.payment_method("credit")

order.buy_hotdog("preset_hotdog_two")
order.payment_method("credit")

order.buy_hotdog("preset_hotdog_three")
order.payment_method("credit")

order.buy_hotdog("preset_hotdog_one", {'ketchup': 1, 'cheese': 1, 'salad': 1})
order.payment_method('cash')

order.buy_hotdog("preset_hotdog_two", {'tomato': 1, 'cheese': 1, 'salad': 1})
order.payment_method('cash')

order.buy_hotdog(['preset_hotdog_one', 'preset_hotdog_two', 'preset_hotdog_three'])
order.payment_method('cash')

order.buy_hotdog("user_hotdog", {'bread': 1, 'meat': 1, 'tomato': 1, 'cheese': 1, 'salad': 1})
order.payment_method('cash')

order.show_account()
order.show_storage()
