# https://stackoverflow.com/questions/53627316/how-to-create-widget-in-pyqt5-to-show-google-map

# re utiliza el modulo re para la validacion
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from AeroArduinos_d2 import Ui_Form
from AeroFileNombre import EditarNombre
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog
# re utiliza el modulo re para la validacion
import sys, re,os
import datetime
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

from AeroHiloArduinos import HiloArduinos
# librerias para arduino....
import serial.tools.list_ports
import serial

'''
    CODIGO DE BOTONES:
        A)Color amarillo significa sin elegir
        B)Color azul significa editando
        C)Color verde significa definitivo

        self.cmbBox_velocidad.setStyleSheet("QComboBox{background-color:rgb(90,61,40);"       
                                                    "color:black; }")       
'''


#########################################################################################################
#           D E  F I  N  I  C I O  N      D E    L  A     C L  A  S  E  :   => R O N I    H D Z         #                       #
########################################################################################################
class Arduinos(QWidget, Ui_Form):

    senalNombreElegido = pyqtSignal(str)  # comunicacion con la aplicacion
    senalArduinoDesconectado = pyqtSignal(str)  # comunicacion con la aplicacion
    senalArduinoConecto = pyqtSignal(str)  # comunicacion con la aplicacion
    senalFase2_ArduinosCompletosListos = pyqtSignal(bool)  # comunicacion con la aplicacion
    senalFase1_Iniciada=pyqtSignal(dict) #le notifica al widgget principal que se ha iniciado
                                        #la fase 1

    senalChange_carpetaFavorita=pyqtSignal(str) #señal que se mandara con el nuevo nombre
                                                #de la carpeta favorita





    # Metodo constructor:
    def __init__(self):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)

        #BLOQUEADOS
        self.cmbBox_velocidad.setEnabled(False)#lo bloquearemos porque ya esta definida la velocidad

#######################################################################################
        self.avanceCarga=0 #representa el numero de arduinos conectados...
        self.proBar_carga.setMinimum(0)
        self.proBar_carga.setMaximum(3)
        #self.proBar_carga.setValue(self.avanceCarga)


        # V A L O R E S    E S T A N D A R E S
        self.__ID_EDIT_DOCUMENTO = "EditandoNombre"
        self.__ID_SINCARPETA = "CARPETA VACIA"
        self.__ID_EXTENSION_RONI = "_aeron.csv"



        self.btn_routeFile.clicked.connect(self.setDicAlm)
        self.btn_nameFile.clicked.connect(self.cambiarNombre)
        self.nombreDefecto()#generamos un nombre por defecto


# C  O  N  E X  I  O  N         C O N        L O S        A R D U I N O S :
        self.guardarVelocidad()
        # Variable de arduino que almacenara el dato
        # al hacer click en este inicia la comunicacion con arduino...
        self.btn_Conectar.clicked.connect(self.conectarArduino)
        # al elegir un opccon del combobox se guarda esta...
        self.cmbBox_velocidad.activated.connect(self.guardarVelocidad)

        self.nombreDispositivos = ["pantalla_1","pantalla_2","transmisor"]
        self.clave = "*1928"  # el asterisco es importante ya que es nuestro caracter de acceso principal
        self.primerEtapa=True #representa en que parte del programa se encuentra la aplicacion
        self.avanceCarga=0#representa el avance que tendran los dispositivos

       #Cuando detectemo un cambio en la barra....
        self.proBar_carga.valueChanged.connect(self.checarCargaExitosa)


# ***********************************************************************************************************************
#  C   A    R     P   E   T    A    S
# ***********************************************************************************************************************

    def setDicAlm(self):
        direccion = ""
        fname = QFileDialog()
        direccion = fname.getExistingDirectory()

        print("nombre=",direccion)

        if direccion != "" or self.name_route.text() != self.__ID_SINCARPETA:
            if direccion != "":
                self.name_route.setText(str(direccion))
                self.senalChange_carpetaFavorita.emit(str(direccion))

    def nombreDefecto(self):
        # ESTABLECIENDO NOMBRE POR DEFECTO...
        x = datetime.datetime.now()
        # estableciendo nombreArchivoDefecto
        # NoDiaMesAnno_horaMinSeg
        self.bel_nameFile.setText(str(x.strftime("%d%b%y_%H%M%S"))+self.__ID_EXTENSION_RONI)

    def cambiarNombre(self):
        #        #  a b r i e n d  o   l a     o  t r  a   v  e n t a n a
        #self.hide()  #hace invisible la ventana principal, pero no la cierra
        self.btn_nameFile.setEnabled(False)
        self.nextVentana = EditarNombre() #creando objeto de ventana EditarNombre
        self.nextVentana.show()
        self.nextVentana.senalNombreElegido.connect(self.cambioNombreExitoso)
        self.nextVentana.senalTermino.connect(self.activarCambioNombre)

    def cambioNombreExitoso(self,nuevoNombre):
          self.bel_nameFile.setText(nuevoNombre+self.__ID_EXTENSION_RONI)
          self.senalNombreElegido.emit(self.bel_nameFile.text())

    def activarCambioNombre(self,regreso):
        if regreso:
            self.btn_nameFile.setEnabled(True)



