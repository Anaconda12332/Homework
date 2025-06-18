"""
Abstract factory
система создания комлектов образовательных материалов
модуль генерирует учебные комплекты для направлений:
программирование
история

в комплект входят:
Course - текст темы
Test - набор вопросов
Assignment - задание

3 интерфейса/аbc класса
Course get_content()
Test get_questions()
Assignment get_task()

LearningMaterialFactory абстрактная фабрика: создаёт комплекты материалов
    create_course() -> Course
    create_test() -> Test
    create_assignment() -> Assignment

две конкретные фабрики
ProgrammingMaterialFactory
HistoryMaterialFactory

клиентская функция принимает фабрику и создаёт комплекты материалов курс тест
задание
"""
from abc import ABC, abstractmethod


class Course(ABC):
    @abstractmethod
    def get_content(self):
        pass


class Test(ABC):
    @abstractmethod
    def get_questions(self):
        pass


class Assignment(ABC):
    @abstractmethod
    def get_task(self):
        pass


class CoursePrigramming(Course):
    def get_content(self):
        return 'Тема курса по программированию'


class TestProgramming(Test):
    def get_questions(self):
        return 'Вопросы по программированию'


class AssignmentProgramming(Assignment):
    def get_task(self):
        return 'Задание по программированию'


class CourseHistory(Course):
    def get_content(self):
        return 'Тема курса по истории'


class TestHistory(Test):
    def get_questions(self):
        return 'Вопросы по истории'


class AssignmentHistory(Assignment):
    def get_task(self):
        return 'Задание по истории'


class LearningMaterialFactory(ABC):
    @abstractmethod
    def create_course(self):
        pass

    @abstractmethod
    def create_test(self):
        pass

    @abstractmethod
    def create_assignment(self):
        pass


class ProgrammingMaterialFactory(LearningMaterialFactory):
    def create_course(self):
        return CoursePrigramming()

    def create_test(self):
        return TestProgramming()

    def create_assignment(self):
        return AssignmentProgramming()


class HistoryMaterialFactory(LearningMaterialFactory):
    def create_course(self):
        return CourseHistory()

    def create_test(self):
        return TestHistory()

    def create_assignment(self):
        return AssignmentHistory()


def create_materials(factory: LearningMaterialFactory):
    course = factory.create_course()
    test = factory.create_test()
    assignment = factory.create_assignment()

    print(course.get_content())
    print(test.get_questions())
    print(assignment.get_task())
    print()


factory_programming = ProgrammingMaterialFactory()
factory_history = HistoryMaterialFactory()

create_materials(factory_programming)
create_materials(factory_history)
