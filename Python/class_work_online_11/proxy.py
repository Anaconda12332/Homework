
"""
прокси-доступ к дорогим операциям - генерация отчетов
RealReport - долгая инициализация/дорогой
    display()

ReportProxy реализует тот же интерфейс, создает настоящий отчет только при
первом вызове display()

Report - интерфейс
    display()
"""
from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def display(self):
        pass


class RealReport(Report):
    def __init__(self, report_name):
        self.report_name = report_name
        self.create_report()

    def display(self):
        print(f"[RealReport] отображение {self.report_name}")

    def create_report(self):
        print(f"[RealReport] создание {self.report_name}")


class ReportProxy(Report):
    def __init__(self, report_name):
        self.report_name = report_name
        self.real_report = None

    def display(self):
        if self.real_report is None:
            self.real_report = RealReport(self.report_name)
        self.real_report.display()


new_report = ReportProxy("Отчет 1")
new_report.display()
new_report.display()
