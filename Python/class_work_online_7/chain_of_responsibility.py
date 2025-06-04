"""
фильтрация и модерация пользовательского контента в социальной сети

публикуют текстовые сообщения
цепочка фильтров
проверка на цензуру - маскировка плохих слов
проверка на спам
проверка на размер текста - заблокировать слишком большие сообщения
проверка на чувствительные данные

абстрактный фильтр ContentFilter
конкретные фильтры
    ProfanityFilter, SpamFilter, LengthFilter, PersonalDataFilter

"""
import re


class ContentFilter:
    def __init__(self):
        self._next_filter = None

    def set_next(self, next_filter):
        self._next_filter = next_filter
        return next_filter

    def handler(self, message):
        if self._next_filter:
            return self._next_filter.handler(message)
        return message


class ProfanityFilter(ContentFilter):
    def handler(self, message):
        print('Проверка на цензуру')
        bad_words = ['плохое', 'слово']

        def mask_word(match):
            word = match.group()
            return '*' * len(word)

        for word in bad_words:
            message = re.sub(rf'\b{word}\b', mask_word, message, flags=re.IGNORECASE)
        return super().handler(message)


class SpamFilter(ContentFilter):
    def handler(self, message):
        print('Проверка на спам')
        words = message.lower().split()
        for i in words:
            if words.count(i) >= 3 and i != '*':
                return 'SpamFilter: сообщение заблокированно за спам!'
        if self._next_filter:
            return super().handler(message)


class LengthFilter(ContentFilter):
    def handler(self, message):
        print('Проверка на длину')

        if len(message) >= 120:
            return 'Сообщение превышает допустимую длинну!'
        else:
            return super().handler(message)


class PersonalDataFilter(ContentFilter):
    def handler(self, message: str) -> str:
        print('Проверка на чувствительные данные')
        message = re.sub(r'\b\S+@\S+\b', '[email удален]', message)
        message = re.sub(r'\b\d{11}\b', '[телефон удален]', message)
        message = re.sub(r'\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}', '[телефон удален]', message)
        return super().handler(message)


one = ProfanityFilter()
two = SpamFilter()
three = LengthFilter()
next = PersonalDataFilter()

test_data = [
    'плохое удален удален удален',
    'тут плохое', 'assad@gmail.com',
    '12345678901', '+7(958)-977-32-32',
    'нормальное сообщение'
    ]

one.set_next(two).set_next(three).set_next(next)


def run(test_data):
    for i in test_data:
        print(one.handler(i))
        print()


run(test_data)
