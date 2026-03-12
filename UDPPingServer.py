# UDPPingServer.py
import random
from socket import *

# 创建 UDP 套接字并绑定 12000 端口
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("UDP 服务器已启动，正在监听 12000 端口...")

while True:
    # 接收客户发来的数据
    message, address = serverSocket.recvfrom(1024)
    
    # 生成 0-10 的随机数，模拟 30% 的网络丢包率
    rand = random.randint(0, 10)
    if rand < 3:
        continue # 如果小于 3，服务器就装死（不回复）
    
    # 否则，将消息转为大写并原路弹回
    serverSocket.sendto(message.upper(), address)