from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys
from data.usuarios import Usuarios
from data.empleados import Empleados
from tableEmpleados import TableEmpleados

class PantallaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, idUsuario,login ,parent=None):
        super(PantallaPrincipal,self).__init__(parent)
        self.idUsuario = idUsuario
        self.login = login
        self.usuarios = Usuarios()
        self.empleadosConeccion = Empleados()
        
        self.usuarios.actualizarUltimoAcceso(self.idUsuario)
        self.datosUsuario = self.usuarios.obtenerUsuario(self.idUsuario)
        uic.loadUi("ui/ventanaPrincipal.ui",self)
        #llamar a los elementos de ui
        self.btnCerrarSesion.clicked.connect(self.cerrarSesion)
        self.labelUsuario.setText("Usuario: " + self.datosUsuario[0][2]+ ", "+self.datosUsuario[0][3] )
    
        self.labelTipoUsuario.setText(self.usuarios.obtenerTipoUsuario(self.datosUsuario[0][1])[0][0].upper())
        self.btnMenu.clicked.connect(self.deslizarMenu)
        self.btnAdministracion.clicked.connect(self.administracion)
        self.btnEmpleados.clicked.connect(self.empleados)
        self.btnTurnos.clicked.connect(self.turnos)
        self.btnCalendario.clicked.connect(self.calendario)
        self.pantallas = []
        self.pantallas.append(self.frameAdministracion)
        self.pantallas.append(self.frameTurnos)
        self.pantallas.append(self.frameCalendario)
        self.pantallas.append(self.frameBienvenida)
        self.pantallas.append(self.frameEmpleados)

        self.bienvenida()
        ((3,3,""),  )
        if self.datosUsuario[0][1] == 1:
            pass
        elif self.datosUsuario[0][1] == 2:
            self.btnAdministracion.hide()
        elif self.datosUsuario[0][1] == 3:
            self.btnAdministracion.hide()
            self.btnEmpleados.hide()
        else:
            self.btnAdministracion.hide()
            self.btnEmpleados.hide()
            self.btnCalendario.hide()

        

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
    def bienvenida(self):
        self.labelTituloPantalla.setText("Inicio")
        self.ocultarPantallasMenos(self.frameBienvenida)
    
    def administracion(self):
        self.labelTituloPantalla.setText("Administracion")
        self.ocultarPantallasMenos(self.frameAdministracion)
    def empleados(self):
        self.labelTituloPantalla.setText("Empleados")
        self.ocultarPantallasMenos(self.frameEmpleados)
        self.empleadosDatos = self.empleadosConeccion.obtenerEmpleados()
        self.tablaEmpleados = TableEmpleados(self)
  
    def turnos(self):
        self.labelTituloPantalla.setText("Turnos")
        self.ocultarPantallasMenos(self.frameTurnos)

    def calendario(self):
        self.labelTituloPantalla.setText("Calendario")
        self.ocultarPantallasMenos(self.frameCalendario)
    def ocultarPantallasMenos(self,pantallaAMostrar):
        for pantalla in self.pantallas:
            pantalla.hide()
        pantallaAMostrar.show()
    def cerrarSesion(self):
        self.close()
        self.login.reiniciar()

app = QApplication(sys.argv)

object = PantallaPrincipal(1,None)
object.show()
app.exec_()