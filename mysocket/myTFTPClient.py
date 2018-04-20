#/usr/bin/env python
#coding:utf-8

import socket
#import sys
import os

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)

container = {'key':'','data':''}
while True:
    myinput = input('path:')
    cmd,path = myinput.split('|') 
    file_name = os.path.basename(path)
    file_size=os.stat(path).st_size
    sk.send(cmd+"|"+file_name+'|'+str(file_size))
    send_size = 0
    f = open(path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 >file_size:
            data = f.read(file_size-send_size)
            Flag = False
        else:
            data = f.read(1024)
            send_size+=1024
        sk.send(data)
    f.close()
    
sk.close()