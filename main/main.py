'''
Created on 2017年12月19日
@author: fluency
'''
from demo import myDemo
if __name__ == '__main__':
    pass

i_a = 10
i_b = 2

ret = myDemo.Sub(i_a, i_b)
print(ret)

ret = myDemo.Sum(i_a, i_b)
print(ret)

print (__name__, __file__, __doc__)
