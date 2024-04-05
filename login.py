from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys
from data.usuarios import Usuarios
from pantallaPrincipal import PantallaPrincipal
class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login,self).__init__(parent)
        self.setFixedSize(447,458)
        uic.loadUi("ui/login.ui",self)
        self.pushButtonEntrar.clicked.connect(self.login)
        self.usuarios = Usuarios()
        self.pantallaPrincipal = None
    def login(self):
        usuario = self.lineEditUsuario.text()
        contrasenia = self.lineEditContrasenia.text()
        if usuario == "" or contrasenia == "":
            self.labelMensaje.setText("Rellene todos los campos")
        else:
            respuesta = self.usuarios.login(usuario,contrasenia)
            if respuesta[0] == True:
                self.pantallaPrincipal = PantallaPrincipal(respuesta[1][0])
                self.pantallaPrincipal.show()
                self.close()
                
            else:
                self.labelMensaje.setText(respuesta[1][0])
        




app = QApplication(sys.argv)
object = Login()
object.show()
app.exec_()