#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
mylab = tk.Label(window, text='This is FLuency!', 
                 bg='#ceea56',font=('Arial',12),width=20,height=2)
mylab.pack()


#按钮
mybtn = tk.Button(window, text='Hit me',width=15,height=2)
mybtn.pack()

#尺度
def print_selection(v):
    mylab.config(text='You have selected ' + v)
    
myscal = tk.Scale(window, label='Try me',from_=5, to=11,
                  orient=tk.HORIZONTAL,length=200,showvalue=0,
                  tickinterval=3, resolution=0.01,command=print_selection)
myscal.pack()
window.mainloop()