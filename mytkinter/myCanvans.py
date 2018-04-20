#/usr/bin/env python
#coding:utf-8
import tkinter as tk
#窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x500')

#图片
image_file = tk.PhotoImage(file='timg.gif')

#画布
mycanvas = tk.Canvas(window, bg='#ceea56', height=450, width=500)
mycanvas.pack()
#anchor属性是锚定 参数有：NW center
image = mycanvas.create_image(0,0,anchor='nw',image=image_file)
#各种图像定义
x0, y0, x1, y1 = 50, 50, 80, 80 
#直线
line = mycanvas.create_line(x0, y0, x1, y1)
#圆形
oval = mycanvas.create_oval(x0, y0, x1, y1,fill='red')
#按钮
def move_it():
    mycanvas.move(oval, 0, 2)
    pass
mybtn = tk.Button(window, text='move', command=move_it)
mybtn.pack()
window.mainloop()