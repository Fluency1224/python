#/usr/bin/env python
#coding:utf-8

class Man:
    #静态变量
    sex = '男'
    #静态方法 
    @staticmethod
    def run():
        print('everyone can run')    
    #动态变量  
    def __init__(self, name, age, bloodtype):
        self.name = name
        self.age = age
        #私有变量（只有通过定义方法来间接访问）
        self.__bloodtype = bloodtype
    #动态方法
    def fly(self):
        print(self.name,'can fly')
    def show_bloodtype(self):
        print('bloodtype',self.__bloodtype)
    def show_study(self):
        self.__study()
    #私有方法(也只能通过动态方法间接访问，对象无法直接访问)
    def __study(self):
        print(self.name,'can study')
    #特性方法(在引用的时要当做变量来引用，不用加括号)
    @property
    def swim(self):
        print(self.name,'can swim')
    
   
p1 = Man('fluency',18,'AB')
print(Man.sex)
print(Man.run())

print('name:',p1.name,'\nsex:',p1.sex,'\nage:',p1.age)
#print('bloodtype',p1.__bloodtype) 访问不到，因为是私有变量 
p1.show_bloodtype()
p1.show_study()
p1.run()
p1.fly()
p1.swim



    