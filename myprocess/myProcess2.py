#/usr/bin/env python
#coding:utf-8

import time
import random
from multiprocessing import Process

def piao(name):
    print('%s piao' %name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' %name)


if __name__ == '__main__':
    p1=Process(target=piao,args=('e',)) #必须加,号
    p2=Process(target=piao,args=('a',))
    p3=Process(target=piao,args=('w',))
    p4=Process(target=piao,args=('y',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')