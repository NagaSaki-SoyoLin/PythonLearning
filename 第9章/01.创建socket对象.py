"""
案例: 演示socket对象的创建

网络编程介绍:
    概述:
        网络编程也叫网络通信, Socket通信, 即: 通信双方都独有自己的Socket对象,
        数据在Socket之间通过 数据报包(UDP协议) 或者 字节流(TCP协议) 的形式进行传输
    大白话举例:
        你和你遥远的朋友在聊天, 看看这你们两个人在交互, 其实是通过 两部手机(双方各自的手机)来交互的
"""

# 导包
import socket

# 创建Socket对象
# 参1: Address Family, 地址族, 即: Ipv4 还是 IpV6, 默认值: AF_INET(ipv4)    AF_INET6(ipv6)
# 参2: Socket Type, Socket类型, 即: TCP 还是 UDP, 默认值: SOCK_STREAM(TCP)   SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)
