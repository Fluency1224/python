#/usr/bin/env python
#coding:utf-8

import socket

def handle_request(client):
    buf = client.recv(1024)
    print(buf)
    client.send(b"HTTP/1.1 200 OK\r\n")
    client.send(b"Content-Type:text/html\r\n\r\n")
    client.send(b"<a fluency </a>")
    
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)
    
    while True:
        connect, address = sock.accept()
        print(address)
        handle_request(connect)
        connect.close()

if __name__ == '__main__':
    main()        