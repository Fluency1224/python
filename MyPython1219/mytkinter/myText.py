#/usr/bin/env python
#coding:utf-8
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#输入框
#myent = tk.Entry(window, show='*') 输入的数据用*代替 常用语密码输入
myent = tk.Entry(window, show=None)
myent.pack()

#按钮
def insert_point():
    var = myent.get()
    mytext.insert('insert', var)

def insert_end():
    var = myent.get()
    mytext.insert('end', var)
    
mybtn1 = tk.Button(window, text='insert point',width=15,height=2,command=insert_point)
mybtn1.pack()
mybtn2 = tk.Button(window, text='insert end',width=15,height=2,command=insert_end)
mybtn2.pack()

#文本框
mytext = tk.Text(window, height=10)
mytext.pack()

window.mainloop()