#/usr/bin/env python
#coding:utf-8
from abc import ABCMeta, abstractmethod

#抽象类
class A:
    __metaclass_=ABCMeta   
    @abstractmethod
    def Func(self):
        pass
    
class B(A):
    def __init__(self):
        print('B __init__')
    
B()