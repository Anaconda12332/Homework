import os
import sys


# утилита сис админа
"""
analyzer.py

1 принимать путь к папке из аргументов командной строки. sys.argv если
аргументов нет - сообщение об ошибке и выход с кодом 1
2 проверять существование os.path.exists и является ли путь директорией.
Если неверный - заверить с 2
3 выводить список файлов с их размерами.
os.listdir os.path.join os.path.getsize os.path.isfile
4 позволяет дополнительно отфильтровать файлы по расширению
(только .txt например) если пользователь передал второй
аргумент os.path.splitext
5 показывает общую информацию о среде выполения
os.name os.getcwd os.environ.get sys.version
    ос
    рабочая dir
    PATH
    sys.version

sys.exit

"""


def print_error(message, num):
    sys.stderr.write(f"Ошибка: {message}\n")
    sys.exit(num)


def main():
    if len(sys.argv) < 2:
        print_error("Путь к папке не указан", 1)

    path = sys.argv[1]
    ext = ".txt" if len(sys.argv) < 3 else sys.argv[2]
    all_files = []

    if not os.path.exists(path):
        print_error("Путь не существует", 2)
    elif not os.path.isdir(path):
        print_error("Путь не является директорией", 2)

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(ext):
                full_path = os.path.join(root, name)
                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    all_files.append((name, size))
    print('Список файлов:')
    for file in all_files:
        print(f"{file[0]}: {file[1]}")

    print('\nИнформация о системе:')
    if os.name == 'nt':
        print("ОС: Windows")
    else:
        print("ОС: Linux")
    print(f"Текущая директория: {os.getcwd()}")
    print(f"PATH: {os.environ.get('PATH')}")
    print(f"Версия Python: {sys.version}")

    sys.exit(0)


if __name__ == "__main__":
    main()
