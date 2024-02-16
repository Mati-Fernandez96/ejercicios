import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QRadioButton
from confimacion_voto import *

class VentanaVotacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Votación")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.opcion1 = QRadioButton("Opción 1") 
        self.opcion2 = QRadioButton("Opción 2")
        self.opcion3 = QRadioButton("Opción 3")
        self.opcion4 = QRadioButton("Opción 4")

        boton_continuar = QPushButton("Continuar")
        boton_continuar.clicked.connect(self.mostrar_resultados)

        layout.addWidget(self.opcion1)
        layout.addWidget(self.opcion2)
        layout.addWidget(self.opcion3)
        layout.addWidget(self.opcion4)
        layout.addWidget(boton_continuar)

        central_widget.setLayout(layout)

    def mostrar_resultados(self):
        self.candidatoVotado=""

        if self.opcion1.isChecked():
            print("Opción 1")
            self.candidatoVotado="Opcion 1"

        if self.opcion2.isChecked():
            print("Opción 2")
            self.candidatoVotado="Opcion 2"

        if self.opcion3.isChecked():
            print("Opción 3")
            self.candidatoVotado="Opcion 3"

        if self.opcion4.isChecked():
            print("Opción 4")
            self.candidatoVotado="Opcion 4"

        self.v = ConfirmacionVoto(self.candidatoVotado)
        self.v.show()
        self.hide()
        #return self.candidatoVotado  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVotacion()
    ventana.show()
    sys.exit(app.exec_())