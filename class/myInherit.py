#/usr/bin/env python
#coding:utf-8

#class的继承
class Father:
    def __init__(self):
        print('Father __init__')
    def Func(self):
        print('Father class')
    def Foo(self):
        print('Father class')
    
class Son(Father):
    def __init__(self):
        print('Son __init__')
        #子类中调用父类的构造函数的两种方式（显式调用）
        Father.__init__(self)
        super(Son,self).__init__()
    def Func(self):
        print('Son class')
#父类对象创建       
f1 = Father()
#子类对象创建
#与C++不同的是，创建子类对象不会调用父类的构造函数
#但是父类中的构造函数可以当做一个方法来被子类调用
s1 = Son()
#父类函数调用
f1.Func()
#子类函数调用
s1.Func()
s1.Foo()