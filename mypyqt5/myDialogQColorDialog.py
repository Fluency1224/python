import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #显示一个按钮和一个QFrame。QFrame的背景为黑色。通过QColorDialog,我们可以改变它的背景
        col = QColor(0, 0, 0) 
 
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
 
        self.btn.clicked.connect(self.showDialog)
 
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):
        #初始化QFrame的颜色为黑色
        col = QColorDialog.getColor()
        #弹出QColorDialog
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())