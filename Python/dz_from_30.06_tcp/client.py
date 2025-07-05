import socket

hostname = 'localhost'

try:
    ip_addres = socket.gethostbyname(hostname)
except socket.gaierror:
    print('Hostname could not be resolved')

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_addres, 1234))

    client_socket.send('hello'.encode())
    response = client_socket.recv(1024)
    print('Server:', response.decode())

    client_socket.close()

except Exception as e:
    print(f'Error: {e}')
