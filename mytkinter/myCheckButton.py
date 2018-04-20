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
    #判断选择按钮的value
    if(var1.get() == 0) & (var2.get() == 0):
        mylab.config(text='You no selected ')
    elif(var1.get() == 1) & (var2.get() == 0):
        mylab.config(text='You selected Python')
    elif(var1.get() == 1) & (var2.get() == 0):
        mylab.config(text='You selected C++')
    else:
        mylab.config(text='You selected tow')
var1 = tk.IntVar()
var2 = tk.IntVar()
mycbtn1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0, font=('Arial',12),
                         command=print_selection)
mycbtn1.pack()
mycbtn2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0, font=('Arial',12),
                         command=print_selection)
mycbtn2.pack()
window.mainloop()