from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtGui import QPainter,QFont
class CalendarioSesion():
    def __init__(self,interfaz) :
        self.interfaz = interfaz 
        self.layout = self.interfaz.verticalLayoutCalendario
        self.calendarioWidget = CalendarWidget(self.interfaz)
        self.layout.addWidget(self.calendarioWidget)

class CalendarWidget(QCalendarWidget):
    def __init__(self,interfaz,parent=None):
        super(CalendarWidget,self).__init__(parent)
    """
    def paintCell(self,painter,rect,date):
        painter.setRenderHint(QPainter.Antialiasing,True)
        painter.save()
        painter.drawRect()

        painter.setFont(QFont('Decorative',10))

    """