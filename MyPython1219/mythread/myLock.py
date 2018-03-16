#/usr/bin/env python
#coding:utf-8

import time
import threading

mynum = 0

def run(n):
    mylcok.acquire()
    time.sleep(1)
    global mynum
    mynum += 1
    mylcok.release()
    print(mynum)

mylcok = threading.Lock()  
for i in range(10):
    t = threading.Thread(target=run,args=(i,))
    t.start()
    t.join()
    
#信号量
#myevent = threading.Event()