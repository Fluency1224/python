#/usr/bin/env python
#coding:utf-8

#socket客户端
import socket
#创建流式套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#主机名和端口号
host = socket.gethostname()
port = 8888

#连接服务器
sockfd.connect((host,port))
#接收信息
clientMsg = sockfd.recv(1024)
print(clientMsg.decode('utf-8'))

#关闭套接字
sockfd.close()