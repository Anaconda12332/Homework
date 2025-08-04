"""
1. Работа с текущей директорией
Получите текущую рабочую директорию.
Создайте в ней папку backup.
Перейдите в созданную папку.
os.getcwd(), os.mkdir(), os.chdir()

2. Сканирование папки
Вернитесь в исходную директорию.
Получите список всех файлов и папок в директории.
Отфильтруйте только файлы.
os.isfile() os.listdir(), os.path.isfile(), os.path.join()

3. Копирование файлов (эмуляция)
Для каждого файла из пункта 2:
Получите его размер.
Создайте копию с добавлением постфикса _backup в папке backup
(только симуляция, без shutil, можно просто создать пустой файл с
новым именем).
os.path.getsize(), open(), os.path.basename(), os.path.splitext()

4. Вывод информации о системе
Определите имя операционной системы.
Получите значение переменной окружения HOME или USERPROFILE
(в зависимости от ОС).
Выведите PID текущего процесса.
os.name, os.environ.get(), os.getpid()
"""

import os


def create_backup_folder(folder):
    path = os.path.join(folder, 'backup')
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as e:
            print('Ошибка создания папки:', e)
    else:
        print('Folder already exists')
    os.chdir(path)
    print('Текущий путь', os.getcwd())
    return os.getcwd()


def list_files(folder):
    os.chdir(folder)
    print('Текущий путь', os.getcwd())
    files = []
    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path) and file.endswith('.txt'):
                files.append(path)
                print('Путь к найденному файлу:', path)
    except OSError as e:
        print('Ошибка чтения папки:', e)
    return files


def simulate_backup(files, dest_folder):
    count = 0
    try:
        for file in files:
            file_size = os.path.getsize(file)
            print(f'Копируется файл: {os.path.basename(file)}, размером: {file_size}')

            name, ext = os.path.splitext(os.path.basename(file))
            backup_file = os.path.join(dest_folder, name + '_backup' + ext)

            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(backup_file, 'w') as f:
                f.write(content)
            count += 1
        print(f'Успешно скопировано {count} файлов')
    except Exception as e:
        print('Ошибка:', e)


def show_system_info():
    print('***Операционная система***')
    if os.name == 'nt':
        print('Имя операционной системы: Windows')
    elif os.name == 'posix':
        print('Имя операционной системы: Mac OS/Linux/Unix')
    else:
        print('Other')
    home = os.environ.get('HOME', os.environ.get('USERPROFILE', None))
    print('Значение переменной окружения:', home)
    print('PID:', os.getpid())


folder = os.getcwd()

path = create_backup_folder(folder)
files_list = list_files(folder)
simulate_backup(files_list, path)
show_system_info()
