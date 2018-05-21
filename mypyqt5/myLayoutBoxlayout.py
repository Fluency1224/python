#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        #我们使用HBoxLayout和QVBoxLayout并添加伸展因子，在窗口的右下角显示两个按钮
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        #创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        #创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())