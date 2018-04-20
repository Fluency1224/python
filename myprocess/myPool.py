#/usr/bin/env python
#coding:utf-8

from multiprocessing import Pool
import time

def func(x):
    print(x*x)
    time.sleep(2)
    return x*x

if __name__ == '__main__':

    pool = Pool(processes=5)
    res_list = []
    
    for i in range(10):
        res = pool.apply_async(func, [i,])
        
        print('----',i)
        res_list.append(res)
        
    for r in res_list:
        print(r.get())
    