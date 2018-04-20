#/usr/bin/env python
#coding:utf-8

'''
My_dict = {'book':'10',
           'pen':'3',
           'iphone':'8888'}

def show(**kargs):
    for item in kargs.items():
        print(item)

show(**My_dict)
'''

print(list(range(10)))
   
def fun():
    yield 1
       
ret = fun()
print(ret)
