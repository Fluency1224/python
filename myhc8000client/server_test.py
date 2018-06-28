#/usr/bin/env python
#coding:utf-8
#socket客户端
import socket
import time
#import base64
import pyDes

#创建流式套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#主机名和端口号
host = '192.168.1.138'
port = 32000
#连接服务器
sockfd.connect((host,port))

#发送信息
sendMsg = 'H00:1D:43:10:00:5220150211'.encode(encoding='utf_8', errors='strict')

k = pyDes.des("12345678", pyDes.ECB, None, pad=None, padmode=pyDes.PAD_PKCS5)

d = k.encrypt(sendMsg)
s = k.decrypt(d)
print(sendMsg, sendMsg.__sizeof__(), type(sendMsg))
print(d, d.__sizeof__(), type(d))
print(s, s.__sizeof__(), type(s))
sockfd.sendall(d)

clientMsg = sockfd.recv(1024)
print(clientMsg)
sendMsg = '0\000\000'.encode(encoding='utf_8', errors='strict')
sockfd.send(sendMsg)
time.sleep(1)
sendMsg = 'a\000\000'.encode(encoding='utf_8', errors='strict')
sockfd.send(sendMsg)
time.sleep(1)
sendMsg = '0\000\000'.encode(encoding='utf_8', errors='strict')
sockfd.send(sendMsg)
time.sleep(1)
sendMsg = '0\000\000'.encode(encoding='utf_8', errors='strict')
sockfd.send(sendMsg)
time.sleep(1)
sendMsg = '0\000\000'.encode(encoding='utf_8', errors='strict')
sockfd.send(sendMsg)
clientMsg = sockfd.recv(1024)
print(clientMsg)


sockfd.close()
# Des_Key = "12345678" # Key
# Des_IV = "\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量
# 
# 
# k = pyDes.des("12345678", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
# d = k.encrypt(sendMsg)
# 
# print("Decrypted: %r" % k.decrypt(sendMsg))
# assert k.decrypt(d) == clientMsg

