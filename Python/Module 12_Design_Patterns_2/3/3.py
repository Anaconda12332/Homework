'''
Создайте приложение для работы в библиотеке. Оно
должно оперировать следующими сущностями: Книга,
Библиотекарь, Читатель. Приложение должно позволять
вводить, удалять, изменять, сохранять в файл, загружать из
файла, логгировать действия, искать информацию
(результаты поиска выводятся на экран или файл) о сущностях.
При реализации используйте максимально возможное
количество паттернов проектирования.
'''
from abc import ABC, abstractmethod
import json
import time


class Books:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        name, author = book
        if name not in self.books:
            self.books[name] = author
        else:
            print("Книга уже существует!")

    def remove_book(self, book_name):
        if book_name in self.books:
            del self.books[book_name]
        else:
            print("Книга не найдена!")

    def change_book(self, book):
        book_name, new_author = book
        if book_name in self.books:
            self.books[book_name] = new_author
        else:
            print("Книга не найдена!")

    def search_book(self, book_name):
        if book_name in self.books:
            print(f"Книга найдена: {self.books[book_name]}")
        else:
            print("Книга не найдена!")


class BibliotekarMediator(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass

    @abstractmethod
    def change_book(self, book):
        pass

    @abstractmethod
    def search_book(self, book):
        pass

    @abstractmethod
    def show_books(self):
        pass

    @abstractmethod
    def get_books(self):
        pass

    @abstractmethod
    def load_books(self, new_books):
        pass


class Bibliotekar(BibliotekarMediator):
    def __init__(self):
        self.book = Books()
        self.logger = logger()

    def add_book(self, book):
        self.book.add_book(book)
        self.logger.log(self.__class__.__name__, 'Добавлена новая книга')

    def remove_book(self, book):
        self.book.remove_book(book)
        self.logger.log(self.__class__.__name__, 'Удалена книга')

    def change_book(self, book):
        self.book.change_book(book)
        self.logger.log(self.__class__.__name__, 'Изменена книга')

    def search_book(self, book):
        self.book.search_book(book)
        self.logger.log(self.__class__.__name__, 'Выполнен поиск книги')

    def show_books(self):
        for book_name, author in self.book.books.items():
            print(f"Название книги: {book_name}, Автор: {author}")
        print()
        self.logger.log(self.__class__.__name__, 'Показаны все книги')

    def get_books(self):
        self.logger.log(self.__class__.__name__, 'Сделан запрос данных')
        return self.book.books

    def load_books(self, new_books):
        self.logger.log(self.__class__.__name__, 'Список книг заменен')
        if new_books:
            self.book.books = new_books


class FileMeneger(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class JsonFile(FileMeneger):
    def __init__(self):
        self.logger = logger()

    def save(self, book):
        with open('3/books.json', 'w', encoding='utf-8') as file:
            json.dump(book, file, ensure_ascii=False, indent=4)
        self.logger.log(self.__class__.__name__, 'Данные сохранены в файл')

    def load(self, file):
        with open(file, 'r', encoding='utf-8') as file:
            new_book = json.load(file)
        self.logger.log(self.__class__.__name__, 'Данные загружены из файла')
        return new_book


class logger(ABC):
    def log(self, name, message):
        with open('3/log.txt', 'a', encoding='utf-8') as file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f'[{timestamp}][{name}]: {message}\n')


class Reader:
    def __init__(self, mediator: BibliotekarMediator):
        self.mediator = mediator

    def add_book(self, book):
        self.mediator.add_book(book)

    def remove_book(self, book):
        self.mediator.remove_book(book)

    def change_book(self, book):
        self.mediator.change_book(book)

    def search_book(self, book):
        self.mediator.search_book(book)

    def show_books(self):
        self.mediator.show_books()


mediator = Bibliotekar()
reader = Reader(mediator)

json_format = JsonFile()

reader.add_book(("Книга1", "Автор1"))
reader.add_book(("Книга2", "Автор2"))
reader.add_book(("Книга3", "Автор3"))
reader.show_books()

json_format.save(mediator.get_books())

reader.remove_book(("Книга2"))
reader.show_books()

reader.change_book(('Книга1', "Автор4"))
reader.show_books()

reader.search_book("Книга3")

mediator.load_books(json_format.load('3/books.json'))
reader.show_books()
