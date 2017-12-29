#/usr/bin/env python
#coding:utf-8
'''
import re 

#正则表达式
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)')

print("p.pattern:", p.pattern)
print("p.flags:", p.flags)
print("p.groups:", p.groups)
print("p.groupindex:", p.groupindex)

a = re.compile(r'\d+')
for m in a.finditer('one1two2three3four4'):
    print(m.group(),)
'''

#时间模块处理
import time

print(time.time())
print(time.gmtime())
print(time.strftime('%Y-%m-%d %H-%M-%S'))#格式化输出时间
print(time.localtime())
print(time.asctime())
print(time.process_time())
print(time.clock())