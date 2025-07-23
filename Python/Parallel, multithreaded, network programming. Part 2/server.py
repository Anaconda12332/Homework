"""
Реализуйте клиент — серверное приложение, позволяющее передавать
файлы. Один пользователь инициирует
передачу файла, второй подтверждает. После подтверждения начинается
отправка. Если отправка была удачной
необходимо сообщить об этом отправителю.
"""
import socket
import threading


event = threading.Event()
print_lock = threading.Lock()


def file_load(conn, addr):
    try:
        with print_lock:
            print('Ожидание подтверждения отправки файла...')
        conn.send('Подтвердите отправку файла'.encode())

        response_conn = conn.recv(1024)
        if response_conn.decode() == 'OK':
            with print_lock:
                print('Подтверждение получено.')
            conn.send('Начало передачи файла'.encode())
            with open('server.txt', 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            conn.send('Отправка завершена'.encode())
            with print_lock:
                print('Файл получен.')

    except Exception as e:
        print(e)
    finally:
        conn.close()
        event.set()


def file_transfer(conn2, addr2):
    event.wait()
    with print_lock:
        print('Ожидание подтверждения отправки файла...')
    try:
        conn2.send('Подтвердите получение файла'.encode())

        response_conn2 = conn2.recv(1024)
        with print_lock:
            print('Подтверждение получено.')

        if response_conn2.decode() == 'OK':
            with print_lock:
                print('Отправка файла второму клиенту...')

            with open('server.txt', 'rb') as file:
                while chunk := file.read(1024):
                    conn2.send(chunk)
            with print_lock:
                print('Отправка завершена.')
    except Exception as e:
        print(e)
    finally:
        conn2.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.settimeout(10.0)
server_socket.bind(('localhost', 12345))
server_socket.listen(2)
with print_lock:
    print('Server is running and listening...')


conn, addr = server_socket.accept()
with print_lock:
    print(f"Connection from {addr} established. ")

    conn2, addr2 = server_socket.accept()
with print_lock:
    print(f"Connection from {addr2} established. ")

thread_1 = threading.Thread(target=file_load, args=(conn, addr))
thread_2 = threading.Thread(target=file_transfer, args=(conn2, addr2))
thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
