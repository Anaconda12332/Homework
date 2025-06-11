"""
система расчета стоимости билетов
у билета базовая цена
    vip
    страховка
    срочная покупка
к цене добавляются надбавки

интерфейс Ticket
class BaseTicket
    get_price
    get_description

декораторы-наценки
наследуются от интерфейса Ticket с ссылкой на объект Ticket
VipAccessDecorator - цена * 1.5 с вип доступом
InsuranceDecorator - цена + 100 со страховкой
LastMinuteDecorator - цена * 1.3 за срочную покупку
"""


class Ticket:
    def get_price(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError


class BaseTicket(Ticket):
    def __init__(self):
        self.price = 500

    def get_price(self):
        return self.price

    def get_description(self):
        return "Базовый билет"


class TicketDecorator(Ticket):
    def __init__(self, wrapped: Ticket):
        self.wrapped = wrapped

    def get_price(self):
        return self.wrapped.get_price()

    def get_description(self):
        return self.wrapped.get_description()


class VipAccessDecorator(TicketDecorator):
    def get_price(self):
        return self.wrapped.get_price() * 1.5

    def get_description(self):
        return self.wrapped.get_description() + " с вип доступом"


class InsuranceDecorator(TicketDecorator):
    def get_price(self):
        return self.wrapped.get_price() + 100

    def get_description(self):
        return self.wrapped.get_description() + " со страховкой"


class LastMinuteDecorator(TicketDecorator):
    def get_price(self):
        return self.wrapped.get_price() * 1.3

    def get_description(self):
        return self.wrapped.get_description() + " со срочной покупкой"


tiket = BaseTicket()
decor = VipAccessDecorator(tiket)
decor = InsuranceDecorator(decor)
decor = LastMinuteDecorator(decor)

print(decor.get_price(), decor.get_description())

# print(tiket.get_price(), tiket.get_description())
