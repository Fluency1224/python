#/usr/bin/env python
#coding:utf-8

#数据库更改操作
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
cursor = conn.cursor()

myInsertOder = "update userinfo set passwd = %s where id = %s"
myArgs = ('666','02')
#执行数据库指令 
cursor.execute(myInsertOder,myArgs)
#提交更改
conn.commit()
#关闭连接
cursor.close ()  
conn.close ()