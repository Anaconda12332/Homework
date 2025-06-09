"""
банкомат/банковская карта

активна
заблокирована
истек срок действия

Satate

оплата покупки
пополнение баланса
проверка баланса
блок/анлок карты

Сосотояния
ActiveState - нормально работает
BlockedState - нельзя совершать операции
ExpiredState - можно смотреть баланс
InactiveState - карта еще не активирована

CardState
pay(amount)
top_up(amount)
check_balance()
block()
unblock()

BankCard
хранит баланс
ссылку на текущее состояние state
методы делегируют действия текущему состоянию
"""
from abc import ABC, abstractmethod


class CardState(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def top_up(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def block(self):
        pass

    @abstractmethod
    def unblock(self):
        pass


class ActiveState(CardState):
    def __init__(self, card):
        self._card = card

    def pay(self, amount):
        if self._card.balance >= amount:
            self._card.balance -= amount
            print("Оплата прошла успешно")
        else:
            print("Недостаточно средств на счете")

    def top_up(self, amount):
        self._card.balance += amount
        print(f"Баланс пополнен на {amount} рублей")

    def check_balance(self):
        print(f"Ваш баланс: {self._card.balance} рублей")

    def block(self):
        self._card.change_state(BlockedState)
        print("Карта заблокирована")

    def unblock(self):
        self._card.change_state(ActiveState)
        print("Карта разблокирована")


class BlockedState(CardState):
    def __init__(self, card):
        self._card = card

    def pay(self, amount):
        print("Операция не может быть выполнена в текущем состоянии")

    def top_up(self, amount):
        print("Операция не может быть выполнена в текущем состоянии")

    def check_balance(self):
        print("Баланс не может быть проверен в текущем состоянии")

    def block(self):
        print("Карта уже заблокирована")

    def unblock(self):
        self._card.change_state(ActiveState)
        print("Карта разблокирована")


class ExpiredState(CardState):
    def __init__(self, card):
        self._card = card

    def pay(self, amount):
        print("Операция не может быть выполнена в текущем состоянии")

    def top_up(self, amount):
        print("Операция не может быть выполнена в текущем состоянии")

    def check_balance(self):
        print(f"Ваш баланс: {self._card.balance} рублей")

    def block(self):
        self._card.change_state(BlockedState)
        print("Карта заблокирована")

    def unblock(self):
        self._card.change_state(ActiveState)
        print("Карта перевыпущенна")


class InactiveState(CardState):
    def __init__(self, card):
        self._card = card

    def pay(self, amount):
        print("Карта еще не активирована")

    def top_up(self, amount):
        print("Карта еще не активирована")

    def check_balance(self):
        print("Карта еще не активирована")

    def block(self):
        self._card.change_state(BlockedState)
        print("Карта заблокирована")

    def unblock(self):
        self._card.change_state(ActiveState)
        print("Карта активирована")


class BankCard:
    def __init__(self):
        self.balance = 0
        self.current_state: CardState = ActiveState(self)

    def change_state(self, new_state: type[CardState]):
        if isinstance(new_state, CardState):
            self.current_state = new_state(self)
        else:
            print("Некорректное состояние")

    def pay(self, amount):
        self.current_state.pay(amount)

    def top_up(self, amount):
        self.current_state.top_up(amount)

    def check_balance(self):
        self.current_state.check_balance()

    def block(self):
        self.current_state.block()

    def unblock(self):
        self.current_state.unblock()


card = BankCard()

print('State: Нормальное состояние')
card.pay(100)
card.top_up(500)
card.pay(100)
card.check_balance()
card.block()
print("========================================\n")

print('State: Заблокированное состояние')
card.pay(100)
card.top_up(500)
card.check_balance()
card.block()
card.unblock()
card.pay(100)
print("========================================\n")

print('State: Срок действия истек')
card.change_state(ExpiredState)
card.pay(100)
card.top_up(500)
card.check_balance()
card.unblock()
card.pay(100)
print("========================================\n")

print('State: Карта не активирована')
card.change_state(InactiveState)
card.pay(100)
card.top_up(500)
card.check_balance()
card.unblock()
card.pay(100)
print("========================================\n")
card.change_state('Ошибка')
