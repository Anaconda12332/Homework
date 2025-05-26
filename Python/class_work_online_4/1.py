"""
платежная система

банковская карта
электронный кошелек
криптовалюта

Создайте интерфейс стратегии PaymentStrategy с методов pay(amount: float)
Реализуйте три класса-стратегии:

CreditCardPayment
EWalletPayment
CryptoPayment

Релизуйте класс Order, который будет использовать объект стратегии для выполнения оплаты
"""
# from abc import ABC, abstractmethod


# class PaymentStrategy(ABC):
#     @abstractmethod
#     def pay(self, price: float) -> float:
#         pass


# class CreditCardPayment(PaymentStrategy):
#     def pay(self, price: float) -> float:
#         return f'Оплата совершена с помощью банковской карты!\nСумма покупки: {price}'


# class EWalletPayment(PaymentStrategy):
#     def pay(self, price: float) -> float:
#         return f'Оплата совершена с помощью электронного кошелька!\nСумма покупки: {price}'


# class CryptoPayment(PaymentStrategy):
#     def pay(self, price: float) -> float:
#         return f'Оплата совершена с помощью криптоволюты!\nСумма покупки: {price}'


# class Order:
#     def __init__(self, price: float, delivery_strategy: PaymentStrategy):
#         self.price = price
#         self.delivery_strategy = delivery_strategy

#     def run(self) -> float:
#         return self.delivery_strategy.pay(self.price)


# order1 = Order(20, CreditCardPayment())
# order2 = Order(221, EWalletPayment())
# order3 = Order(132, CryptoPayment())
 
# print(order1.run())
# print(order2.run())
# print(order3.run())


from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, price: float) -> float:
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, price: float) -> float:
        return f'Оплата совершена с помощью банковской карты!\nСумма покупки: {price}'


class EWalletPayment(PaymentStrategy):
    def pay(self, price: float) -> float:
        return f'Оплата совершена с помощью электронного кошелька!\nСумма покупки: {price}'


class CryptoPayment(PaymentStrategy):
    def pay(self, price: float) -> float:
        return f'Оплата совершена с помощью криптоволюты!\nСумма покупки: {price}'


class Order:
    def __init__(self, price: float, delivery_strategy: PaymentStrategy):
        self.price = price
        self.delivery_strategy = delivery_strategy

    def run(self) -> float:
        return self.delivery_strategy.pay(self.price)

    def set_payment_startegy(self, new_stratage):
        self.delivery_strategy = new_stratage


order1 = Order(20, CreditCardPayment())
order2 = Order(221, EWalletPayment())
order3 = Order(132, CryptoPayment())

print(order1.run())
print(order2.run())
print(order3.run())

order2.set_payment_startegy(CryptoPayment())
print(order2.run())
