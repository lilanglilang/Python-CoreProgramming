# -*- coding: utf-8 -*-
import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#tcp发送
sk.connect(("169.254.66.254", 8080))  # 主动初始化与服务器端的连接
send_data = input("输入发送内容：")
sk.sendall(bytes(send_data, encoding="utf8"))
accept_data = sk.recv(1024)
print(str(accept_data, encoding="utf8"))
sk.close()