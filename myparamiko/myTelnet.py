#/usr/bin/env python
#coding:utf-8

def do_telnet(Host, username, password, finish, commands):  
    import telnetlib  
    
    # 连接Telnet服务器  
    tn = telnetlib.Telnet(Host)  
       
    # 输入登录用户名  
    tn.read_until(b"login: ")  
    tn.write(username.encode('ascii') + b"\n") 
      
    # 输入登录密码  
    if password:  
        tn.read_until(b"Password: ")  
        tn.write(password.encode('ascii') + b"\n")  
        print('登录成功！')
        
    # 登录完毕后执行命令  
    tn.write(b"ifconfig\n")  
    tn.write(b"exit\n")  
    
    #输出获取的结果
    print(tn.read_all().decode('utf-8'))  
    #执行完毕后，终止Telnet连接（或输入exit退出）  
    #tn.close() # tn.write('exit\n')  
  
if __name__=='__main__':  
    # 配置选项  
    Host = "192.168.1.149"  
    username = 'fluency'
    password = '1'  
    finish = ':~$ '      # 命令提示符  
    commands = ['echo "test"']  
    do_telnet(Host, username, password, finish, commands)  
    
'''
import getpass  
import telnetlib  
  
HOST = "localhost"  
user = input("Enter your remote account: ")  
password = getpass.getpass()  
  
tn = telnetlib.Telnet(HOST)  
  
tn.read_until(b"login: ")  
tn.write(user.encode('ascii') + b"\n")  
if password:  
    tn.read_until(b"Password: ")  
    tn.write(password.encode('ascii') + b"\n")  
  
tn.write(b"ls\n")  
tn.write(b"exit\n")  
  
print(tn.read_all().decode('ascii'))  
'''