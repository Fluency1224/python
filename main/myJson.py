#/usr/bin/env python
#coding:utf-8

import pickle
import json

#将字典写入文件,pickle序列化（dumps）
'''
mylist = ['fluency',11,'book',123,1]

dumpsed = pickle.dumps(mylist)
print(list(dumpsed))
print(type(mylist))
loadsed = pickle.loads(dumpsed)
print(loadsed)
print(type(loadsed))
'''
def func1(name):
    print('hello..',name)

a = {
    'name':'fluency',
    'age':22,
    'salary':2000,
    'arge':func1
}
with open('C:/Users/fluency/Desktop/myfile01.txt','wb') as f:
    pickle.dump(a,f)
    
with open('C:/Users/fluency/Desktop/myfile01.txt','rb') as f1:
    line = pickle.loads(f1.read())
    print(line['arge']('lili'))
    
#将字典写入文件,JSON序列化（dumps）
b = {
    'name':'fluency',
    'age':22,
    'salary':2000
}

with open('C:/Users/fluency/Desktop/myfile02.txt','w') as f:
    f.write(json.dumps(b))
#反序列化    
with open('C:/Users/fluency/Desktop/myfile02.txt','r') as f1:
    line = json.loads(f1.read())
    print(line['name'])
    print(line['age'])
    print(line['salary'])