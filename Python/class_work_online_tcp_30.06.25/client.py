"""
#задание 1:
клиент сначала отправляет команду "UPLOAD" или "DOWNLOAD"
если UPLOAD - передает файл
если DOWNLOAD - сервер ищет файл и возвращает его содержимое
"""
import socket
import os

filename = 'отправляемый_файл.txt'
filesize = os.path.getsize(filename)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

command = input('Введите команду: ').upper()

if command == 'UPLOAD':
    client_socket.send('UPLOAD\n'.encode())
    client_socket.send(f"{filename}\n".encode())

    with open(filename, 'rb') as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
    client_socket.shutdown(socket.SHUT_WR)
    print('файл отправлен')

elif command == 'DOWNLOAD':
    client_socket.send('DOWNLOAD\n'.encode())
    client_socket.send(f"принятый_сервером_{filename}\n".encode())
    with open(f'загруженный_из_сервера_{filename}', 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    client_socket.shutdown(socket.SHUT_WR)
    print('файл получен')

client_socket.close()
