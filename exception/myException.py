#/usr/bin/env python
#coding:utf-8
'''
AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 尝试访问一个没有申明的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
Exception 所有异常类的父类
'''
#异常的使用
names = ['wt','gxb']
data = {}
try:
    names[3]
    data['name']
    open('b.txt')
except IndexError as e:
    print('there is not exist this key',e)
except Exception as e:
    print('I can`t find this error!!!',e)
else:
    print('it`s ok!!')
finally:
    print('fluency')
    
#手动定义自己的异常（通过继承Exception类）

class MyException(Exception):
    def __init__(self,myErrorMsg):
        self.error = myErrorMsg
    def __str__(self, *args, **kwargs):
        return self.error
#创建自定义异常的对象
myerror = MyException('myerror')
print(myerror)
#手动出发自己创建的异常
try:
    raise MyException('myerror')
except MyException as e:
    print(e)