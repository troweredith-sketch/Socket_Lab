import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 10086))

with open('./data_client/1.txt', 'rb') as src_f:
    while True:
        data = src_f.read(8192)

        client_socket.send(data)

        if len(data) == 0:
            break

client_socket.shutdown(socket.SHUT_WR)

print(f'客户端收到：{client_socket.recv(1024).decode()}')

client_socket.close()