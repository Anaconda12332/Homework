"""
Создайте реализацию паттерна Command. Протестируйте работу созданного класса.
"""
"""
Создайте простую систему управления текстовым редактором, используя паттерн Command. У вас должны быть следующие классы:
TextEditor: класс, представляющий текстовый редактор. Он должен иметь методы insert_text, delete_text и replace_text, которые вставляют, удаляют и заменяют текст соответственно.
Command: абстрактный класс, представляющий команду. Он должен иметь методы execute и undo, которые будут выполнять и отменять команду соответственно.
InsertTextCommand, DeleteTextCommand и ReplaceTextCommand: конкретные классы команд, которые будут вставлять, удалять и заменять текст соответственно.
Invoker: класс, который будет выполнять команды. Он должен иметь методы set_command, execute_command и undo_command, которые устанавливают, выполняют и отменяют команду соответственно.
Ваша задача - создать объекты TextEditor, InsertTextCommand, DeleteTextCommand и ReplaceTextCommand, а затем использовать объект Invoker для управления текстовым редактором.
"""
from abc import ABC, abstractmethod


class TextEditor:
    def __init__(self):
        self.text = ''

    def insert_text(self, text):
        self.text += text if not self.text else ' ' + text
        return f'Вставляем текст: {text}'

    def delete_text(self, text):
        if text in self.text:
            self.text = self.text.replace(text, '')
            return f'Удаляем текст: {text}'
        return 'Такого текста нет'

    def replace_text(self, old_text, new_text):
        if old_text in self.text:
            self.text = self.text.replace(old_text, new_text)
            return f'Заменяем текст: {old_text} на {new_text}'
        return 'Такого текста нет'

    def show_text(self):
        if len(self.text) == 0:
            return 'Текст пуст'
        return self.text


class Command(ABC):
    @abstractmethod
    def execute(self, text=None):
        pass

    @abstractmethod
    def undo(self):
        pass


class InsertTextCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor
        self.text = None

    def execute(self, text=None):
        if text:
            self.text = text
        return self.editor.insert_text(self.text)

    def undo(self):
        return self.editor.delete_text(self.text)


class DeleteTextCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor
        self.text = None

    def execute(self, text=None):
        if text:
            self.text = text
        return self.editor.delete_text(self.text)

    def undo(self):
        return self.editor.insert_text(self.text)


class ReplaceTextCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor
        self.old_text = None
        self.new_text = None

    def execute(self, text=None):
        if text:
            self.old_text, self.new_text = text
        return self.editor.replace_text(self.old_text, self.new_text)

    def undo(self):
        return self.editor.replace_text(self.new_text, self.old_text)


class Invoker:
    def __init__(self):
        self.history = []
        self.redo = []

    def execute_command(self, command: Command, text):
        self.history.append(command)
        return command.execute(text)

    def redo_command(self):
        if self.redo:
            next = self.redo.pop()
            self.history.append(next)
            return next.execute()

    def undo_command(self):
        if self.history:
            last = self.history.pop()
            self.redo.append(last)
            return last.undo()


editor = TextEditor()
insert_command = InsertTextCommand(editor)
delete_command = DeleteTextCommand(editor)
replase_command = ReplaceTextCommand(editor)
invoker = Invoker()

print(invoker.execute_command(insert_command, 'Hello, world!'))
print(editor.show_text())

print(invoker.execute_command(delete_command, 'Hello, world!'))
print(editor.show_text())

print(invoker.undo_command())
print(editor.show_text())

print(invoker.execute_command(replase_command, ('Hello,', 'Hi')))
print(editor.show_text())

print(invoker.undo_command())
print(editor.show_text())

print(invoker.undo_command())
print(editor.show_text())

print(invoker.redo_command())
print(editor.show_text())

print(invoker.redo_command())
print(editor.show_text())
