from PyQt5 import QtCore,QtWidgets,uic
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QDate,QTime
from data.turno import Turno
import datetime
class Turnos():
    def __init__(self,interfaz) :
        self.interfaz = interfaz
        self.coneccionTurnos = Turno()
        self.datosProfesionales = self.coneccionTurnos.obtenerProfesionales()
        self.datosPacientes = self.coneccionTurnos.obtenerPacientes()
        self.configurarPacientes()
        self.configurarProfesionales()
        self.configurarFecha()
        self.configurarHora()
        self.interfaz.btnCancelarTurnos.clicked.connect(self.cancelar)
        self.interfaz.btnGuardarCambiosTurnos.clicked.connect(self.guardarCambios)
    def configurarPacientes(self):
        for paciente in self.datosPacientes:
            self.interfaz.comboBoxPaciente.addItem(paciente[3]+", " +paciente[2]+ " DNI: "+paciente[5])
    def configurarProfesionales(self):
            for profesional in self.datosProfesionales:
                 self.interfaz.comboBoxProfesional.addItem(profesional[3]+", " +profesional[2]+ " DNI: "+profesional[5])
    def configurarFecha(self):
        ahora = datetime.datetime.now()

        self.interfaz.dateEditTurno.setDate(QDate(ahora.year,ahora.month,ahora.day))
    def configurarHora(self):
        ahora = datetime.datetime.now()
        self.interfaz.timeEditFecha.setTime(QTime(ahora.hour,ahora.minute,ahora.second))
    def resetearComboBoxs(self):
          self.interfaz.comboBoxPaciente.setCurrentIndex(0)
          self.interfaz.comboBoxProfesional.setCurrentIndex(0)
    def cancelar(self):
        self.configurarFecha()
        self.configurarHora()
        self.resetearComboBoxs()
    def guardarCambios(self):
        posicionPaciente = self.interfaz.comboBoxPaciente.currentIndex()
        posicionProfesional = self.interfaz.comboBoxProfesional.currentIndex()

        idPaciente = self.datosPacientes[posicionPaciente][0]
        idProfesional = self.datosProfesionales[posicionProfesional][0]

        qfecha = self.interfaz.dateEditTurno.date()

        fecha = f"{qfecha.year()}-{qfecha.month()}-{qfecha.day()}"

        qhora = self.interfaz.timeEditFecha.time()

        hora =  f"{qhora.hour()}:{qhora.minute()}:00"

        self.coneccionTurnos.insertarTurno(idPaciente,idProfesional,fecha,hora)
        print("Exitoso")
