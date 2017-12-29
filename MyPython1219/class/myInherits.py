#/usr/bin/env python
#coding:utf-8

#class的多继承

class A:
    def __init__(self):
        print('A __init__')
    def Func(self):
        print('A Func')
        
class B(A):
    def __init__(self):
        print('B __init__')
        
class C(A):
    def __init__(self):
        print('C __init__')
    def Func(self):
        print('C Func')
        
class D(B,C):
    def __init__(self):
        print('D __init__')

        
d1 = D()
d1.Func()