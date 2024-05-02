from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from data.turno import Turno
class Turnos():
    def __init__(self,interfaz) :
        self.interfaz = interfaz
        self.coneccionTurnos = Turno()
        self.datosProfesionales = self.coneccionTurnos.obtenerProfesionales()
        self.datosPacientes = self.coneccionTurnos.obtenerPacientes()
        self.configurarPacientes()
        self.configurarProfesionales()

    def configurarPacientes(self):
        for paciente in self.datosPacientes:
            self.interfaz.comboBoxPaciente.addItem(paciente[3]+", " +paciente[2]+ " DNI: "+paciente[5])
    def configurarProfesionales(self):
            for profesional in self.datosProfesionales:
                 self.interfaz.comboBoxProfesional.addItem(profesional[3]+", " +profesional[2]+ " DNI: "+profesional[5])