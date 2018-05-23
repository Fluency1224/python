import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
 
 
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
 
    def mouseMoveEvent(self, e):
 
        if e.buttons() != Qt.RightButton:
            return
 
        mimeData = QMimeData()
 
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
 
        dropAction = drag.exec_(Qt.MoveAction)
 
    def mousePressEvent(self, e):
 
        QPushButton.mousePressEvent(self, e)
 
        if e.button() == Qt.LeftButton:
            print('press')
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.setAcceptDrops(True)
 
        self.button = Button('Button', self)
        self.button.move(100, 65)
 
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)
 
    def dragEnterEvent(self, e):
        e.accept()
 
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
 
        e.setDropAction(Qt.MoveAction)
        e.accept()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  