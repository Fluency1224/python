#/usr/bin/env python
#coding:utf-8
'''
另一种导入方法

temp = 'sys'
mydemo = __import__(temp)

print(mydemo.path)
'''
'''
反射解决问题为：把你导入的模块当做字符串
通过对字符串的判断，导入不通的模块
这个功能跟C中的宏有相似功能、方便以后的替换、你赋给什么值就导入什么
'''

mysqlite = 'sys'
fun = 'path'

mysqlitemode = __import__(mysqlite)

myfunc = getattr(mysqlitemode, fun)

print(myfunc)