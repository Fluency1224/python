#/usr/bin/env python
#coding:utf-8

#数据库查询
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
cursor = conn.cursor()
#执行数据库指令 
cursor.execute("select * from userinfo")
#获取指令得到的所有信息
data = cursor.fetchall()
#关闭连接
cursor.close ()  
conn.close ()


print(data)