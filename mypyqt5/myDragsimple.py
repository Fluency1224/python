import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

#重新实现某些方法才能使QPushButton接受拖放操作。因此我们创建了继承自QPushButton的Button类
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        #使该控件接受drop(放下)事件
        self.setAcceptDrops(True)
    #重新实现了dragEnterEvent()方法，并设置可接受的数据类型(在这里是普通文本)
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    #重新实现dropEvent()方法，我们定义了在drop事件发生时的行为。这里我们改变了按钮的文字
    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  