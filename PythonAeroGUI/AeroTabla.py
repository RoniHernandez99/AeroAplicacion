# https://stackoverflow.com/questions/53627316/how-to-create-widget-in-pyqt5-to-show-google-map

# re utiliza el modulo re para la validacion
import sys, re,os
import datetime
import time

######################3

#####################################################
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog,QTableWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon   #para poner un icono

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget
from PyQt5 import  QtWidgets

from AeroTabla_d2 import Ui_Form
#########################################################################################################
#           D E  F I  N  I  C I O  N      D E    L  A     C L  A  S  E  :   => R O N I    H D Z         #                       #
########################################################################################################
class Tabla(QWidget,Ui_Form):
    #Metodo constructor:
    def __init__(self):
       Ui_Form.__init__(self)
       QWidget.__init__(self)
       self.setupUi(self)
########################################################################################

       self.nombresColumnas = ["Altitude", "Speed", "Latitude", "Longitude", "Distance", "CDA", "PayLoad"]
       self.noColumnasTabla=len(self.nombresColumnas)
       self.punteroFilas=0
       self.limpiarTabla()


    # B O T O N E S :
       self.btn_abrirTabla.clicked.connect(self.escogerTabla)  # escogeremos la tabla que queremos abrir
       self.btn_borrarNew.clicked.connect(self.limpiarTabla)

    # T A B L A :
       #self.tablaDatos.cellActivated.connect(self.mostrarDatos)
       #self.tablaDatos.cellClicked.connect(self.mostrarDatos)






# ***********************************************************************************************************************
#  C   A    R     P   E   T    A    S
# ***********************************************************************************************************************

