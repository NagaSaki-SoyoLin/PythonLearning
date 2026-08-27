"""
案例: 文件上传案例, 客户端代码

回顾: 网编客户端实现流程
    1. 创建客户端Socket对象
    2. 连接服务器端的 ip 和 端口号
    3. 关联数据源文件, 读取内容, 写给服务器端
    4. 释放资源
"""
# 导包
import socket

# 1. 创建客户端Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器端的 ip 和 端口号
client_socket.connect(("127.0.0.1", 6666))  # 127.0.0.1 = 本机回环地址, 本机测试用
# 3. 关联数据源文件, 读取内容, 写给服务器端
# 3.1 关联数据源数据
with open('./data/绕口令.txt', 'rb') as src_f:  # 需自行在data目录放一个 绕口令.txt
    # 3.2 循环读取内容
    while True:
        # 3.3 具体的读取操作
        data = src_f.read(8192)
        # 3.4 把读取到的数据写给服务器端
        client_socket.send(data)
        # 3.5 如果读取到的数据为空, 说明文件读取完毕
        if len(data) == 0:
            break

# 4. 接收回执信息
# print(f'客户端收到: {client_socket.recv(1024).decode("utf-8")}')

# 5. 释放资源
client_socket.close()
