from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pantalla_admin import * 
from ventana_votacion import *

class SistemaVotacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        self.titulo = QLabel("VOTACIONES 2023")
        layout.addWidget(self.titulo)
        self.titulo.setStyleSheet("font: 50px; color: black")

        self.texto1 = QLabel("INGRESE SU DNI:")
        layout.addWidget(self.texto1)
        self.texto1.setStyleSheet("font: 20px; color: black")
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)

        self.aceptar = QPushButton("ACEPTAR")
        self.aceptar.setDefault(True)
        layout.addWidget(self.aceptar)
        self.aceptar.setStyleSheet("font: 20px; background: green; color: black;")
        self.aceptar.clicked.connect(self.abrirVentanaVotacion)

        self.cancelar = QPushButton("CANCELAR")
        self.cancelar.setDefault(True)
        layout.addWidget(self.cancelar)
        self.cancelar.setStyleSheet("font: 20px; background: red; color: black;")
        self.cancelar.clicked.connect(self.close)

        self.admin = QPushButton("ADMINISTRADOR")
        self.admin.setDefault(True)
        layout.addWidget(self.admin)
        self.admin.setStyleSheet("font: 20px; background: blue; color: black;")
        self.admin.clicked.connect(self.abrirVentanaAdmin)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def abrirVentanaAdmin(self):
        self.admin = ventanaPadronCompleto()
        self.admin.show()

    def abrirVentanaVotacion(self):
        try:
            dni = int(self.entrada.text())  
            if (7 <= len(str(dni)) <= 8) and (self.buscarDNIenBD() == True) and (self.buscarVoto() == True) and (dataBase.checkVoto(dni) == False):  
                self.v2 = VentanaVotacion()
                self.v2.show()
            else:
                QMessageBox.warning(self, "Error", "El DNI debe tener entre 7 y 8 dígitos o estar en el padrón.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido como DNI.")

    def buscarDNIenBD(self):
        check=False
        persona = self.entrada.text()
        if dataBase.buscar(f"DNI = {persona}"):
            check=True
        return check

    def buscarVoto(self):
        check=False
        persona = self.entrada.text()
        if dataBase.buscar(f"voto = 0"):
            check=True
        return check
    
if __name__ == "__main__":
    app = QApplication()
    css = "*{font-size: 50px; background-color: #c6f5c7; color: #850a30;}"
    app.setStyleSheet(css)
    window = SistemaVotacion()
    window.show()
    app.exec()