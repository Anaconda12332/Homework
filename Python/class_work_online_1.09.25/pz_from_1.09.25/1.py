"""
компания занимается обработкой больших тексовых файлов
вам нужно параллельно:
загружать тексты
делить их на части
считать частоту слов
сохранять результаты в общий словарь
синхронизировать доступ к ресурсам
модульность
"""
import multiprocessing
from multiprocessing import Process, JoinableQueue, Pipe, Lock, Event, Semaphore, BoundedSemaphore, Barrier, Value, Array, Manager
from concurrent.futures import ProcessPoolExecutor, as_completed


def file_loader(queue: JoinableQueue, barrier: Barrier, files: list):
    """
    Загружает содержимое файлов и помещает их в очередь
    Должен дождаться остальных учтчиков через Barrier
    :param queue: очередь для передачи данных
    :param barrier: барьер для синхронизации старта
    :param files: список файлов для обработки
    """
    barrier.wait()

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        print(f"[LOADER] Файл {filename} загружен")
        queue.put(text)

    for _ in range(multiprocessing.cpu_count()):
        queue.put(None)
    queue.join()


def text_worker(queue: JoinableQueue, result_pipe, word_freq: dict, lock: Lock, sem: Semaphore, counter: Value, lengths: Array):
    """
    Извлекает тексты из очереди, обрабатывает их и отправляет промежуточные результаты по каналу.
    :param queue: очередь с текстами
    :param result_pipe: pipe для отправки промежуточных данных
    :param word_freq: общий словарь (Manager.dict) для частот слов
    :param lock: блокировка для синхронизации доступа к словарю
    :param sem: семафор для ограничения числа параллельных процессов
    :param counter: общий счётчик обработанных файлов (Value)
    :param lengths: массив длин текстов (Array)
    """
    while True:
        text = queue.get()
        if text is None:
            queue.task_done()
            break

        with sem:
            words = text.split()
            local_count = len(words)
            local_dict = {}
            for w in words:
                w = w.lower().strip(",.!?")
                local_dict[w] = local_dict.get(w, 0) + 1

        with lock:
            for k, v in local_dict.items():
                word_freq[k] = word_freq.get(k, 0) + v

        with counter.get_lock():
            counter.value += 1

        for i in range(len(lengths)):
            if lengths[i] == 0:
                lengths[i] = local_count
                break

        result_pipe.send((local_count, len(local_dict)))

        queue.task_done()


def result_collector(result_pipe):
    """
    Принимает промежуточные результаты обработки текстов через Pipe и выводит их.
    """
    while True:
        try:
            local_count, unique_words = result_pipe.recv()
            print(f"[COLLECTOR] Текст: {local_count} слов, {unique_words} уникальных")
        except EOFError:
            break


def pool_word_count(text: str) -> dict:
    """
    Функция для подсчёта слов в тексте. Используется с Pool.map или ProcessPoolExecutor.
    :param text: текстовая строка
    :return: словарь {слово: количество}
    """
    words = text.split()
    local_dict = {}
    for w in words:
        w = w.lower().strip(",.!?")
        local_dict[w] = local_dict.get(w, 0) + 1
    return local_dict


def pool_callback(result: dict):
    """
    Callback-функция для сбора результатов работы пула.
    """
    print('[POOL CALLBACK] Получен результат с', len(result), 'слов')


def final_report(event: Event, word_freq: dict, counter: Value, lengths: Array):
    """
    Ждёт сигнал от Event, затем выводит финальный отчёт:
    - частотный словарь
    - количество обработанных файлов
    - среднюю длину текста
    """
    print("[REPORT] Ожидание завершения всех процессов...")
    event.wait()

    print('\n------ Финальный отчет -------')
    print(f"Общее количество обработанных файлов: {counter.value}")

    lengths_list = [l for l in lengths if l > 0]
    if lengths_list:
        avg_len = sum(lengths_list) / len(lengths_list)
    else:
        avg_len = 0

    print(f"Средняя длина текста: {avg_len:.2f} слов")
    print(f"Общее количество уникальных слов: {len(word_freq)}")
    print("Топ-10 самых часто встречающихся слов:")
    for k, v in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{k}: {v}")


def main():
    """
    Главная функция:
    - создаёт все очереди, пайпы, события, блокировки
    - запускает процессы
    - использует Pool и ProcessPoolExecutor
    - синхронизирует работу через Barrier, Event, Condition, Semaphore
    """
    manager = Manager()
    word_freq = manager.dict()
    lock = Lock()
    sem = BoundedSemaphore(multiprocessing.cpu_count())
    event = Event()
    barrier = Barrier(2)
    counter = Value('i', 0)
    lengths = Array('i', [0] * 100)

    queue = JoinableQueue()
    parent_conn, child_conn = Pipe()

    files = ['file1.txt', 'file2.txt']

    loader = Process(target=file_loader, args=(queue, barrier, files))
    collector = Process(target=result_collector, args=(child_conn,))

    workers = [
        Process(target=text_worker,
                args=(queue, parent_conn, word_freq, lock, sem, counter, lengths))
        for _ in range(multiprocessing.cpu_count())
    ]

    loader.start()
    collector.start()

    for w in workers:
        w.start()

    barrier.wait()

    loader.join()
    for w in workers:
        w.join()
    parent_conn.close()
    collector.terminate()

    report_proc = Process(target=final_report, args=(event, word_freq, counter, lengths))
    report_proc.start()
    event.set()
    report_proc.join()

    print('пример с ProcessPoolExecutor')
    sample_texts = [
        'The quick brown fox jumps over the lazy dog.',
        'The quick brown fox jumps over the lazy dog.',
    ]
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(pool_word_count, text) for text in sample_texts]
        for future in as_completed(futures):
            pool_callback(future.result())


if __name__ == "__main__":
    main()
