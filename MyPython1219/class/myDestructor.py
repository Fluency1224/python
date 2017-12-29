#/usr/bin/env python
#coding:utf-8

#构造函数和析构函数（跟c++中的东西差不多）
class Foo:
    #构造函数
    def __init__(self):
        print('类被构造了')
    #析构函数
    def __del__(self):
        print('类被析构了')  
    #__call__方法
    def __call__(self):
        print('call方法的执行')

#当对象被创建时，执行__init__函数（构造函数）。
#对象被销毁时，执行__del__函数（析构函数）
p1 = Foo()
#call方法是中特殊调用
p1()