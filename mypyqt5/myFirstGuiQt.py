#/usr/bin/env python
#coding:utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setWindowTitle("Hello World")
    sys.exit(app.exec_())