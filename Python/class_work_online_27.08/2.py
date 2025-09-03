"""
Общий словарь частот слов
список строк
каждый процесс обрабатывает свою часть списка строк и считает сколько раз
каждое слово встречается в списке
общий результат в словарь Manager
Lock
"""
from multiprocessing import Process, Manager, Lock


def count_words(lines, result_dict, lock):
    for line in lines:
        word = line.lower().split()
        for j in word:
            with lock:
                if j in result_dict:
                    result_dict[j] += 1
                else:
                    result_dict[j] = 1


if __name__ == '__main__':
    manager = Manager()
    result_dict = manager.dict()
    lock = Lock()

    lines = [
        'Привет как дела',
        'Привет мир',
        'Тест строка',
        'Просто строка',
        'Привет как дела'
    ]

    p1 = Process(target=count_words, args=(lines[:2], result_dict, lock))
    p2 = Process(target=count_words, args=(lines[2:], result_dict, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Колличество слов: ', result_dict)
