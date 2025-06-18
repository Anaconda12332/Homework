"""
Система тестирования

иерарахия вопросов
Question def check_answer(self, user_answer):
SingleChoiceQuestion один правильный ответ
MultipleChoiceQuestion несколько правильных ответов

интерфейс проверок
AnswerChecker def check()

реализации
AnswerChecker точное совпадение
PartialChecker частичное совпадение

Question содержит ссылку на AnswerChecker
"""
from abc import ABC, abstractmethod


class AnswerChecker(ABC):
    @abstractmethod
    def check(self, correct_answer, user_answer):
        pass


class StrictChecker(AnswerChecker):
    def check(self, correct_answer, user_answer):
        return correct_answer == user_answer


class PartialChecker(AnswerChecker):
    def check(self, correct_answer, user_answer):
        if not isinstance(correct_answer, set) or not isinstance(user_answer, set):
            return False
        check = correct_answer & user_answer
        return len(check) / len(user_answer) >= 0.5


class Question(ABC):
    def __init__(self,  text, correct_answer, checker: AnswerChecker):
        self.text = text
        self.correct_answer = correct_answer
        self.checker = checker

    @abstractmethod
    def check_answer(self, user_answer):
        pass


class SingleChoiceQuestion(Question):
    def check_answer(self, user_answer):
        return self.checker.check(self.correct_answer, user_answer)


class MultipleChoiceQuestion(Question):
    def check_answer(self, user_answer):
        return self.checker.check(self.correct_answer, user_answer)


q1 = SingleChoiceQuestion(
    'Сборник географических карт',
    'Атлас',
    checker=StrictChecker()
)

q2 = MultipleChoiceQuestion(
    'Назовите числа, которые больше 10, но меньше 15?',
    correct_answer={11, 12, 13, 14},
    checker=PartialChecker()
)

q3 = MultipleChoiceQuestion(
    'Назовите числа, которые больше 10, но меньше 15?',
    correct_answer={11, 12, 13, 14},
    checker=StrictChecker()
)

print('*' * 30)
print(q1.check_answer('Атлас'))
print(q1.check_answer('Атлас1'))
print(q1.check_answer(''))

print('*' * 30)
print(q2.check_answer({11, 12, 13, 14}))
print(q2.check_answer({11, 12, 13, 14, 16}))
print(q2.check_answer({}))

print('*' * 30)
print(q3.check_answer({11, 12, 13, 14}))
print(q3.check_answer({11, 12, 13, 14, 16}))
print(q3.check_answer({}))
