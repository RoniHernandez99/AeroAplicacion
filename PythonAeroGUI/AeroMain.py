# https://stackoverflow.com/questions/53627316/how-to-create-widget-in-pyqt5-to-show-google-map

# re utiliza el modulo re para la validacion
import sys
import os
import datetime
######################3

#####################################################
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog,QTableWidget,QWidget,QMessageBox
from PyQt5.QtWidgets import QApplication
from AeroMain_d import Ui_MainWindow as aeroMenu
import time
from AeroTabla import Tabla
from AeroAccion import Accion
from AeroArduinos import Arduinos

from AeroHiloDarGet import HiloArdDarGet

from AeroHiloArduinos import HiloArduinos

'''
    Fase 0   =>Solo se esta probando la interfaz
    Fase 1   =>Inicia el hilo 1
    Fase 2   =>Cargan todos los arduinos exitosamente y se pasa a ventana de accion
    Fase 3   =>Se crea el hilo 2 para ya recibir datos
    Fase 4   =>Se termina el Hilo1 e Hilo2 existosamente y se abre la tabla
               e iniiiar el hilo 3, cabe aclara que las otras dos widgets se bloquean
'''



#########################################################################################################
#           D E  F I  N  I  C I O  N      D E    L  A     C L  A  S  E  :   => R O N I    H D Z         #                       #
########################################################################################################
class AeroRoni(QMainWindow,aeroMenu):

    #Metodo constructor:
    def __init__(self):
       aeroMenu.__init__(self)
       QMainWindow.__init__(self)
       self.setupUi(self)
    #VENTANAS QUE UTILIZAMOS...
       self.ven1_Arduino =Arduinos()
       self.ven2_Accion=Accion()
       self.ven3_Tabla=Tabla()

    #SENALES ENTRE WIDGETS...
       self.ven1_Arduino.senalNombreElegido.connect(self.cambiarNombreFile)
       self.ven1_Arduino.senalFase1_Iniciada.connect(self.iniciarFase1)
       self.ven1_Arduino.senalFase2_ArduinosCompletosListos.connect(self.iniciarFase2)
       self.ven1_Arduino.senalArduinoDesconectado.connect(self.quitarDispDesco)
       self.ven1_Arduino.senalArduinoConecto.connect(self.mostrarDispConect)


       self.ven2_Accion.senalCancelar.connect(self.cancelarProcesosEspeciales)
       self.ven2_Accion.senalFase3_creaHilo2.connect(self.iniciarFase3)
       self.ven2_Accion.senalFase4A_EndHilo1y2.connect(self.preinicioFase4)
       self.ven2_Accion.senalFase4B_FaseTabla.connect(self.iniciarFase4)


    #SENALES ACERCA DE LOS FICHEROS GUARDADORES...
       #Con esta señal guadaremos el nombre de la carpeta favorita
       self.ven1_Arduino.senalChange_carpetaFavorita.connect(self.guardarName_carpetaFavorita)





    #LLENANDO LA LISTA DE VENTANAS..
       self.listaPantallas.addWidget(self.ven1_Arduino)
       self.listaPantallas.addWidget(self.ven2_Accion)
       self.listaPantallas.addWidget(self.ven3_Tabla)

    #VENTANA CON LA QUE SE INICIA POR DEFAULT...
       self.listaPantallas.setCurrentIndex(0)
       self.listaPantallas.showFullScreen()


    #BOTONES PARA CAMBIAR DE VENTANA
       self.btn_RecorderData.clicked.connect(self.abrirVentanaTabla)
       self.btn_Datos.clicked.connect(self.abrirVentanaAccion)
       self.btn_Arduino.clicked.connect(self.abrirVentanaArduino)

    #FASES DE LA APLICACION
       self.avanceCarga=0
       self.estadoGUI_Aero=0 #se encuentra en el estado 1
       self.nombreDispositivos = ["pantalla_1", "pantalla_2", "transmisor"]

    #DATOS DEL VUELO
       self.inicioVuelo=""
       self.finVuelo=""
    #C A R
       self._ID_DICT_CRACK="cracksRoni"
       self._ID_DICT_RESPALDO= self._ID_DICT_CRACK+"/respaldoAeron"
       self._ID_DICT_FAVORITO= self._ID_DICT_CRACK+"/dicFavorito.txt"
       self._ID_DICT_PUERTOS_REBELDES=self._ID_DICT_CRACK+"/portsRebeldes.txt"

      #Checando la existencia de los archivos...
       self.portsRebeldes=[] #MUY IMPORTANTE YA QUE NOS DICE QUE PUERTOS NO APLICAN
       self.buenOrden()
       self.cambiarNombreFile()

      #CONFIGURACION INCIIAL
       self.buenOrden()
       self.confiFase_0()
       self.cargarDatosFiles()#esta funcion se encargar de abrir los files disponibles


    #PANTALLA DE ARDUINO Y LA BARRA DE CARGAR
    def cambiarNombreFile(self):
        nuevoNombre=self.ven1_Arduino.bel_nameFile.text()
        self.ven2_Accion.bel_nameFile.setText(nuevoNombre)
        self.ven3_Tabla.bel_nameFile.setText(nuevoNombre)

