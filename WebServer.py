# WebServer.py
from socket import *

# 1. 创建 TCP 的“迎宾大门” (注意第二个参数变成了 SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)

# 2. 绑定一个端口，假设我们用 6789 端口 (作业要求避开默认的 80 端口)
serverPort = 6789
serverSocket.bind(('', serverPort))

# 3. 让迎宾大门竖起耳朵，开始监听敲门声 (最大排队人数设为 1)
serverSocket.listen(1)

print(f"Web 服务器已启动，正在监听 {serverPort} 端口...")
print("请在浏览器输入 http://127.0.0.1:6789/helloworld.html 访问")

# 服务器是全天候营业的，所以要用死循环
while True:
    print('Ready to serve...')
    
    # TODO 1: 迎接客人的敲门 (TCP 专属动作)
    # 当有客户(浏览器)来连接时，使用 accept() 方法接受连接。
    # 这个方法会吐出两个东西：一个是专门为这个客户生成的“专属服务员”(connectionSocket)，另一个是客户的地址(addr)。
    # 你的代码：
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # TODO 2: 听听客户说了什么 (接收数据)
        # 用刚刚生成的专属服务员 connectionSocket，调用 recv(1024) 接收浏览器发来的 HTTP 请求报文。
        # 别忘了收到的字节流需要用 .decode() 拆包成字符串，并存入变量 message 中。
        # 你的代码：
        message = connectionSocket.recv(1024).decode()
        
        # 打印出浏览器到底给我们发了什么神奇的暗号
        print("\n--- 收到来自浏览器的 HTTP 请求 ---")
        print(message)
        print("----------------------------------\n")
        
        # 测试完毕，直接关闭这个专属服务员（粗暴拒客，我们下一阶段再给它发网页）
        connectionSocket.close()
        
    except IOError:
        # 如果中间发生错误，也要记得把服务员辞退，释放资源
        connectionSocket.close()

# 关闭迎宾大门（实际上只要死循环不破，这行不会执行）
serverSocket.close()