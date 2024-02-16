from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt
import sys, dataBase


abs_file_path = "styles/styles.qss"

class ventanaPadronCompleto(QMainWindow):
       def __init__(self):
        super().__init__()

        cartel = dataBase.leerFilas()
        layout = QVBoxLayout()
        for c in cartel:
            x =f"APELLIDO: {c[0]}, NOMBRE: {c[1]}, DNI: {c[2]}"
            self.texto = QLabel(x)
            layout.addWidget(self.texto)
  
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)    

class ventanaPadronQVoto(QMainWindow):
       def __init__(self):
        super().__init__()

        total = 0
        cant = 0
        lista = dataBase.leerFilas()
        for v in lista:
            total += 1
        condicion = "voto = 1"
        cartel = dataBase.buscar(condicion)
        layout = QVBoxLayout()
        for c in cartel:
            #x =f"APELLIDO: {c[0]}, NOMBRE: {c[1]}, DNI: {c[2]}"
            #self.texto = QLabel(x)
            cant += 1
        porcentaje =  (cant/total)*100  
        x =f"Porcentaje del padron que SÍ votó: %{porcentaje}"  
        self.texto = QLabel(x)
        layout.addWidget(self.texto)
  
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

class ventanaPadronQNoVoto(QMainWindow):
       def __init__(self):
        super().__init__()

        total = 0
        cant = 0
        lista = dataBase.leerFilas()
        for v in lista:
            total += 1
        condicion = "voto = 0"
        cartel = dataBase.buscar(condicion)
        layout = QVBoxLayout()
        for c in cartel:
            #x =f"APELLIDO: {c[0]}, NOMBRE: {c[1]}, DNI: {c[2]}"
            #self.texto = QLabel(x)
            cant += 1
        porcentaje =  (cant/total)*100  
        x =f"Porcentaje del padron que SÍ votó: %{porcentaje}"  
        self.texto = QLabel(x)
        layout.addWidget(self.texto)
  
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        resX = 1366
        resY = 768
        self.setFixedSize(resX,resY)
        with open(abs_file_path,"r") as file:
            self.setStyleSheet(file.read())
        


        admi = QLabel(self)
        admi.setText("ADMINISTRADOR")
        admi.setAlignment(Qt.AlignCenter)
        with open(abs_file_path,"r") as file:
            admi.setStyleSheet(file.read())

        btn1 = QPushButton(f"Ver % del padron que votó",self)
        btn1.move((resX/2)-(resX/8),250)
        btn1.clicked.connect(self.PadronQVoto)
        with open(abs_file_path,"r") as file:
            btn1.setStyleSheet(file.read())

        btn2 = QPushButton(f"Ver % del padron que NO votó",self)
        btn2.move((resX/2)-(resX/8),350)
        btn2.clicked.connect(self.PadronQNoVoto)
        with open(abs_file_path,"r") as file:
            btn2.setStyleSheet(file.read())

        btn3 = QPushButton(f"Recuento de votos",self)
        btn3.move((resX/2)-(resX/8),450)
        with open(abs_file_path,"r") as file:
            btn3.setStyleSheet(file.read())       


        btn4 = QPushButton(f"Ver padron completo",self)
        btn4.move((resX/2)-(resX/8),550)
        btn4.clicked.connect(self.padronCompleto)
        with open(abs_file_path,"r") as file:
            btn4.setStyleSheet(file.read())      


    def padronCompleto(self):
        self.v4 = ventanaPadronCompleto()
        self.v4.show()
        with open(abs_file_path,"r") as file:
            self.v4.setStyleSheet(file.read())

    def PadronQVoto(self):
        self.v1 = ventanaPadronQVoto()
        self.v1.show()
        with open(abs_file_path,"r") as file:
            self.v1.setStyleSheet(file.read())

    def PadronQNoVoto(self):
        self.v2 = ventanaPadronQNoVoto()
        self.v2.show()
        with open(abs_file_path,"r") as file:
            self.v2.setStyleSheet(file.read())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
