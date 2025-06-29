"""
Создайте систему для клонирования документов, используя паттерн Prototype.
У вас должны быть следующие классы:

Document: абстрактный класс, представляющий документ. Он должен иметь метод
clone, который создает копию документа.
TextDocument и ImageDocument: конкретные классы документов, которые реализуют
метод clone.
DocumentManager: класс, который управляет документами. Он должен иметь методы
для добавления и клонирования документов.
Ваша задача - создать объекты TextDocument и ImageDocument, а затем
 использовать их для клонирования документов.
"""
from abc import ABC, abstractmethod
import copy


class Document(ABC):
    @abstractmethod
    def clone(self):
        pass


class TextDocument(Document):
    def __init__(self):
        self.name = None
        self.content = None

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'{self.name}: [{self.content}]'


class ImageDocument(Document):
    def __init__(self):
        self.name = None
        self.content = None

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'{self.name}: [{self.content}]'


class Manager(ABC):
    @abstractmethod
    def create_new_document(self, name, content):
        pass

    @abstractmethod
    def clone_document(self):
        pass


class DocumentManager(Manager):
    def __init__(self, document: Document):
        self.document = document

    def create_new_document(self, name, content):
        self.document.name = name
        self.document.content = content

    def clone_document(self):
        return self.document.clone()


text = TextDocument()
image = ImageDocument()

manager_text = DocumentManager(text)
manager_image = DocumentManager(image)

manager_text.create_new_document('Текстовый документ', 'текст')
manager_image.create_new_document('Документ с изображениями', 'картинка')


clone_text = manager_text.clone_document()
clone_image = manager_image.clone_document()

print('\nОригинальные документы')
print(text)
print(image)

print('\nКлонированные документы')
print(clone_text)
print(clone_image)

print('\nПроверка изменений')
clone_text.name = 'Клон'
clone_image.name = 'Клон'
print(clone_text)
print(clone_image)
print(text)
print(image)
