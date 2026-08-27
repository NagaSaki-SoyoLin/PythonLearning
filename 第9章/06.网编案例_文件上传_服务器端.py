"""
案例: 文件上传案例, 服务器端代码

回顾: 网编服务器端实现流程
    1. 创建服务器端Socket对象
    2. 绑定ip 和 端口号
    3. 设置最大监听数
    4. 等待客户端申请建立连接
    5. 读取客户端上传的(文件)数据, 写到目的地文件
    6. 释放资源
"""

# 导包
import socket

# 1. 创建服务器端Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定ip 和 端口号
server_socket.bind(("", 6666))  # '' 表示监听本机所有网卡, 适配任意IP环境
# 3. 设置最大监听数
server_socket.listen(5)
# 4. 等待客户端申请建立连接
accept_socket, client_info = server_socket.accept()

# 5. 读取客户端上传的(文件)数据
# 5.1 关联目的地文件
with open('./data/my.txt', 'wb') as dest_f:
    # 5.2 循环读取数据
    while True:
        # 5.3 接收客户端上传的文件数据
        bys = accept_socket.recv(8192)  # 8192字节 = 8kb
        # 5.4 判断是否读取到数据, 无数据(说明客户端断开连接)结束即可
        if len(bys) == 0:
            break
        # 5.5 把读取到的数据写入到目的地文件中
        dest_f.write(bys)

# 6.给出回执信息
# accept_socket.send('文件上传成功!'.encode('utf-8'))

# 7. 释放资源
accept_socket.close()