#Esta funcion se encargara de supervisar que todas las carpetas existan, ya que son
#totalmente necesarias,de no existir habria problemas en el resto de los programas por
#la dependencia de estos en ellas
    def buenOrden(self):
        #Carpetas que deben existir desde un principio
        #Veremos si no existe la carpeta la vamos a crear...
        if not( os.path.isdir(self._ID_DICT_CRACK) ):
            os.mkdir(self._ID_DICT_CRACK)
        if not( os.path.isdir(self._ID_DICT_RESPALDO)):
            os.mkdir(self._ID_DICT_RESPALDO)
        if not(os.path.isfile(self._ID_DICT_FAVORITO)):
            file=open(self._ID_DICT_FAVORITO,'w')
            file.close()
        if not( os.path.isfile(self._ID_DICT_PUERTOS_REBELDES)):
            file=open(self._ID_DICT_PUERTOS_REBELDES,'w')
            file.close()
        print("no entiendo")

#       self._ID_DICT_FAVORITO= self._ID_DICT_CRACK+"/dicFavorito.txt"
#       self._ID_DICT_PUERTOS_REBELDES=self._ID_DICT_CRACK+"/portsRebeldes.txt"
#       self._ID_DICT_OBJETIVO=self._ID_DICT_CRACK+"/coorObjetivo.txt"

    def cargarDatosFiles(self):
        self.buenOrden() #primero nos sercioaramos de que existan todos
        #Cargando el nombre de la carpeta por defecto...

        #nombre de la     C A R P E T A    P O R    D E F E C T O :
        archivo = open(self._ID_DICT_FAVORITO, "r")  # lectura del archivo
        archivo.seek(0)  # poner al punteroFile en posicion cero
        self.ven1_Arduino.name_route.setText(archivo.readline()[:-1])# quitamos el salto de linea
        archivo.close()



        # nombre de los   P U E R T O S     N O   V A L I D O S  :
        # readline()  ==>devuelve una cadena vacia cuando se encuentra el final del archivo
        archivo = open(self._ID_DICT_PUERTOS_REBELDES, "r")  # lectura del archivo
        archivo.seek(0)  # poner al punteroFile en posicion cero
        self.portsRebeldes=[]
        while True:
            linea=archivo.readline()[:-1]#quitamos el salto de linea
            if not(linea==""):
               self.portsRebeldes.append(linea)
            else:
                archivo.close()
                break


    def guardarData_Objetivo(self,listCordenadas):
        archivo=open(self._ID_DICT_OBJETIVO,'w')
        archivo.seek(0)  # poner al punteroFile en posicion cero
        archivo.write( str(listCordenadas[0]) +"\n"  )
        archivo.write(str(listCordenadas[1]) + "\n")
        archivo.close()



    def guardarName_carpetaFavorita(self,nameCarpeta):
            archivo=open(self._ID_DICT_FAVORITO,"w")
            archivo.seek(0)
            archivo.write(nameCarpeta + "\n")
            archivo.close()
            print(f"ESCRBIENDO {nameCarpeta} en {self._ID_DICT_FAVORITO}")


        #Esta funcion recibe los datos de la señal del hilo con arduino
    #con ayuda de esta funcion vamos a modificar hacer lo que queramos
    #con estos datos
    #El avion mandara los dats en el siguiente orden
    #1       Yaw
    #2       Pitch
    #3       Roll
    #4       Altitud
    #5       Velocidad
    #6       Longitud
    #7       Objeto 1 lanzado
    #8       Objeto 2 lanzado



    def abrirVentanaArduino(self):
        self.listaPantallas.setCurrentIndex(0)

    def abrirVentanaAccion(self):
        if self.estadoGUI_Aero==1 and self.ven1_Arduino.getNameCarpetaFavorita()=="":
            QMessageBox.critical(self, "Atencion", "No puedes abrir la otra ventana si no tienes \n"
                                                   "el nombre de la carpeta destino lista\n"
                                                  ,QMessageBox.Ok)
        else:
            self.listaPantallas.setCurrentIndex(1)

    def abrirVentanaTabla(self):
        self.listaPantallas.setCurrentIndex(2)


    def closeEvent(self,event):
            resultado = QMessageBox.question(self, "Salir ...",
                                             "¿Seguro que quieres salir?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()  # No saldremos del evento




#################################################################################################################################3
#  V E  N  T  A  N  A       A  C  C  I  O  N
##############################################################################################################################






#################################################################################################################################3
#
#
#    E  T  A  P A S
#
#
##############################################################################################################################
    def mostrarDispConect(self, nombre):
        self.avanceCarga += 1
        if nombre == self.nombreDispositivos[0]:  # pantalla 1...
            self.ven1_Arduino.bel_pantalla1.setText(nombre)
            self.ven2_Accion.bel_pantalla1.setText(nombre)
        elif nombre == self.nombreDispositivos[1]:  # pantalla 2...
            self.ven1_Arduino.bel_pantalla2.setText(nombre)
            self.ven2_Accion.bel_pantalla2.setText(nombre)
        elif nombre == self.nombreDispositivos[2]:  # trasnmisor...
            self.ven1_Arduino.bel_Arduino.setText(nombre)
            self.ven2_Accion.bel_Arduino.setText(nombre)
        self.ven2_Accion.proBar_carga.setValue(self.avanceCarga)
        self.ven1_Arduino.proBar_carga.setValue(self.avanceCarga)  # aumentamos en 1 el avance de carga

    def quitarDispDesco(self, nombre):
        self.avanceCarga -= 1
        if nombre == self.nombreDispositivos[0]:  # pantalla 1...
            self.ven1_Arduino.bel_pantalla1.setText("")
            self.ven2_Accion.bel_pantalla1.setText("")
        elif nombre == self.nombreDispositivos[1]:  # pantalla 2...
            self.ven1_Arduino.bel_pantalla2.setText("")
            self.ven2_Accion.bel_pantalla2.setText("")
        elif nombre == self.nombreDispositivos[2]:  # trasnmisor...
            self.ven1_Arduino.bel_Arduino.setText("")
            self.ven2_Accion.bel_Arduino.setText("")
        self.ven1_Arduino.proBar_carga.setValue(self.avanceCarga)  # aumentamos en 1 el avance de carga
        self.ven2_Accion.proBar_carga.setValue(self.avanceCarga)  # aumentamos en 1 el avance de carga

    def iniciarFase1(self,punteroDictArduinos):
        self.confiFase_2()
        self.btn_RecorderData.setEnabled(False)#restringimos el acceso a este botonn...
        self.btn_Datos.setEnabled(True)#pueden entrar y salir a esa ventana, no hay problema alguno
        self.ven1_Arduino.btn_Conectar.setEnabled(False)  # Para que no cree otro hilo

        #Quedan desbloqueados los botones de la GUI 2
        self.estadoGUI_Aero=1
        #cargamos al apuntador diccionario...
        # PASAMOS POR REFEENCIA EL OBJETO DE TIPO DICCIONARIO DEL HILO
        self.ven2_Accion.punterDicArduinos = punteroDictArduinos

        self.ven2_Accion.btn_cancel.setEnabled(True)  # Activamos el boton de cancelacion
                                                      # pues como acabao de pasar a la etapa 1
                                                      #ya puede activar el hilo,asi como cancelar
                                                      #el hilo 1
        self.ven2_Accion.btn_startPause.setEnabled(True) #El boton se encuentra disponible ya que
                                                         #ya puede iniciar el hilo 2 pues ya inicio
                                                         #el hilo 1


    def iniciarFase2(self):
        self.estadoGUI_Aero=2 #cambiamos a la fase numero 2...
        self.abrirVentanaAccion()
        self.ven2_Accion.starProtocolo()

    def iniciarFase3(self):
        self.estadoGUI_Aero=3
        #Cambiamos el metodo asociado al boton para que ya tenga la capacidad de pausar y reunudar
        #la recepccion de datos..
        self.inicioVuelo=self.datoTiempoAhorita()#almacenamos el dato de tiempo inicial

#Cuando preiniciamos la fase 4 no queremos borrar lo que hay en la pantalla de accion
#solo queremos bloquear sus botones start finish and save y oviamente matar a los dos hilos

    def preinicioFase4(self):
        self.ven2_Accion.terminarHiloRecibeTransmite()  # eliminamos hilo2
        self.ven1_Arduino.terminarHiloChecadorConector()  # eliminamos hilo1
        self.estadoGUI_Aero = 4
        self.finVuelo=self.datoTiempoAhorita()#almacenamos el tiempo en el que acabo el vuelo
        self.confiFase_1()

    def iniciarFase4(self,noRenglonesTotales):
        print("QUE PASA AQUI....")
        #Para acceder a un atributo encapsulado
        #nombreInstancia._NombreClase__nombrePropiedad

        #sera un archivo que se almacenara en la carpeta de respaldos, por cualquier cosa...
        name_archivoRespaldo= self._ID_DICT_RESPALDO+"/"+self.finVuelo+self.ven1_Arduino.getExtensionFile()
        #sera el nombre de la carpeta donde se almacenara el archivo
        name_archivoFinal=self.ven1_Arduino.getNameFileFinal()#returnara el nmbre final del archivo
                                                              #importante mencionar que ya viene la extension incluida
        #representa el archivo que contiene temporalmente los datos
        name_archivoTemporal=self.ven2_Accion.getNameFileGuardadorTemporal()
        print("RONI TE AMO:",name_archivoTemporal)
        archivoTemporal=open(name_archivoTemporal,'r')
        archivoFinal=open(name_archivoFinal,'w')
        archivoRespaldo=open(name_archivoRespaldo,'w')

        #Todos los archivos iniciaran desde el inicio
        archivoFinal.seek(0)
        archivoRespaldo.seek(0)
        archivoTemporal.seek(0)
        #Escribiendo fecha de inicio y fecha de cadocidad
        archivoRespaldo.write(self.inicioVuelo+"\n")
        archivoRespaldo.write(self.finVuelo+"\n")
        archivoRespaldo.write(str(noRenglonesTotales)+"\n")

        archivoFinal.write(self.inicioVuelo+"\n")
        archivoFinal.write(self.finVuelo+"\n")
        archivoFinal.write(str(noRenglonesTotales)+"\n")
        while True:
            linea = archivoTemporal.readline()
            if not(linea):
                break
            archivoFinal.write(linea)
            archivoRespaldo.write(linea)
        #Cerrandos todos los archivos
        archivoFinal.close()
        archivoRespaldo.close()
        archivoTemporal.close()
        self.ven3_Tabla.bel_nameRoute.setText(self.ven1_Arduino.name_route.text())
        self.ven3_Tabla.bel_nameFile.setText(self.ven1_Arduino.bel_nameFile.text())
        print("VAMO A ABRIR archivo final",name_archivoFinal)
        self.ven3_Tabla.openFileAeron(name_archivoFinal)
        self.abrirVentanaTabla()



    def datoTiempoAhorita(self):
        # ESTABLECIENDO NOMBRE POR DEFECTO...
        x = datetime.datetime.now()
        # estableciendo nombreArchivoDefecto
        # NoDiaMesAnno_horaMinSeg
        return str(x.strftime("%d%b%y_%H%M%S"))




    def cancelarProcesosEspeciales(self):
        '''
            Fase 0   =>Solo se esta probando la interfaz
            Fase 1   =>Inicia el hilo 1
            Fase 2   =>Cargan todos los arduinos exitosamente y se pasa a ventana de accion
            Fase 3   =>Se crea el hilo 2 para ya recibir datos
            Fase 4   =>Se termina el Hilo1 e Hilo2 existosamente y se abre la tabla
                       e iniiiar el hilo 3, cabe aclara que las otras dos widgets se bloquean
        '''
        if self.estadoGUI_Aero==1 or self.estadoGUI_Aero==2:
           #Le decimo a la ventana 1 que mate a su hilo...
           self.ven1_Arduino.terminarHiloChecadorConector()
           self.abrirVentanaArduino() #Despues nos vamos a la ventana principal
           self.confiFase_0()

        elif self.estadoGUI_Aero==3:
           self.ven2_Accion.terminarHiloRecibeTransmite()#eliminamos hilo2
           self.ven1_Arduino.terminarHiloChecadorConector() #eliminamos hilo1
           self.abrirVentanaArduino()
           self.confiFase_0()



#   Esta configuracion aplica cuando se cancela el vuelo....
#   pues se reinician todas las configuraciones..
    def confiFase_0(self):
        self.estadoGUI_Aero=0
        self.avanceCarga=0


    # Modificando ventana1...

# M O D I F I C A N D O    G E N E R A L M E N T E   :
        self.ven1_Arduino.nombreDefecto()  # Generamos un nombre por defecto
        self.ven2_Accion.bel_nameFile.setText(self.ven1_Arduino.bel_nameFile.text()) #Lo actualizamos en esta pantalla
        self.ven3_Tabla.bel_nameFile.setText("")#Le ponemos un nombre que no conocemos...

        self.btn_Arduino.setEnabled(True)
        self.btn_RecorderData.setEnabled(True)
        self.btn_Datos.setEnabled(True)

# M O D I F I C A N D O    P A N T A L L A   1

        self.ven1_Arduino.primerEtapa = True
        #botones
        self.ven1_Arduino.btn_Conectar.setEnabled(True)
        self.ven1_Arduino.cmbBox_velocidad.setEnabled(False)

        # barra y todas las etiquetas hay que reiniciairlas
        self.ven1_Arduino.bel_Arduino.setText("")
        self.ven1_Arduino.bel_pantalla1.setText("")
        self.ven1_Arduino.bel_pantalla2.setText("")
        self.ven1_Arduino.proBar_carga.setValue(0)

# M O D I F I C A C I O N E S    P A N T A L L A   2
        #Ponemos a que apunte a un objeto nulo
        self.ven2_Accion.punterDicArduinos=""
        self.ven2_Accion.btn_cancel.setEnabled(False)
        self.ven2_Accion.btn_startPause.setEnabled(False)
        self.ven2_Accion.btn_terminar.setEnabled(False)

    #INDICADORES DE DISPOSITIVOS CONECTADOS...
        self.ven2_Accion.bel_Arduino.setText("")
        self.ven2_Accion.bel_pantalla1.setText("")
        self.ven2_Accion.bel_pantalla2.setText("")
        self.ven2_Accion.proBar_carga.setValue(0)

    #DATOS PEQUEÑOS...
        self.ven2_Accion.belData1_long.setText("")
        self.ven2_Accion.belData2_lat.setText("")
        self.ven2_Accion.belData3_velo.setText("")
        self.ven2_Accion.belData_dist.setText("")
    #DATOS GRANDES...
        self.ven2_Accion.bel_altitude.setText("")
        self.ven2_Accion.bel_altitude.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        self.ven2_Accion.bel_CDA.setText("")
        self.ven2_Accion.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        self.ven2_Accion.bel_payLoad.setText("")
        self.ven2_Accion.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
    #EL BOTON REGRESAR PAUSAR REGRESA A SU METODO PRINCIPAL
        self.ven2_Accion.btn_startPause.setText("Start")


# M O D I F I C A N D O    P A N T A L L A   3
        self.ven3_Tabla.limpiarTabla()
        self.ven3_Tabla.bel_CDA.setText("")
        self.ven3_Tabla.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
        self.ven3_Tabla.bel_payLoad.setText("")
        self.ven3_Tabla.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")



#   Esta configuracion ocurre despues de terminar un vuelo existosamente...
    def confiFase_1(self):
        self.estadoGUI_Aero=0
        self.avanceCarga=0


    # Modificando ventana1...

# M O D I F I C A N D O    G E N E R A L M E N T E   :
        #self.ven1_Arduino.nombreDefecto()  # Generamos un nombre por defecto
        #self.ven2_Accion.bel_nameFile.setText(self.ven1_Arduino.bel_nameFile.text()) #Lo actualizamos en esta pantalla
        #self.ven3_Tabla.bel_nameFile.setText("")#Le ponemos un nombre que no conocemos...

        self.btn_Arduino.setEnabled(True)
        self.btn_RecorderData.setEnabled(True)
        self.btn_Datos.setEnabled(True)

# M O D I F I C A N D O    P A N T A L L A   1

        self.ven1_Arduino.primerEtapa = True
        #botones
        self.ven1_Arduino.btn_Conectar.setEnabled(True)
        self.ven1_Arduino.cmbBox_velocidad.setEnabled(False)

        # barra y todas las etiquetas hay que reiniciairlas
        self.ven1_Arduino.bel_Arduino.setText("")
        self.ven1_Arduino.bel_pantalla1.setText("")
        self.ven1_Arduino.bel_pantalla2.setText("")
        self.ven1_Arduino.proBar_carga.setValue(0)

# M O D I F I C A C I O N E S    P A N T A L L A   2
        #Ponemos a que apunte a un objeto nulo
        self.ven2_Accion.punterDicArduinos=""
        self.ven2_Accion.btn_cancel.setEnabled(False)
        self.ven2_Accion.btn_startPause.setEnabled(False)
        self.ven2_Accion.btn_terminar.setEnabled(False)

    #INDICADORES DE DISPOSITIVOS CONECTADOS...
        self.ven2_Accion.bel_Arduino.setText("")
        self.ven2_Accion.bel_pantalla1.setText("")
        self.ven2_Accion.bel_pantalla2.setText("")
        self.ven2_Accion.proBar_carga.setValue(0)

    #DATOS PEQUEÑOS...
        #self.ven2_Accion.belData1_long.setText("")
        #self.ven2_Accion.belData2_lat.setText("")
        #self.ven2_Accion.belData3_velo.setText("")
        #self.ven2_Accion.belData_dist.setText("")
    #DATOS GRANDES...
        #self.ven2_Accion.bel_altitude.setText("")
        #self.ven2_Accion.bel_altitude.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        #self.ven2_Accion.bel_CDA.setText("")
        #self.ven2_Accion.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        #self.ven2_Accion.bel_payLoad.setText("")
        #self.ven2_Accion.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
    #EL BOTON REGRESAR PAUSAR REGRESA A SU METODO PRINCIPAL
        self.ven2_Accion.btn_startPause.setText("Start")


# M O D I F I C A N D O    P A N T A L L A   3
        #self.ven3_Tabla.limpiarTabla()
        #self.ven3_Tabla.bel_CDA.setText("")
        #self.ven3_Tabla.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
        #self.ven3_Tabla.bel_payLoad.setText("")
        #self.ven3_Tabla.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")



#   Esta configuracion aplica cuando se inicia el vuelo
#   pues se borran los datos de las etiquetas del vuelo anterior
#   para evitar posibles confusiones
    def confiFase_2(self):

    #DATOS PEQUEÑOS...
        self.ven2_Accion.belData1_long.setText("")
        self.ven2_Accion.belData2_lat.setText("")
        self.ven2_Accion.belData3_velo.setText("")
        self.ven2_Accion.belData_dist.setText("")
    #DATOS GRANDES...
        self.ven2_Accion.bel_altitude.setText("")
        self.ven2_Accion.bel_altitude.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        self.ven2_Accion.bel_CDA.setText("")
        self.ven2_Accion.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")

        self.ven2_Accion.bel_payLoad.setText("")
        self.ven2_Accion.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
    #EL BOTON REGRESAR PAUSAR REGRESA A SU METODO PRINCIPAL
        self.ven2_Accion.btn_startPause.setText("Start")


# M O D I F I C A N D O    P A N T A L L A   3
        self.ven3_Tabla.bel_nameFile.setText("")  # Le ponemos un nombre que no conocemos...
        self.ven3_Tabla.limpiarTabla()
        self.ven3_Tabla.bel_CDA.setText("")
        self.ven3_Tabla.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
        self.ven3_Tabla.bel_payLoad.setText("")
        self.ven3_Tabla.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")










app = QApplication(sys.argv)
dialogo =AeroRoni()
dialogo.show()
app.exec_()








