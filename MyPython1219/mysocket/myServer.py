#/usr/bin/env python
#coding:utf-8

#一个socket服务器程序
import socket
from time import sleep

#创建流式监听套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#获取主机名、定义端口
host = socket.gethostname()
port = 8888

#绑定端口
sockfd.bind((host,port))
#监听套接字(最大监听说)
sockfd.listen(10)

#创建循环服务器
while True:
    #创建连接套接字
    fd,addr = sockfd.accept()
    print(str(addr),'已连接','套接字fd=',fd)
    sleep(10)
    serverMsg = 'I am server!'
    fd.send(serverMsg.encode('utf-8'))
    
    fd.close()
sockfd.close()