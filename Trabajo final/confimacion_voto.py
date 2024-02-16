from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton,QHBoxLayout
from PySide6.QtGui import QFont, QPixmap, QImage
from PySide6.QtCore import Qt
from ventana_votacion import * 

class ConfirmacionVoto(QMainWindow):
    def __init__(self,voto):
        super().__init__()
        self.voto=voto
        #votado=VentanaVotacion.mostrar_resultados -> dentro del QLabel self.entrada
        self.setWindowTitle("Confirmacion")
        
        layout = QVBoxLayout()
        self.texto = QLabel(f'Su voto es para:\n{self.voto}')
        layout.addWidget(self.texto)
        self.entrada = QLabel()
        layout.addWidget(self.entrada)

        #Imagen
        imagenCandidato = QImage("C:\\Users\\Mati\\Documents\\Desarrollo de Software\\programacion-1\\Trabajo final\\messi.jpg")
        pixmap = QPixmap()  
        if imagenCandidato.isNull():
            print("Error al cargar la imagen")
        else:
            pixmap = QPixmap.fromImage(imagenCandidato)
        labelCandidato = QLabel(self)
        labelCandidato.setPixmap(pixmap)

        #Font
        font = QFont("Times New Roman", 12)
        
        #Boton Confirmar
        botonConfirmar = QPushButton('Confirmar')
        botonConfirmar.setDefault(True)
        layout.addWidget(botonConfirmar)
        botonConfirmar.setFont(font)
        botonConfirmar.setStyleSheet("color: green")

        #Bototn Volver Atras
        botonBack = QPushButton('Cancelar voto')
        botonBack.setDefault(True)
        layout.addWidget(botonBack)
        botonBack.setFont(font)
        botonConfirmar.clicked.connect(self.confirmacion)
        botonBack.clicked.connect(self.cancelacion)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def confirmacion(self):

        self.v22 = ventanaRegistrado(self.voto)
        self.v22.show()

    def cancelacion(self):
        self.close()
        
        
class ventanaRegistrado(QMainWindow):
    def __init__(self,cartel):
        super().__init__()

        layout = QVBoxLayout()

        self.texto = QLabel(f"Su voto por {cartel} ha sido registrado")
        self.texto.setStyleSheet("color: black")
        layout.addWidget(self.texto)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