# es la carpeta que aparecera cuando se decida abrir un archivo
# es la carpeta en la cual se guardaran los resultados...


    def limpiarTabla(self):
        self.incializarTabla(10)#la inicializo con 10 renglones paara que se pueda apreciar como
                                #quedara la tabla
        self.bel_payLoad.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
        self.bel_CDA.setStyleSheet("background-color:rgb(24,170,229);font: 50pt;border-radius: 10px;")
        self.bel_payLoad.setText("")
        self.bel_CDA.setText("")

    def incializarTabla(self,noRenglones):
        self.tablaDatos.clear() #borramos la tabla
        self.tablaDatos.setColumnCount(self.noColumnasTabla)
        self.tablaDatos.setRowCount(noRenglones)
        #Diseño de la cabecera de la tabla...
        stylesheet = "QHeaderView::section{Background-color:rgb(190,1,1);border - radius: 14px;font: 15pt;height:25px} font:16pt;"
        self.tablaDatos.setStyleSheet(stylesheet)
        self.tablaDatos.setFont(QtGui.QFont("Ubuntu", 12))
        # si selecccionas una sola casilla seleccionan todas las casilas por renglon
        self.tablaDatos.setSelectionBehavior(QTableWidget.SelectRows)
        # Desactivar la vista de los renglones
        self.tablaDatos.verticalHeader().setVisible(False)
        #Desactivar para que no puedan editar la tabla
        self.tablaDatos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for n in range(self.noColumnasTabla):
            self.tablaDatos.setHorizontalHeaderItem(n, QtWidgets.QTableWidgetItem(self.nombresColumnas[n]))


    def openFileAeron(self,nameFileAeron):
        CDA_tirado=False
        payLOAD_tirado=False



        # del fichero que se escogio...
        if not(nameFileAeron==""):
            rutaFile=nameFileAeron.split("/") #separando cada uno por /
            rutaFile=rutaFile[:-1]#eliminando el nombre del archivo
            print(rutaFile)
            nuevaRuta=""
            for x in rutaFile:
                nuevaRuta+= ("/"+str(x))
            self.bel_nameRoute.setText(nuevaRuta)

            file=open(nameFileAeron,'r')
            file.seek(0)#Ubicamos el puntero en la posicion cero
            dateInicio=file.readline()#Fecha de inicio del vuelo
            dateFinal=file.readline()#Fecha de termino del vuelo
            dateTime=file.readline()#Tiempo de vuelo total

            self.bel_dateStart.setText(dateInicio)
            self.bel_dateEnd.setText(dateFinal)
            self.bel_duracion.setText(dateTime)
            noFilas=0
            #Contando el tamño del archivo
            while file.readline()!="":
                noFilas+=1
            file.close()
            file = open(nameFileAeron, 'r')
            file.readline()#Fecha del inicio del vuelo
            file.readline()#fecha del termino del vuelo
            file.readline()#duracion del video


        #Se crea la tabla con el numero de renglones respectivo...
            self.incializarTabla(noFilas)
        #Llenando cada celda...
            for r in range(noFilas):
                renglonTabla = file.readline().split(",")
                if not (CDA_tirado) and int(float(renglonTabla[-2])) == 1:
                    self.bel_CDA.setStyleSheet("background-color:green;font: 50pt;border-radius: 10px;}")
                    self.bel_CDA.setText(renglonTabla[0])
                    CDA_tirado = True
                    reglon_CDA = r
                if not (payLOAD_tirado) and int(float(renglonTabla[-1])) == 1:
                    self.bel_payLoad.setStyleSheet("background-color:green;font: 50pt;border-radius: 10px;}")
                    self.bel_payLoad.setText(renglonTabla[0])
                    payLOAD_tirado = True
                    reglon_payLoad = r


                for c in range(self.noColumnasTabla):
                    print(r, ",", c)
                    self.tablaDatos.setItem(r, c, QtWidgets.QTableWidgetItem(renglonTabla[c]))

            file.close()
            if CDA_tirado:
                print("gdsssssssssssssssssssssssssssssssssssssssssssssss")
                for c in range(self.noColumnasTabla):
                    self.tablaDatos.item(reglon_CDA, c).setBackground(QtGui.QColor("green"))
            if payLOAD_tirado:
                print("gdsssssssssssssssssssssssssssssssssssssssssssssss")
                for c in range(self.noColumnasTabla):
                     self.tablaDatos.item(reglon_payLoad, c).setBackground(QtGui.QColor("green"))


    def escogerTabla(self):
        direc = self.bel_nameRoute.text() + "/"
        print("Nombre de la ruta", direc)

        # Archivo especificos...
        nameFileAeron = QFileDialog.getOpenFileName(self, 'Open file', direc, "Image files (*_aeron.csv)")
        nameFileAeron = str(nameFileAeron[0])  # fname es una tupla y en su primera posicion contiene el nombre
        self.openFileAeron(nameFileAeron)



    def escogerCarpetaFavorita(self):
        nombreCarpetaFavorita = "nameCarpetaFavorita.txt"
        direccion = ""
        # Solo carpetas
        fname = QFileDialog()
        direccion = fname.getExistingDirectory()

        if not (direccion == ""):
            print(direccion)
            archivo = open(nombreCarpetaFavorita, "w")
            archivo.write(direccion + "\n")
            archivo.close()


    '''
    
           self.tablaDatos.setItem(0,0,QtWidgets.QTableWidgetItem("Roni Hernandez") )
           self.tablaDatos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
           self.tablaDatos.cellActivated.connect(self.pantalla_tablaDatos)
           self.tablaDatos.cellClicked.connect(self.pantalla_tablaDatos)
           self.tablaDatos.item(0,0).setBackground(QtGui.QColor(125,125,125))#cambiar el color

           self.tablaDatos.cellActivated.connect(self.pantalla_tablaDatos)
           self.tablaDatos.cellClicked.connect(self.pantalla_tablaDatos)    
           #self.tablaDatos.cellChanged.connect(self.pantalla_datos)
           #self.tablaDatos.setSelectionBehavior(QTableWidget.SelectRows)
    
    
    
 
    def mostrarDatos(self, renglon, columna):
        #se actualizara en el numero de renglon en el que esta
        #["Altitude", "Speed", "Latitude", "Longitude", "Distance", "CDA", "PayLoad"]
        if renglon!=self.punteroFilas:
            self.punteroFilas=renglon
            self.belData_alt.setText(self.tablaDatos.item(renglon,0).text())
            self.belData_velo.setText(self.tablaDatos.item(renglon,1).text())
            self.belData_lat.setText(self.tablaDatos.item(renglon,2).text())
            self.belData_long.setText(self.tablaDatos.item(renglon,3).text())
            self.belData_dist.setText(self.tablaDatos.item(renglon,4).text())
    



    '''
if __name__ == "__main__":
 app = QApplication(sys.argv)
 dialogo = Tabla()
 dialogo.show()
 app.exec_()