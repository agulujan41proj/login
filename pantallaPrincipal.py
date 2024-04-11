from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys
from data.usuarios import Usuarios
class PantallaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, idUsuario ,parent=None):
        super(PantallaPrincipal,self).__init__(parent)
        self.idUsuario = idUsuario
        self.usuarios = Usuarios()
        self.datosUsuario = self.usuarios.obtenerUsuario(self.idUsuario)
        
        uic.loadUi("ui/ventanaPrincipal.ui",self)
        #llamar a los elementos de ui

        self.labelUsuario.setText("Usuario: " + self.datosUsuario[0][2]+ ", "+self.datosUsuario[0][3] )
    
        self.labelTipoUsuario.setText(self.usuarios.obtenerTipoUsuario(self.datosUsuario[0][1])[0][0].upper())
        self.btnMenu.clicked.connect(self.deslizarMenu)
    def deslizarMenu(self):
        anchoMenu = self.frameMenu.width()
        nuevoAncho = 0
        if anchoMenu == 0:
            nuevoAncho = 300
        self.animation = QtCore.QPropertyAnimation(self.frameMenu,b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(anchoMenu)
        self.animation.setEndValue(nuevoAncho)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
app = QApplication(sys.argv)
object = PantallaPrincipal(1)
object.show()
app.exec_()