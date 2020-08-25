# https://stackoverflow.com/questions/53627316/how-to-create-widget-in-pyqt5-to-show-google-map

# re utiliza el modulo re para la validacion
import sys

#####################################################
from AeroAccion_d2 import Ui_Form
from AeroHiloDarGet import HiloArdDarGet
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog,QTableWidget,QWidget,QMessageBox
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

#########################################################################################################
#           D E  F I  N  I  C I O  N      D E    L  A     C L  A  S  E  :   => R O N I    H D Z         #                       #
########################################################################################################
class Accion(QWidget,Ui_Form):
    #Metodo constructor:

    senalCancelar= pyqtSignal(bool)  #Matara al primer hilo
                                     #Matara al segundo hilo
    senalFase3_creaHilo2=pyqtSignal(bool)
    senalFase4A_EndHilo1y2 = pyqtSignal(bool)
    senalFase4B_FaseTabla = pyqtSignal(int)


    ###########################################
    senalAlturaPayload = pyqtSignal(str)
    senalAlturaCDA = pyqtSignal(str)
    #####################################

    def __init__(self):
       Ui_Form.__init__(self)
       QWidget.__init__(self)
       self.setupUi(self)
       self.avanceCarga = 0  # representa el numero de arduinos conectados...
       self.proBar_carga.setMinimum(0)
       self.proBar_carga.setMaximum(3)
       self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)




    #B O T O N E S :
       self.btn_startPause.clicked.connect(self.pausarRenudarGrabacion)
       self.btn_cancel.clicked.connect(self.cancelarEliminarVuelo)
       self.btn_terminar.clicked.connect(self.terminarGuardarVuelo)

       #CONFIGURACION INCIAL:
       self.configuracionInicial()

    #De los mas importantes atributos....
       self.punterDicArduinos=""


    #CONSTANTES...
       self.noDatosRecbir = 7
       self.sepDatos = ","
       self.__ID_FILE_GUARDADOR = "roniAero1928374655_aeron.csv"

    #BLOQUEADOS
       self.hilo2_comenzo=False
       self.exito=False




    def configuracionInicial(self):
        self.btn_startPause.setEnabled(False)
        self.btn_terminar.setEnabled(False)
        self.btn_cancel.setEnabled(False)

