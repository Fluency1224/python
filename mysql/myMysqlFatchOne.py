#/usr/bin/env python
#coding:utf-8

#一个一个取读取的数据
import pymysql
#连接数据库 打开dataese
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='fluency')
#cursor = conn.cursor()
cursor = conn.cursor(pymysql.cursors.DictCursor)
#执行数据库指令 
cursor.execute("select * from userinfo")
#获取指令得到的信息
data1 = cursor.fetchone()
data2 = cursor.fetchone()
data3 = cursor.fetchone()
#scroll函数跟C中的lseek函数类似，让操作指针去到你指定的位置（absolute是绝对定位，relative是相对定位）
cursor.scroll(0,mode = 'absolute')
data4 = cursor.fetchone()
cursor.scroll(-1,mode = 'relative')
data5 = cursor.fetchone()
#关闭连接
cursor.close ()  
conn.close ()


print(data1)
print(data2)
print(data3)
print(data4)
print(data5)