#################################################################################################################################3
#  V E  N  T  A  N  A       A  R D U I N O
##############################################################################################################################

    def guardarVelocidad(self):
        #revisara la velocidad de comunicacion con los arduinos...
        self.velocidad = self.cmbBox_velocidad.currentText()

    def getExtensionFile(self):
        return self.__ID_EXTENSION_RONI
    def getNameFileFinal(self):
        return self.name_route.text().replace("\n","")+"/"+self.bel_nameFile.text()#el nombre de la etiqueta ya viene
                                                                                   #incluida la extension
    def getNameCarpetaFavorita(self):
        if self.name_route.text()==self.__ID_SINCARPETA:
            return ""
        else:
            return self.name_route.text()


#################################################################################################################################3
#
#
#   H     I      L       O       S       :
#
#
##############################################################################################################################
    def conectarArduino(self):
            resultado = QMessageBox.information(self, "Atencion", "¿Los datos son correctos?"
                                                                  f"\nVelocidad: {self.velocidad} [bps]"
                                                , QMessageBox.Yes | QMessageBox.No)
            # se han llenado los datos de forma exitosa y ya se puede actuar en funcion...
            if resultado == QMessageBox.Yes:
                self.cmbBox_velocidad.setEnabled(False) #ya no podra cambiar la velocidad
                self.btn_Conectar.setEnabled(False) #desactivamos el boton de conectar...
                self.guardarVelocidad()#guardamos la velocidad a partir de la otra ventana...
                # Se hace uso de este metodo para convertir en numero el texto del combobox
                self.velocidad = self.velocidad.split(",")  # elimiando comas de numeros
                velCom = ""  # almacenara velocidad de comunicacionUnida juntandos los numeros
                for x in self.velocidad:
                    velCom += x
                self.velocidad = int(velCom)  # convirtiendo a entero el numero

                #Creamos el hilo...

                self.com_pyAr = HiloArduinos(self.velocidad, self.nombreDispositivos, self.clave)
                #Iniciamos el hilo...
                self.com_pyAr.start()
                #mandamos el objeto diccionario por referencia
                datos = self.com_pyAr.puertosRegistrados
                self.senalFase1_Iniciada.emit(datos)
                self.com_pyAr.dispositivoConecto.connect(self.mostrarDispConect)#señal que da el hilo
                self.com_pyAr.dispositivoDesconecto.connect(self.quitarDispDesco)#señal que dal el hilo
                self.com_pyAr.hiloTerminadoExitosamente.connect(self.eliminarHiloChecadorConector)


    def terminarHiloChecadorConector(self):
        self.com_pyAr.terminarHilo=True

    def eliminarHiloChecadorConector(self):
        while True:
            if self.com_pyAr.isFinished():
                print("HILO TERMINADO CON EXITO")
                del (self.com_pyAr) #eliminando el objeto de tipo hilo
                break


    def mostrarDispConect(self,nombre):
        self.senalArduinoConecto.emit(nombre)

    def quitarDispDesco(self,nombre):
        self.senalArduinoDesconectado.emit(nombre)

    def checarCargaExitosa(self,porcentajeCarga):
        #Si fue la primera vez que se cargo la barra desde la ventana de arduinos
        if self.primerEtapa and porcentajeCarga==len(self.nombreDispositivos):
                resultado = QMessageBox.information(self, "Good! :) ", "Everything ready to start :)\n"
                                                                        "Are you ready?"
                                                    , QMessageBox.Yes | QMessageBox.No)
                # se han llenado los datos de forma exitosa y ya se puede actuar en funcion...
                if resultado == QMessageBox.Yes:
                    self.cmbBox_velocidad.setEnabled(False)  # ya no podra cambiar la velocidad
                    self.btn_Conectar.setEnabled(False)  # desactivamos el boton de conectar...
                    self.primerEtapa = False #hemos pasado a la estapa siguiente... :O
                    #datos=self.ven1_Arduino.com_pyAr.puertosRegistrados.copy()
                    self.senalFase2_ArduinosCompletosListos.emit(True)



########################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = Arduinos()
    dialogo.show()
    app.exec_()




