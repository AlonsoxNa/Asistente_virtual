from PyQt5 import QtWidgets, uic

# iniciar la aplicación
app = QtWidgets.QApplication([])

# cargar archivos .ui
login = uic.loadUi("login1.ui")
login2 = uic.loadUi("login2.ui")


def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(name) == 0 or len(password) == 0:
        login.label_2.setText("Ingrese todos los datos")

def abrir_crear_cuenta():
    login.label_2.setText("")
    login.close()
    login2.show()

def crear_cuenta():
    login2.close()
    login.show()

def ingresar_como_invitado():
    login.close()
    # Cargar archivo asistente virtual

def regresar():
    login2.close()
    login.show()

# botones
login.pushButton.clicked.connect(gui_login)  # Boton de ingresar
login.pushButton_2.clicked.connect(abrir_crear_cuenta)  # Boton de creacion de cuenta
login.pushButton_3.clicked.connect(ingresar_como_invitado)  # Boton de ingresar como invitado

login2.pushButton.clicked.connect(crear_cuenta)
login2.pushButton_2.clicked.connect(regresar) # Boton de regresar

# ejecutable
login.show()
app.exec()
