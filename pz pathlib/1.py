"""
управление файлами и папками

получить текущую рабочую директорию
создать в ней reports директорию
перейти в нее
Path.cwd(), Path.mkdir(), Path.chdir() (через os.chdir(Path))

создать текстовый summary.txt в reports
записать туда список файлов из текущей директории
Path.write_text(), Path.iterdir()

прочитать содержимое summary.txt и вывести
Path.read_text()

фильтрация файлов по расширению
получить все .txt файлы в текущей папке
вывести их имена и размеры
Path.glob('*.txt'), Path.stat()

рекурсивный обход директорий
Path.rglob("*")
"""
from pathlib import Path
import os


p = Path.cwd()
directory = 'reports'
files = 'summary.txt'


def create_dir():
    (p / directory).mkdir(parents=True, exist_ok=True)
    os.chdir(str(Path(directory)))
    p2 = Path.cwd()
    return p2


def create_file(p2):
    for i in Path('.').iterdir():
        if i.is_file():
            if Path(files).stat().st_size == 0:
                (p2 / files).write_text(str(i))
                continue
            (p2 / files).write_text(Path(files).read_text() + '\n' + str(i))
    print('Список файлов текущей директории:\n', Path(files).read_text(), '\n')


def filter_files():
    for i in Path('.').glob('*.txt'):
        if i.is_file():
            print(f'Файл {i} размером {i.stat().st_size}')


def directory_traversal():
    print('\nОбход директории:')
    for i in Path('.').rglob('*'):
        print(i)


create_d = create_dir()
create_f = create_file(create_d)
filter_files()
directory_traversal()
