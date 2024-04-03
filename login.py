from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys
class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login,self).__init__(parent)
        self.setFixedSize(447,458)
        uic.loadUi("ui/login.ui",self)

    def login(self):
        pass




app = QApplication(sys.argv)
object = Login()
object.show()
app.exec_()