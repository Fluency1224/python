#/usr/bin/env python
#coding:utf-8
import tkinter as tk
from tkinter import messagebox
#窗口
window = tk.Tk()
window.title('Fluency Login Program')
window.geometry('600x400')

#图片
image_file = tk.PhotoImage(file='title.gif')
#画布
mycanvas = tk.Canvas(window, bg='#ceea56', height=230, width=600)
mycanvas.pack(side='top')
#anchor属性是锚定 参数有：NW center
image = mycanvas.create_image(0,0,anchor='nw',image=image_file)
#文本
tk.Label(window, text='User Name:',font=('Arial',12)).place(x=150,y=260)
tk.Label(window, text='Passwd:',font=('Arial',12)).place(x=150,y=290)

#文本框
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=250,y=260)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=250,y=290)

#按钮
def login():
    var_usr_name.get()
    var_usr_pwd.get()
    messagebox.showinfo(title='login', message='This is Fluency!')
def sign():
    window_sign = tk.Toplevel(window)
    window_sign.title('Sign Up')
    window_sign.geometry('600x400')
    #文本
    tk.Label(window_sign, text='New Name:',font=('Arial',12)).place(x=150,y=80)
    tk.Label(window_sign, text='New Passwd:',font=('Arial',12)).place(x=150,y=150)
    tk.Label(window_sign, text='Confirm Passwd:',font=('Arial',12)).place(x=150,y=230)
    #文本框
    new_usr_name = tk.StringVar()
    new_usr_name.set('example@python.com')
    new_usr_pwd = tk.StringVar()
    new_usr_confirm_pwd = tk.StringVar()
    sign_usr_name = tk.Entry(window_sign, textvariable=new_usr_name)
    sign_usr_name.place(x=300,y=80)
    sign_usr_pwd = tk.Entry(window_sign, textvariable=new_usr_pwd,show='*')
    sign_usr_pwd.place(x=300,y=150)
    sign_usr_confirm_pwd = tk.Entry(window_sign, textvariable=new_usr_confirm_pwd,show='*')
    sign_usr_confirm_pwd.place(x=300,y=230)
    #按钮
    def done():
        pass
    def cancel():
        pass
    btn_login = tk.Button(window_sign, text='Done', width=5, height=1, command=done)
    btn_login.place(x=200,y=300)
    btn_sign = tk.Button(window_sign, text='Cancel', width=5, height=1, command=cancel)
    btn_sign.place(x=350,y=300)
    
btn_login = tk.Button(window, text='Login', width=5, height=1, command=login)
btn_login.place(x=200,y=330)
btn_sign = tk.Button(window, text='Sign', width=5, height=1, command=sign)
btn_sign.place(x=300,y=330)

if __name__ == '__main__':
    window.mainloop()