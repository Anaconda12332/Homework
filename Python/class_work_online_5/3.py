"""
чат-комната
ChatRoom - субъект
User - обсервер
пользователь может подписать и отписать от чата в любой момент

Observer
Subject
ChatRoom
User
"""
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass


'''первый вариант'''
# class ChatRoom(Subject):
#     def __init__(self):
#         self._subscribers = []
#         # как сделать анонимным

'''второй вариант анон'''
# class ChatRoom(Subject):
#     def __init__(self):
#         self._subscribers = initialize__subscribers()
# ...
# def initialize__subscribers():
#     # общая функция инициализации?
#     return []


'''его вариант анон'''


class ChatRoom(Subject):
    def __init__(self):
        self._subscribers = []
        # как сделать анонимным

    def attach(self, observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)
        else:
            print('Ошибка добавления: Пользователь уже подписан!')

    def detach(self, observer):
        if observer in self._subscribers:
            self._subscribers.remove(observer)
        else:
            print('Ошибка удаления: Пользователь не подписан!')

    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)

    def set_message(self, message):
        print(f"Новое сообщение '{message}'")
        self.notify(message)


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} получил уведомление '{message}'")


telegram = ChatRoom()

user_1 = User('User 1')
user_2 = User('User 2')

telegram.attach(user_1)
telegram.attach(user_1)

telegram.attach(user_2)

telegram.set_message('Hi')
telegram.set_message('New message')

telegram.detach(user_2)
telegram.detach(user_2)

telegram.set_message('New message 2')
