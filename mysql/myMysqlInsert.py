#/usr/bin/env python
#coding:utf-8

#数据库增加操作
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
cursor = conn.cursor()

myInsertOder = "insert into userinfo(id,name,passwd) values(%s,%s,%s)"
myArgs = ('01','fluency','123456')
#执行数据库指令 
cursor.execute(myInsertOder,myArgs)
#提交更改
conn.commit()
#关闭连接
cursor.close ()  
conn.close ()


