"""
отправитель отправляет от 1 до 5
приемник получает через Pipe и печатет их квадрта
когда отправитель закончит, он отправит специальное сообщение "STOP" и
применик завершит работу
"""
from multiprocessing import Process, Pipe
import time


def sender(conn):
    for i in range(1, 6):
        conn.send(i)
        print(f"[ОТПРАВИТЕЛЬ]: Отправлено число {i}")
        time.sleep(1)
    conn.send("STOP")
    conn.close()


def receiver(conn):
    while True:
        msg = conn.recv()
        if msg == "STOP":
            print("Получено сообщение 'STOP'. Завершение работы.")
            break
        print(f"[ПОЛУЧАТЕЛЬ]: получено число {msg}, его квадрат: {msg ** 2}")


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
