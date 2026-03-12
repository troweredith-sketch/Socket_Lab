# UDPPingClient.py
import time
from socket import *

# 1. 准备目标地址
serverName = '127.0.0.1' # 发给自己
serverPort = 12000

# 2. 创建 UDP 套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 3. 【极其重要】设置超时时间为 1 秒
clientSocket.settimeout(1.0)

# 发送 10 个 Ping 报文
for i in range(1, 11):
    # 获取当前精确时间（发送时间）
    sendTime = time.time() 
    
    # 构造要发送的消息内容，例如：Ping 1 1678901234.56
    message = f"Ping {i} {sendTime}"
    
    try:
        # TODO: 使用 sendto() 方法，将 message 编码(encode)后发送给 (serverName, serverPort)
        # 你的代码写在这里：
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # TODO: 使用 recvfrom(1024) 接收服务器的回信 (返回 modifiedMessage 和 serverAddress)
        # 你的代码写在这里：
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        # 获取收到回信的当前时间
        returnTime = time.time() 
        
        # TODO: 计算往返时延 RTT (returnTime 减去 sendTime)
        # 你的代码写在这里：
        rtt = returnTime - sendTime
        
        print(f"收到回复: {modifiedMessage.decode()} | RTT: {rtt:.6f} 秒")
        
    except timeout:
        # 如果 1 秒内没收到，就会跳到这里执行
        print(f"请求 {i}: 请求超时 (Packet Lost)")

# 关闭套接字大门
clientSocket.close()