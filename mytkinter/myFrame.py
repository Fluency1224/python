#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
mylab = tk.Label(window, text='on the window', 
                 bg='#ceea56',font=('Arial',12),width=20,height=5)
mylab.pack()

#框架
myfrm = tk.Frame(window).pack()
myfrm_left = tk.Frame(myfrm)
myfrm_right = tk.Frame(myfrm)

myfrm_left.pack(side='left')
myfrm_right.pack(side='right')

tk.Label(myfrm_left,text='on the frm_left').pack()
tk.Label(myfrm_left,text='on the frm_left').pack()

tk.Label(myfrm_right,text='on the frm_right').pack()


window.mainloop()