from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import sys
 
class QHolaMundo(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.leMiNombre = QLineEdit(self)
        self.btHola = QPushButton('Hola...',self)
        layout.addWidget(self.leMiNombre)
        layout.addWidget(self.btHola)
        self.setLayout(layout)
        QObject.connect(self.btHola,SIGNAL('clicked()'),self.salude)
    def salude(self):
        miNombre = self.leMiNombre.text()
        saludo = 'Hola %s'%(miNombre)
        QMessageBox.information(self,'Saludo',saludo)
 

qhm = QtGui.QWidget()
qhm = QHolaMundo()
qhm.setWindowIcon(QIcon('mx.png'))
qhm.resize(640,480)
qhm.setWindowTitle('¡Viva México!')
qhm.show()
sys.exit(app.exec_())
