import socket
import threading
import datetime


def handle_client(conn, addr):
    logger(addr)
    print(f'Ip {addr} connected!')

    try:
        data = conn.recv(1024)
        message = data.decode()
        print(f"Message from {addr}: {message}")
        conn.send(f'Принятое сообщение: {message}'.encode())
    except Exception as e:
        print(f'Error: ip {addr[0]}: {e}')
    finally:
        conn.close()


def logger(addr):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}]: подключение с {addr[0]}: порт {addr[1]}\n"
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(log_message)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen(3)
print("Server is listening...")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
