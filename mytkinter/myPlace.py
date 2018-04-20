#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
# tk.Label(window, text='This is FLuency!').pack(side='top')
# tk.Label(window, text='This is FLuency!').pack(side='bottom')
# tk.Label(window, text='This is FLuency!').pack(side='left')
# tk.Label(window, text='This is FLuency!').pack(side='right')

#grid
# for i in range(4):
#     for j in range(3):
#         #tk.Label(window, text='This is FLuency!').grid(row=i, column=j, padx=10, pady=10)
#         tk.Label(window, text='This is FLuency!').grid(row=i, column=j, ipadx=10, ipady=10)

#place
tk.Label(window, text='This is FLuency!').place(x=10, y=100,anchor='nw')

window.mainloop()