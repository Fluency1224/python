import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        hbox = QHBoxLayout(self)
        #创建了三个QFrame与两个QSplitter。注意在某些主题中这些QSplitter可能会不可见
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
 
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        #使用一个风格框架为了看到QFrame小部件之间的界限
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        #创建一个QSplitter小部件和添加两个帧
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
 
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
 
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
 
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())