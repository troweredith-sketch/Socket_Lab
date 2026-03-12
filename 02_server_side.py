import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 开启端口复用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ⚠️ 极其核心：云服务器必须绑定 0.0.0.0，向全世界敞开大门！
server_socket.bind(('0.0.0.0', 10086))
server_socket.listen(5)

print("🚀 云服务器已启动，正在向全世界监听 10086 端口...")

while True:
    try:
        accept_socket, client_info = server_socket.accept()
        print(f"🎉 收到来自全球网友 {client_info} 的连接！")
        
        # 发送云端专属欢迎语
        accept_socket.send('Welcome to Hong Kong Cloud Server!'.encode('utf-8'))
        
        data = accept_socket.recv(1024).decode('utf-8')
        print(f"📩 客户端发来消息: {data}")
        
        accept_socket.close()
    except KeyboardInterrupt:
        print("\n🛑 接收到退出信号，服务器安全关闭。")
        break
    except Exception as e:
        print(f"❌ 发生小错误: {e}")

