#/usr/bin/env python
#coding:utf-8

#数据库删除操作
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
cursor = conn.cursor()

myInsertOder = "delete from userinfo where id = %s"
myArgs = ('01')
#执行数据库指令 
cursor.execute(myInsertOder,myArgs)
#提交更改
conn.commit()
#关闭连接
cursor.close ()  
conn.close ()