"""
Система тестирования

иерарахия вопросов
Question def check_answer(self, user_answer):
SingleChoiceQuestion один правильный ответ
MultipleChoiceQuestion несколько правильных ответов

интерфейс проверок
AnswerChecker def check()

реализации
StrictChecker точное совпадение
PartialChecker частичное совпадение

Question содержит ссылку на AnswerChecker
"""
