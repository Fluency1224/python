#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
mylab = tk.Label(window, bg='#ceea56',font=('Arial',12),width=20,height=5)
mylab.pack()

#菜单
counter = 0
def do_job():
    global counter
    mylab.config(text='do' + str(counter))
    counter += 1

mymenu = tk.Menu(window,font=('Arial',50))
filemenu = tk.Menu(mymenu,tearoff=0)
mymenu.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu = tk.Menu(mymenu,tearoff=0)
mymenu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)
submenu.add_command(label="Submenu2", command=do_job)
submenu.add_command(label="Submenu3", command=do_job)

window.config(menu=mymenu)

window.mainloop()