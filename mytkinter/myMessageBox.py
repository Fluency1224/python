#/usr/bin/env python
#coding:utf-8
import tkinter as tk
from tkinter import messagebox
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')


#按钮

def hit_me():     
    #messagebox.showinfo(title=None, message='This is Fluency!')
    messagebox.showerror(title=None, message='This is Fluency!')
mybtn = tk.Button(window, text='Hit me',width=15,height=2,command=hit_me)
mybtn.pack()
window.mainloop()