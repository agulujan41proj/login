from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import QDate,QRectF,Qt
from data.turno import Turno
class CalendarioSesion():
    def __init__(self,interfaz) :
        self.interfaz = interfaz 
        self.layout = self.interfaz.verticalLayoutCalendario
        self.calendarioWidget = CalendarWidget(self.interfaz)
        self.layout.addWidget(self.calendarioWidget)
    def actualizar(self):
        self.layout.removeWidget(self.calendarioWidget)
        self.calendarioWidget = CalendarWidget(self.interfaz)
        self.layout.addWidget(self.calendarioWidget)
class CalendarWidget(QCalendarWidget):
    def __init__(self,interfaz,parent=None):
        super(CalendarWidget,self).__init__(parent)
        self.coneccionTurnos = Turno()
        self.turnos = self.coneccionTurnos.obtenerTodosLosTurnos()
        self.fechas = []
        for turno in self.turnos : 
            fechaDateTime = turno[3]
            fechaQDate = QDate(fechaDateTime.year,fechaDateTime.month,fechaDateTime.day)
            if fechaQDate not in self.fechas:
                self.fechas.append(fechaQDate)
        
        font = QFont()
        font.setPixelSize(18)
        self.font = font
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

    def paintCell(self,painter,rect,date):
        painter.setRenderHint(QPainter.Antialiasing,True)

        if date in self.fechas:
    
            painter.save()
            painter.drawRect(rect)

            painter.setFont(QFont('Decorative',10))
            painter.setPen(QColor(168,34,3))
            painter.drawText(QRectF(rect),Qt.TextSingleLine|Qt.AlignCenter,str(date.day()))
            painter.setPen(QColor(168,34,3))
            painter.drawText(rect,Qt.AlignCenter,"\nTurno")
            painter.restore()
        else:
             QCalendarWidget.paintCell(self,painter,rect,date)

