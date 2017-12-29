#/usr/bin/env python
#coding:utf-8

#插入大量数据可以采用列表的方式
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
cursor = conn.cursor()

myInsertOder = 'insert into userinfo(id,name,passwd) values(%s,%s,%s);'
params = ('04','xiaoming','123456')
myUserInfoList = [('04','xiaom','123456'),
                  ('05','xiaoh','123456'),
                  ('06','xiaoa','123456'),
                  ('07','xiaob','123456'),
                  ('08','xiaoc','123456'),]

#执行数据库指令 (返回值查看影响条数)
ret = cursor.executemany(myInsertOder,myUserInfoList)
#提交更改
conn.commit()
#关闭连接
cursor.close ()  
conn.close ()

print(ret)