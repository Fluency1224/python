#/usr/bin/env python
#coding:utf-8

import paramiko
#做一个sshclient 通过密码登录远程服务器
# 创建SSH对象
ssh = paramiko.SSHClient()
print('创建SSH对象')
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('允许连接不在know_hosts文件中的主机')
# 连接服务器
ssh.connect('192.168.1.149', port=22, username='fluency', password='1')
print('连接服务器')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print('执行命令')
# 获取命令结果
result = stdout.read()
print('获取命令结果\n',result.decode('utf-8'))
# 关闭连接
ssh.close()
print('关闭连接')

#通过秘钥登录
