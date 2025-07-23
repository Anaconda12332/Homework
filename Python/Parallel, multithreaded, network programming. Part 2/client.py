import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5.0)
client_socket.connect(('localhost', 12345))
print('Клиент подключися к серверу', client_socket.getsockname())

try:
    data = client_socket.recv(1024)
    print("сервер:", data.decode())

    client_socket.send('OK'.encode())

    data = client_socket.recv(1024)
    print("сервер:", data.decode())

    with open('client.txt', 'rb') as file:
        while chunk := file.read(1024):
            client_socket.send(chunk)
    client_socket.shutdown(socket.SHUT_WR)

    data = client_socket.recv(1024)
    print('сервер:', data.decode())

    print('Файл передан')
except Exception as e:
    print(e)
finally:
    client_socket.close()
