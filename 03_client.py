import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('43.99.112.155', 10086))

data = client_socket.recv(1024).decode('utf-8')
print(f'客户端收到：{data}')

client_socket.send('客户端成功响应'.encode('utf-8'))

client_socket.close()