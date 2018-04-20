#/usr/bin/env python
#coding:utf-8
from multiprocessing import Pool

#多进程程序

def func(x):
    return x*x

if __name__ == '__main__':
    p = Pool();
    print(p.map(func,[1,2,3]))