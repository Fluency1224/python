#/usr/bin/env python
#coding:utf-8

import socket
import requests

def GetIp():
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
    return ip

def GetInfo(ip):    
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url = "http://%s/cgi-bin/am335info.txt"% ip
    html_cn = requests.get(url, head)
    print(html_cn)
    return html_cn
    
def main():
    Am335Ip = GetIp()
    GetInfo(Am335Ip)
    

if __name__ == '__main__':
    main()