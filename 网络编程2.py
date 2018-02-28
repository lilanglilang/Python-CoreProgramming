# -*- coding: utf-8 -*-
import socket
class TcpServer(object):
    def __init__(self):
        serverSocket=socket(socket.AF_INET,socket.SOCK_STREAM)
        assert isinstance(serverSocket,socket)
        serverSocket.bind("",8899)
        serverSocket.listen(5)
        clientSocket,clientInfo=serverSocket.accept()