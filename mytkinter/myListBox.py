#/usr/bin/env python
#coding:utf-8
import tkinter as tk

#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#文本
var1 = tk.StringVar()
mylab = tk.Label(window, textvariable=var1, text='This is FLuency!', 
                 bg='#ceea56',font=('Arial',12),width=20,height=5)
mylab.pack()

#按钮
def print_selection():
    value = mylistbox.get(mylistbox.curselection())
    var1.set(value)
    
mybtn1 = tk.Button(window, text='print selection',width=15,height=2,command=print_selection)
mybtn1.pack()

#列表
var2 = tk.StringVar()
var2.set((11,22,33,44))
mylistbox = tk.Listbox(window, listvariable=var2)
mylistbox.pack()

list_items = [1,2,3,4]
for item in list_items:
    mylistbox.insert('end', item)

mylistbox.insert(1,'fluency')
mylistbox.delete(2)

window.mainloop()
