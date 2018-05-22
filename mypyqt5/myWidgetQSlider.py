import sys
from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('audio.ico'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):
 
        if value == 0:
            self.label.setPixmap(QPixmap('audio.ico'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.ico'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.ico'))
        else:
            self.label.setPixmap(QPixmap('max.ico'))
            
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    