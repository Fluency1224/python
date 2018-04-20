#/usr/bin/env python
#coding:utf-8
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = socket.gethostname()
port = 8888

sock.bind((name, port))
print("warting for connect...")
data,addr = sock.recvfrom(1024)
print(str(addr) + "being connect!")
data = data.decode("utf-8")
ip = data.split(' ')[0].split('=')[1]
mac = data.split(' ')[1].split('=')[1]
print(ip, mac)

sock.close()



