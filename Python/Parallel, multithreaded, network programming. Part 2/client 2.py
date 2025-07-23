import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print('Клиент подключися к серверу', client_socket.getsockname())

try:
    data = client_socket.recv(1024)
    print("сервер:", data.decode())

    client_socket.send('OK'.encode())

    with open('client2.txt', 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
    print('Файл принят')
except Exception as e:
    print(e)
finally:
    client_socket.close()
