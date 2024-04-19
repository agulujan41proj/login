from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

class TableEmpleados():
    def __init__(self,interfazPrincipal):
       self.interfaz = interfazPrincipal
       self.tabla = self.interfaz.tableEmpleados
       self.cargarTabla(self.interfaz.empleadosDatos)
    def cargarTabla (self,tuplaEmpleados):
        self.tabla.setHorizontalHeaderLabels(["Id","Apellido","Nombre","Rol","DNI","CUIT","Fecha de nacimiento","Direccion","Email", "Ultimo Acceso","Habilitado"])
        filasI = 0
        for fila in tuplaEmpleados:
            self.tabla.setRowCount(filasI+1)

            if filasI == 0:
                columnasJ = len(tuplaEmpleados[0])
                self.tabla.setColumnCount(columnasJ)
            columnasJ = len(fila)

            for columna in range(columnasJ):
                valor = fila[columna]
                celda = QTableWidgetItem(str(valor))

                self.tabla.setItem(filasI,columna,celda)
            filasI = filasI +1
        
        if filasI == 0:
            self.tabla.clear()
            self.tabla.setHorizontalHeaderLabels(["Id","Apellido","Nombre","Rol","DNI","CUIT","Fecha de nacimiento","Direccion","Email", "Ultimo Acceso","Habilitado"])
            self.tabla.setRowCount(0)