#/usr/bin/env python
#coding:utf-8
from threading import Thread
from queue import Queue
import time

#创建线程类
class Producer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self)
        '''
        name生产者名字  queue队列
        '''
        self.__name = name
        self.__queue = queue       
    def run(self):
        while True:
            if self.__queue.full():
                time.sleep(1)
            else:
                self.__queue.put(self.__name)
                #print(self.__name)
                #Thread.run(self)

class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self)
        '''
        name生产者名字  queue队列
        '''
        self.__name = name
        self.__queue = queue
    def run(self):
        while True:
            if self.__queue.empty():
                time.sleep(1)
            else:
                print(self.__queue.get())
                #Thread.run(self)
        
#创建队列、大小10
myqueue = Queue(maxsize=10)
'''
print(myqueue.qsize())
myqueue.put('a')
myqueue.put('s')
print(myqueue.qsize())
print(myqueue.get())
print(myqueue.get())
print(myqueue.qsize())
'''

#创建生产者对象
prd1 = Producer('prd1',myqueue)
prd1.start()
prd2 = Producer('prd2',myqueue)
prd2.start()
prd3 = Producer('prd3',myqueue)
prd3.start()
#创建消费者对象
cnm1 = Consumer('cnm1',myqueue)
cnm1.start()
cnm2 = Consumer('cnm2',myqueue)
cnm2.start()
cnm3 = Consumer('cnm3',myqueue)
cnm3.start()