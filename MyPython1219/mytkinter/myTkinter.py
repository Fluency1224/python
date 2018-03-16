#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
var = tk.StringVar()
mylab = tk.Label(window, textvariable=var, text='This is FLuency!', 
                 bg='#ceea56',font=('Arial',12),width=20,height=5)
mylab.pack()

#按钮
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

mybtn = tk.Button(window, text='Hit me',width=15,height=2,command=hit_me)
mybtn.pack()
window.mainloop()