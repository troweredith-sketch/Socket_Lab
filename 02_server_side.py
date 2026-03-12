import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('127.0.0.1', 10086))

server_socket.listen(5)

accept_socket, client_info = server_socket.accept()

accept_socket.send(b'Welcome To Socket!')

data = accept_socket.recv(1024).decode('utf-8')
print(f'服务器端收到 来自 {client_info} 的信息：{data}')

accept_socket.close()

