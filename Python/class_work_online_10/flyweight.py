
"""
система отображения стикеров в мессенджере

10 стикеров:
отправитель
получатель
метка времени
графика

внутреннее состояние: изображение, имя
внешнее состояние: кто отправлял, кому, когда

StickerType внутр
StickerFactory хранит и переиспользует StickerType
StickerMessage содержит ссылку на StickerType внеш

"""
from datetime import datetime


class StickerType:
    def __init__(self, image, name):
        self.image = image
        self.name = name

    def sent(self, user_name, target_user_name, time):
        print(f"Отправален стикер: {self.name} {self.image} от {user_name} к {target_user_name} в {time}")


class StickerFactory:
    _types = {}

    @classmethod
    def get_shape_type(cls, shape_name, image):
        key = (shape_name, image)
        if key not in cls._types:
            cls._types[key] = StickerType(shape_name, image)
            print(f"[StickerFactory] новый тип {shape_name} {image}")
        return cls._types[key]


class StickerMessage:
    def __init__(self, user_name, target_user_name, time, shape_type: StickerType):
        self.user_name = user_name
        self.target_user_name = target_user_name
        self.time = time
        self.shape_type = shape_type

    def send(self):
        self.shape_type.sent(self.user_name, self.target_user_name, self.time)


class Chat:
    def __init__(self):
        self.stickers = []

    def add_sticker(self, user_name, target_user_name, shape_name, image):
        shape_type = StickerFactory.get_shape_type(shape_name, image)
        date = datetime.now()
        time = datetime.time(date)
        sticker = StickerMessage(user_name, target_user_name, time, shape_type)
        self.stickers.append(sticker)

    def send_all(self):
        for sticker in self.stickers:
            sticker.send()


chat = Chat()
chat.add_sticker("Вася", "Петя", "ромашка", "name_one.jpg")
chat.add_sticker("Вася", "Петя", "ромашка", "name_one.jpg")
chat.add_sticker("Петя", "Вася", "кошка", "name_three.jpg")
chat.add_sticker("Петя", "Вася", "собака", "name_three.jpg")
chat.add_sticker("Вася", "Петя", "сердце", "ass.jpg")

chat.send_all()
