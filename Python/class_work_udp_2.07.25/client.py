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
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3)

server_address = ('localhost', 1234)
message_default = 'Привет, сервер!'
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    message_id = f'{attempt}'
    message = f'{message_id}:{message_default}'

    try:
        start_time = time.time()

        print(f'Отправка сообщения {message} попытка {attempt}')
        client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(4096)

        end_time = time.time()
        delay = end_time - start_time

        print(f'Получен ответ сервера: {data.decode()} с задержкой {delay:.4f} секунд')

        if data.decode() == 'OK':
            print(f'Сервер принял сообщение {message} с UID {message_id}')
            break
        elif data.decode() == 'ERROR':
            print(f'Ошибка при отправке сообщения {message} с UID {message_id}')
            break

    except socket.timeout:
        print('Превышено время ожидания ответа от сервера. Повторная попытка...')

    except Exception as e:
        print('Ошибка:', e)
        break
else:
    print('Нет ответа от сервера.')