#######################################################################################################################
#
#      P  R   O  T  O   C  O  L  O      D   E      L   A      F  A   S  E       3
#
#######################################################################################################################


    def mostrarAlturaCDA(self,altura):
        self.bel_CDA.setStyleSheet("background-color:green;font: 50pt;border-radius: 10px;}")
        self.bel_CDA.setText(altura)
    def mostrarAlturaPayLoad(self,altura):
        self.bel_payLoad.setStyleSheet("background-color:green;font: 50pt;border-radius: 10px;}")
        self.bel_payLoad.setText(altura)

    def utilizarDatosRecibidos(self, datos):
        print("Datos: ", datos)
        datos = datos.split(self.sepDatos)
        self.bel_altitude.setText(datos[0])  # altitude
        self.belData1_long.setText(datos[3])  # longitude
        self.belData2_lat.setText(datos[2])  # latitude
        self.belData3_velo.setText(datos[1])  # velocidad
        self.belData_dist.setText(datos[4])  #rellenar la velocidad...

    def pausarRenudarGrabacion(self):
        if self.hilo2_comenzo:
            # ¿El hilo recibir datos ya estaba pausado?
            if self.hiloRecibirDatos.hiloPausado == True:
                # estara actividad la opccion de terminar grabacion si no esta pausada
                self.btn_terminar.setEnabled(True)
                self.hiloRecibirDatos.hiloPausado = False
                self.btn_startPause.setText("Pause")
            else:
                self.hiloRecibirDatos.hiloPausado = True
                self.btn_startPause.setText("Start")
                self.btn_terminar.setEnabled(False)
        else:
            resultado = QMessageBox.question(self, "Atencion", "¿Listo para comenzar? \n"
                                             , QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                # Creamos el segundo hilo que se encargar de recibir los datos...7
                ##########################################################
                #      H         I        L         O                2   #
                ##########################################################

                self.hiloRecibirDatos = HiloArdDarGet(self.punterDicArduinos, self.noDatosRecbir, self.sepDatos,
                                                      self.__ID_FILE_GUARDADOR)
                self.hiloRecibirDatos.start()  # iniciamos el hilo
                # Señales del hilo:

                self.hiloRecibirDatos.datosRecibidos.connect(self.utilizarDatosRecibidos)
                self.hiloRecibirDatos.hiloTerminadoExitosamente.connect(self.eliminarHiloRecibeTransmite)
                self.hiloRecibirDatos.senalLanzado_CDA.connect(self.mostrarAlturaCDA)
                self.hiloRecibirDatos.senalLanzado_payLoad.connect(self.mostrarAlturaPayLoad)

                self.senalFase3_creaHilo2.emit(True)  # le notificamos a la GUI principal que pasaremos
                # a la estapa 3
                self.hilo2_comenzo = True
                self.btn_startPause.setText("Pause")
                self.hiloRecibirDatos.hiloPausado = False
                self.btn_terminar.setEnabled(True)


    def terminarGuardarVuelo(self):
        # Este metodo se encargara tambien de elimnar el otro hilo
        self.hiloRecibirDatos.hiloPausado = True  # pausamo el vuelo en el que el usario decide...
        resultado = QMessageBox.question(self, "Atencion", "¿Estas que quieres ya quieres concluir el vuelo? \n"
                                         , QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.senalFase4A_EndHilo1y2.emit(True)
            self.exito = True
        self.hiloRecibirDatos.hiloPausado = False#liberamos el hilo de pausarlo

    def cancelarEliminarVuelo(self):
        if self.hilo2_comenzo:
            self.hiloRecibirDatos.hiloPausado=True #pausamos el hilo en el que el usuario decide...
            resultado = QMessageBox.question(self, "Atencion", "¿Estas seguro de cancelar el vuelo? \n"
                                                        "se perderan todos los datos\n"
                                             , QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.hiloRecibirDatos.hiloPausado=False
                self.senalCancelar.emit(True) #la GUI principal sabra que hacer en esta caso...
            self.hiloRecibirDatos.hiloPausado=False #liberamos el hilo de pausarlo

        else:
            resultado = QMessageBox.question(self, "Atencion", "¿Estas seguro de cancelar el vuelo? \n"
                                                               "se perderan todos los datos\n"
                                             , QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.senalCancelar.emit(True)  # la GUI principal sabra que hacer en esta caso...

    def terminarHiloRecibeTransmite(self):
        self.hiloRecibirDatos.terminarHilo = True
        self.hilo2_comenzo=False

    def eliminarHiloRecibeTransmite(self,noDatosRegistrados):
        while True:
            if self.hiloRecibirDatos.isFinished():
                print("HILO TERMINADO CON EXITO")
                del (self.hiloRecibirDatos)  # eliminando el objeto de tipo hilo
                break
        print("JORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRGE TE AMMMMMMMMMMMMMMMMMMOOOOOOOOOOOOOOOOOOOO")
        if self.exito:
            self.senalFase4B_FaseTabla.emit(noDatosRegistrados)#con esto le decimos que ya puede
                                                 #hacer lo que quiera con el archivo
            self.exito=False








#################################################################################################################################3
#
#
#    E  T  A  P A S
#
#
##############################################################################################################################


    def starProtocolo(self):
        self.btn_startPause.setEnabled(True)
        self.btn_cancel.setEnabled(True)


        QMessageBox.critical(self, "Atencion", "Bienvenido a la ventana de acciónn\n"
                                               " recuerda que para empezar el vuelo\n"
                                                "deberas oprimir el boton de start"
                                              ,QMessageBox.Ok)



############################################################################################################
    def getNameFileGuardadorTemporal(self):
        return self.__ID_FILE_GUARDADOR







########################################################################################
if __name__ == "__main__":
 app = QApplication(sys.argv)
 dialogo = Accion()
 dialogo.show()
 app.exec_()