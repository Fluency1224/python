#/usr/bin/env python
#coding:utf-8

#数据库操作测试、获取MySQL版本
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='mysql')
cursor = conn.cursor()  
cursor.execute ("SELECT VERSION()")  
row = cursor.fetchone()  
print("MySQL server version:", row[0])
cursor.close ()  
conn.close ()  