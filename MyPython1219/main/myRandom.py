#/usr/bin/env python
#coding:utf-8
'''
生成随机数的相关函数
'''
import random

print(random.random())
print(random.randint(1,3))
print(random.randrange(1,3))

'''
生成一个六位验证码
'''
code = []
for i in range(6):
    if i == random.randint(1,9):
        code.append(str(random.randint(1,9)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print(''.join(code))