import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        vbox = QVBoxLayout()
 
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        
        btn.move(20, 20)
 
        vbox.addWidget(btn)
 
        btn.clicked.connect(self.showDialog)
        
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
 
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
        
    def showDialog(self):
        #创建了一个按钮和一个标签，通过QFontDialog来改变标签的字体
        font, ok = QFontDialog.getFont()
        #getFont()方法返回字体名称和ok参数，如果用户点击了ok他就是True,否则就是false
        if ok:
            self.lbl.setFont(font)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())