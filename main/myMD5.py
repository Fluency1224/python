#/usr/bin/env python
#coding:utf-8
'''
MD5加密方式
'''
import hashlib

m = hashlib.md5()

m.update('admin')
print(m.hexdigest())