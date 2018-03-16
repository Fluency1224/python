#/usr/bin/env python
#coding:utf-8

#自定义线程类
from threading import Thread
#继承Thread类
class MyThread(Thread):
    #重写run方法
    def run(self):
        print('thread')
        
def MyFunc():
    print('MyFunc')
    
t1 = MyThread(target=MyFunc)
t1.start()
