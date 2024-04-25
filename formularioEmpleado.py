from PyQt5 import QtCore,QtWidgets,uic

from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from data.empleados import Empleados
class FormularioEmpleados(QtWidgets.QMainWindow):
    def __init__(self ,idUsuario,apellido,nombre,rol,tabla,parent=None):
        super(FormularioEmpleados,self).__init__(parent)
        self.empleadosConeccion = Empleados()
        self.idUsuario = idUsuario
        self.apellido = apellido
        self.nombre = nombre
        self.rol = rol
        self.tabla = tabla

        uic.loadUi("ui/formEmpleado.ui",self)

        #debajo de esto modificar
        self.labelNombre.setText(self.nombre)
        self.labelApellido.setText(self.apellido)
        self.lineEditRol.setText(self.rol)

        self.btnCancelar.clicked.connect(self.close)
        self.btnGuardarCambios.clicked.connect(self.guardarCambios)
    
    def guardarCambios(self):
        self.empleadosConeccion.actualizarRol(self.idUsuario,self.lineEditRol.text())
        self.tabla.actualizar()
        self.close()