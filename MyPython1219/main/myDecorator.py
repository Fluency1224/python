#/usr/bin/env python
#coding:utf-8
'''
#装饰器的原则及构成：
# 原则：
# 1、不能修改被装饰函数的源代码。
# 2、不能修改被装饰函数的调用方式。
# 3、不能改变被装饰函数的执行结果。
# 装饰器对被装饰函数是透明的。
#
# 如何理解装饰器
# 1、函数即“变量”
# 2、高阶函数
# a:把一个函数名作为实参传递给另外一个函数
# b:返回值中包含函数名
# 3、嵌套函数
#
# 在一个函数体内声明另一个函数称为函数的嵌套
'''

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return warpper
@timmer
def func1():
    time.sleep(5)
    print("I'm a test!")
func1()

def outer(fun):
    def wrapper():
        print('666')
        fun()
    return wrapper

@outer
def Fun1():
    print('Fun1') 
    
@outer    
def Fun2():
    print('Fun2')
    
@outer    
def Fun3():
    print('Fun3')

Fun1()    
Fun2()
Fun3()

'''
#带参数的装饰器 在函数执行前后执行任意的函数
def before_func():
    print('before_func')
    pass
def after_func():
    print('after_func')
    pass
def filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_ret = before_func(request,kargs)
            if(before_ret!= None):
                return before_ret
            
            main_ret = main_func(request,kargs)
            if(main_ret != None):
                return main_ret
            after_ret = after_func(request,kargs)
            if(after_ret != None):
                return after_ret
        return wrapper
    return outer

@filter(before_func,after_func)
def List(request,kargs):
    pass  
request = 'request'
kargs = 'kargs'
List(request,kargs)     
'''   