#/usr/bin/env python
#coding:utf-8
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = socket.gethostname()
port = 1700

d_bw = { 0:'7.8 kHz', 1:'10.4 kHz' , 2:'15.6 kHz', 3:'20.8kHz', 4:'31.25 kHz', 5:'10.4 kHz',
      6:'41.7 kHz', 7:'62.5 kHz', 8:'125 kHz', 9:'250 kHz'}
d_cr = { 1:'4/5', 2:'4/6' , 3:'4/7', 4:'4/8'}

sock.bind((name, port))
print("warting for connect...")

while True:  
#     print("-------------------")
    data,addr = sock.recvfrom(1024)
#     for i in range(0,11):       
#         print(hex(data[i]))
    
    if hex(data[16]) == hex(0x00):
        print("------------设备信息-------------------")
        print('MAC:',str(hex(data[0]).split('x')[1])+':'+str(hex(data[1]).split('x')[1])+':'+str(hex(data[2]).split('x')[1])+':'+
              str(hex(data[3]).split('x')[1])+':'+str(hex(data[4]).split('x')[1])+':'+str(hex(data[5]).split('x')[1]))
        bw = (data[6] & 0xf0) >> 4
        print('带宽:',d_bw[bw])
        sf = data[6] & 0x0f
        print('扩频因子:',sf)
        cr = (data[7] & 0xf0) >> 4
        print('编码率:',d_cr[cr])
        pa = data[7] & 0x0f
        print('增益:',pa)
        print('网关工作频率：','0x'+str(hex(data[11]).split('x')[1])+str(hex(data[10]).split('x')[1])+
              str(hex(data[9]).split('x')[1])+str(hex(data[8]).split('x')[1]))
        t = ((data[15] << 24) & 0xff000000) + ((data[14] << 16) & 0xff0000) + ((data[13] << 8) & 0xff00) + (data[12] & 0xff)
        localtime = time.asctime(time.localtime(t))
        print('设备时间:',localtime)
    else:
        print("------------节点信息-------------------")
        print('头：', hex(data[0]))
        print('随机数：',hex(data[1]))
        print('温度：', str(data[2] - 50)+'℃')
        print('湿度：', str(data[3])+'%')
        print('节点序列号：',str(hex(data[4]).split('x')[1])+str(hex(data[5]).split('x')[1])+str(hex(data[6]).split('x')[1])+str(hex(data[7]).split('x')[1])+
              str(hex(data[8]).split('x')[1])+str(hex(data[9]).split('x')[1])+str(hex(data[10]).split('x')[1])+str(hex(data[11]).split('x')[1]))
        t = ((data[15] << 24) & 0xff000000) + ((data[14] << 16) & 0xff0000) + ((data[13] << 8) & 0xff00) + (data[12] & 0xff)
        localtime = time.asctime(time.localtime(t))
        print('设备时间:',localtime)
#         print("------------数据错误-------------------")
#         for i in range(0,11):       
#             print(hex(data[i]))
         
sock.close()



