"""
案例: 网编入门案例, 服务器端给客户端发送消息, 客户端给出回执信息

客户端开发流程:
    1. 创建客户端Socket对象
    2. 连接服务器端, 指定: 服务器端IP, 端口号
    3. 接收服务器端的信息并打印
    4. 给服务器端发送消息
    5. 释放资源

细节:
    客户端和服务器端是通过 字节流(bytes) 的形式实现的
"""
# 导包
import socket

# 1. 创建客户端Socket对象. ipv4, TCP协议
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器端, 指定: 服务器端IP, 端口号
client_socket.connect(('127.0.0.1', 10086))  # 127.0.0.1 = 本机回环地址, 本机测试用
# 3. 接收服务器端的信息并打印
data = client_socket.recv(1024).decode('utf-8')
print(f'客户端收到: {data}')

# 4. 给服务器端发送消息
client_socket.send('Socket很好玩儿, 很有趣, 我很喜欢!'.encode('utf-8'))
# 5. 释放资源
client_socket.close()
