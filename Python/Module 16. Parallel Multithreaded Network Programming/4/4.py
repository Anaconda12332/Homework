"""
Задание 4
Пользователь с клавиатуры вводит путь к существующей
директории и слово для поиска. После чего запускаются
два потока. Первый должен найти файлы, содержащие
искомое слово и слить их содержимое в один файл. Второй
поток ожидает завершения работы первого потока.
После чего проводит вырезание всех запрещенных слов
(список этих слов нужно считать из файла с запрещенными словами)
из полученного файла. На экран необходимо
отобразить статистику выполненных операций.
"""
import os
import threading
import re


def search_and_merge_files(src, word):
    files_found = 0
    words_found = 0
    try:
        for root, dirs, files in os.walk(src):
            for file in files:
                full_path = os.path.join(root, file)
                print('-' * 20)
                print('Найден файл:', file)

                with open(full_path, 'r', encoding='utf-8') as f:
                    print('Идет поиск слов в файле:', file)
                    content = f.read()

                    for i in content.split():
                        if word.lower() == i.lower():
                            print('Найдено искомое слово:', word)
                            files_found += 1
                            words_found += 1
                            with open('result.txt', 'a', encoding='utf-8') as file:
                                print('Содержимое записывается в файл: result.txt')
                                file.write(content + '\n')

        print(f"Найдено файлов: {files_found}, найдено вхождений: {words_found}")
        event.set()
    except Exception as e:
        print('[Ошибка]', e)


def delete_forbidden_words(forbidden_words):
    words_removed = 0
    try:
        event.wait()
        print('-' * 20)
        print('Запускается удаление запрещенных слов')
        with open(forbidden_words, 'r', encoding='utf-8') as f:
            words = [line.strip().lower() for line in f.readlines()]

            if not os.path.exists('result.txt'):
                print("Файл result.txt не существует!")
                return
            with open('result.txt', 'r', encoding='utf-8') as file:
                content = file.read()

                pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words) + r')\b'
                regex = re.compile(pattern, re.IGNORECASE)

                content = regex.sub('[Удалено]', content)
                words_removed = content.count('[Удалено]')

        with open('result.txt', 'w', encoding='utf-8') as a:
            a.write(content)

        print(f"Всего удалено запрещённых слов: {words_removed}")
        print('Программа завершена')
    except Exception as e:
        print('[Ошибка]', e)


if __name__ == '__main__':
    event = threading.Event()
    user_dir = input('Введите путь к директории: ').lower()
    word = input('Введите слово для поиска: ').lower()
    forbidden_words = 'forbidden_words.txt'

    if os.path.exists(user_dir):
        thread1 = threading.Thread(target=search_and_merge_files, args=(user_dir, word))
        thread2 = threading.Thread(target=delete_forbidden_words, args=(forbidden_words,))

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    else:
        print('Путь не существует!')
