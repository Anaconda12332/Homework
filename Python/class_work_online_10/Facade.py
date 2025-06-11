
"""
система бронирования путешествий
подсистемы:
    бронирование авиабилетов
    бронирование отеля
    бронирование автобуса
    стравки

FlightBooking book_flight()
HotelBooking book_hotel()
TransferService book_transfer()
InsuranceService buy_insurance()

TravelFacade: book_all()
"""


class FlightBooking:
    def book_flight(self):
        print("[FlightBooking]: Бронирование авиабилетов")
        return "Flight 123"


class HotelBooking:
    def book_hotel(self):
        print("[HotelBooking]: Бронирование отеля")
        return "Hotel ABC"


class TransferService:
    def book_transfer(self):
        print("[TransferService]: Бронирование трансфера")
        return "Transfer XYZ"


class InsuranceService:
    def buy_insurance(self):
        print("[InsuranceService]: Покупка страховки")
        return "Insurance 456"


class ClientNotification:
    def notify_client(self, message):
        print(f"[ClientNotification]: Уведомление клиента о статусе бронирования: {message}")


class TravelFacade:
    def __init__(self):
        self.flight_booking = FlightBooking()
        self.hotel_booking = HotelBooking()
        self.transfer_service = TransferService()
        self.insurance_service = InsuranceService()
        self.client_notification = ClientNotification()

    def book_all(self):
        print("[TravelFacade]: Начало бронирование путешествия")
        flight = self.flight_booking.book_flight()
        hotel = self.hotel_booking.book_hotel()
        transfer = self.transfer_service.book_transfer()
        insurance = self.insurance_service.buy_insurance()
        self.client_notification.notify_client(f' Бронирование завершено!\nСамолет: {flight}, Отель: {hotel}, Трансфер: {transfer}, Страховка: {insurance}')
        print('[TravelFacade] Бронирование завершено!')


travel = TravelFacade()
travel.book_all()
