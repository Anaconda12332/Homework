"""
Задание 3
Пользователь с клавиатуры вводит путь к существующей директории
и к новой директории. После чего
запускается поток, который должен скопировать содержимое директории
в новое место. Необходимо сохранить
структуру директории. На экран необходимо отобразить
статистику выполненных операций.
"""
from pathlib import Path
import os
import shutil
import threading


def walk_directory_tree(src, dst, count):

    os.makedirs(dst, exist_ok=True)

    for root, dirs, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        dst_path = os.path.join(dst, rel_path)

        for dir in dirs:
            print('Копируем папку', dir)
            os.makedirs(os.path.join(dst_path, dir), exist_ok=True)
            count['dir'] += 1

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_path, file)

            print('Копируем файл', file)
            shutil.copy2(src_file, dst_file)
            count['file'] += 1


if __name__ == '__main__':
    count = {
        'dir': 0,
        'file': 0
    }

    path_src = input('Введите путь к исходной папке: ')
    path_dst = input('Введите путь к новой папке: ')

    if Path(path_src).exists() and Path(path_src).is_dir():
        t = threading.Thread(target=walk_directory_tree, args=(path_src, path_dst, count))
        t.start()
        t.join()
        print(f'Всего скопированно: {count['dir']} папок и {count['file']} файлов')
    else:
        print('Такой папки не существует')
