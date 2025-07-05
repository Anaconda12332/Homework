"""
надежная отправка сообщений по UDP
udp server:
    принимает сообщения от клиента
    в сообщении UID (номер пакета)
    сервер хранит список уже полученных идентификаторов
    если UID уже получен, то игнорируем
    если новое
        печать
        отправить OK при корректности или ERROR (содержит слово ошибка)
        при ошибке

udp client:
    отправляет серверу 1 или более сообщений с UID например (1:Привет, ...)
    ожидает ответа
    если нет за 3 сек - повтор
    максимум 3 попытки
    если есть ответ, то измеряем и выводим время задержки
    если прислали ERROR - выводим ошибку
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 1234))

processed_id = set()

print('Server started and listening...')

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f'Received from {client_address}: ', message)

        message_split = message.split(':')
        message_id = message_split[0]
        message_content = message_split[1]

        if message_id in processed_id:
            print(f'Message {message_id} already processed')
            continue

        processed_id.add(message_id)

        if 'ERROR' in message_content:
            response = 'ERROR'
        else:
            response = 'OK'

        server_socket.sendto(response.encode(), client_address)

    except Exception as e:
        print(f'Error: {e}')
