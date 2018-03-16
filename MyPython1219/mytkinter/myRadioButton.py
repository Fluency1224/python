#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本

mylab = tk.Label(window, text='This is FLuency!', 
                 bg='#ceea56',font=('Arial',12),width=20,height=5)
mylab.pack()

#选择按钮
def print_selection():
    mylab.config(text='You have selected ' + var.get())

var = tk.StringVar()
myRbtn1 = tk.Radiobutton(window, text='Option A', variable=var, font=('Arial',12),
                        value='A', command=print_selection)
myRbtn1.pack()
myRbtn2 = tk.Radiobutton(window, text='Option B', variable=var, font=('Arial',12),
                        value='B', command=print_selection)
myRbtn2.pack()
myRbtn3 = tk.Radiobutton(window, text='Option C', variable=var, font=('Arial',12),
                        value='C', command=print_selection)
myRbtn3.pack()
window.mainloop()
