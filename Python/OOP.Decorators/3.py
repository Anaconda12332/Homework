# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные.
# Используя механизм декораторов, решите вопрос
# отчетности для организаций.
import json
import xml.etree.cElementTree as ET


def text_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        result = 'Ваш ежемесячный отчет:\n'
        result += f'Доходы за месяц: {data['Доход']}\n'
        result += f'Расходы за месяц: {data['Расход']}\n'
        result += f'Чистая выручка: {data['Выручка']}\n'
        print(result)
        return data
    return wrapper


def json_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        json_data = json.dumps(data, indent=2, ensure_ascii=False)
        print('Финансовый отчет (JSON):\n', json_data)
        print()
        return data
    return wrapper


def xml_report(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        root = ET.Element('Отчет', {"id": "123"})
        income = ET.SubElement(root, 'Доход')
        income.text = str(data['Доход'])
        expenses = ET.SubElement(root, 'Расход')
        expenses.text = str(data['Расход'])
        revenue = ET.SubElement(root, 'Выручка')
        revenue.text = str(data['Выручка'])

        xml_string = ET.tostring(root, encoding='unicode')
        print('Финансовый отчет (XML):\n', xml_string)
        print()
        return data
    return wrapper


@text_report
def financial_report(income, expenses):
    report = {}
    report['Доход'] = income
    report['Расход'] = expenses
    report['Выручка'] = income - expenses
    return report


@json_report
def financial_report_json(income, expenses):
    report = {}
    report['Доход'] = income
    report['Расход'] = expenses
    report['Выручка'] = income - expenses
    return report


@xml_report
def financial_report_xml(income, expenses):
    report = {}
    report['Доход'] = income
    report['Расход'] = expenses
    report['Выручка'] = income - expenses
    return report


financial_report(20, 12)
financial_report_json(20, 12)
financial_report_xml(20, 12)
