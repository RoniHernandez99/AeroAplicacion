from AeroFileNombre_d import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog
import sys, re,os
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana



class EditarNombre(QDialog, Ui_Dialog):
    # Metodo constructor:
    senalNombreElegido = pyqtSignal(str)  # comunicacion con la aplicacion
    senalTermino = pyqtSignal(bool)  # comunicacion con la aplicacion
    def __init__(self,parent=None):
        super(EditarNombre, self).__init__(parent)  # propiedad para ser segunda ventana
        Ui_Dialog.__init__(self)
        QDialog.__init__(self)
        self.setupUi(self)


        # Como manipular nuestro lineEdit cada ves
        # que se introduzcan letras
        self.lineEdit_nombre.textChanged.connect(self.validar_nombre)

        # Asociando un metodo al boton cuando este se presionado
        self.btn_endSetName.clicked.connect(self.terminarEditar)

        #Indica que el nombre fue elegido
        self.nombreElegido=False

    def terminarEditar(self):
        nombreCorrecto=self.validar_nombre()
        if not(nombreCorrecto):
            QMessageBox.critical(self, "Atencion", "Atiende tus errores", QMessageBox.Ok)
        else:
            resultado = QMessageBox.warning(self,"Atencion",f"Nuevo nombre={self.lineEdit_nombre.text()}\n"
                                             "¿es correcto?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.nombreElegido=True
                self.close()

    # primer metodo para validar el dato nombre
    def validar_nombre(self):
        nombre = self.lineEdit_nombre.text()  # obtenmos lo que se haya escrito en
        # el objeto 'editText' llamado nombre
        # en el parametro ^[se añaden los caracteres validos]
        #       a-z significa todas las letras de la a a la z
        #       \s  representan los espacios
        #       re.I  ignorar mayuscula y minisculas
        validar = re.match('^[a-z|A-Z|0-9|_]{4,15}$', nombre)
        if nombre == "":
            # modifcando el estilo del objeto etiqueta llamado 'nombre'
            self.lineEdit_nombre.setStyleSheet("border: 3px solid yellow;")
            self.bel_estadoNombre.setText("Sintaxis INCORRECTA"
                                          "\n\tc)El nombre no puede ser NULL")
            return False

        elif not validar:  # si la validacion no es correcta  (si  no es True)
            # modifcando el estilo del objeto etiqueta llamado 'nombre'
            self.lineEdit_nombre.setStyleSheet("border: 3px solid red;")
            self.bel_estadoNombre.setText("Sintaxis: INCORRECTA:"
                                          "\n\ta) El tamano del nombre debe estar\n\ten el intervalo de  [4,15] caracteres"
                                          "\n\tb) Este solo puede contener LETRAS\n\t y numeros")
            return False
        else:  # no pasa ningun error
            self.lineEdit_nombre.setStyleSheet("border: 3px solid green;")
            self.nombreArchivo = nombre
            self.bel_estadoNombre.setText("Sintaxis: CORRECTA")

            return True


    def closeEvent(self, event):
        if self.nombreElegido:
            self.senalNombreElegido.emit(str(self.lineEdit_nombre.text())) # mandando nombre
            self.senalTermino.emit(True)
            #self.parent().show()
            event.accept()  # Saldremos del evento
        else:
            resultado = QMessageBox.question(self, "Salir ...",
                                             "¿Seguro que quieres salir?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.senalTermino.emit(True)
                event.accept()
                #self.parent().show()
            else:
                event.ignore()  # No saldremos del evento

########################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = EditarNombre()
    dialogo.show()
    app.exec_()


