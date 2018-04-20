#/usr/bin/env python
#coding:utf-8

#简单并发服务器
import socketserver

#创建一个类来继承socketserver下的BaseRequestHandler类
class MyServer(socketserver.BaseRequestHandler):
    # 要想实现并发效果必须重写父类中的handle方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
    def handle(self):
        while True:
            # 上面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了。
            #还替我们包装了包括bind()、listen()、accept()方法。
            conn = self.request
            #addr = self.client_address
            while True:
                accept_data = str(conn.recv(1024), encoding='utf-8')
                print(accept_data)
                if accept_data == 'byebye':
                    break
                send_data = bytes(input(">>>>>>"), encoding='utf-8')
                conn.sendall(send_data)
            conn.close()
            
if __name__ == '__main__':
    #传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MyServer)
    # 通过调用对象的serve_forever()方法来激活服务端
    server.serve_forever()
    