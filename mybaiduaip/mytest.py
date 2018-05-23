#/usr/bin/env python
#coding:utf-8
from aip import AipOcr
import os 
""" 你的 APPID AK SK """
APP_ID = '11036171'
API_KEY = 'nFtlymGZBLoFkbHNmQP9stnF'
SECRET_KEY = '6LPcxsiRziNZH9URsZTzCnmvYBad4wXx'
 
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
print(client)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        print (child) # .decode('gbk')是解决中文显示乱码问题
        image = get_file_content(child)
        print(client.licensePlate(image))
 
eachFile("image") 

