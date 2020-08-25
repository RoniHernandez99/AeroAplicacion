# re utiliza el modulo re para la validacion
import os
import time
import serial.tools.list_ports
import serial
from PyQt5.QtCore import pyqtSignal, QThread #hilos

'''
    La clase HiloArduino abre el puerto serial con este y  
    crea un fichero con extension '_aeron.csv' el cual 
    va guardando los datos que le van llegando de arduino
    
    Tiene un atributo cuyo nombre es 'hiloPausado',el cual
    representa una variable de tipo bool donde si...
    hiloPausado=True ==>Significa que python dejara 
                        de escribir los datos que recibe de
                        arduino 
    hiloPausado=False==>Significa que python estara escribiendo
                        todos los datos que recibe de arduino     

    Tiene un atributo cuyo nombre es 'terminarHilo', el cual
    representa una variable de tipo bool donde si...
    terminarHilo=True==>A la primera vez que 'terminaHilo'
                        valga True se terminara la comunicacion
                        con arduino
    terminarHilo=False==>Mientras este atributo se mantenga con
                         ese valor python seguira en comunicacion
                         con arduino
    Este atributo sirve para terminar de usar el hilo 
    exitosamente


    Tiene un atributo cuyo nombre es 'cancerlarHilo', el cual
    representa una variable de tipo bool donde si...
    cancerlarHilo=True==>A la primera vez que 'terminaHilo'
                        valga True se terminara la comunicacion
                        con arduino
    cancerlarHilo=False==>Mientras este atributo se mantenga con
                         ese valor python seguira en comunicacion
                         con arduino
    Este atributo sirve para dejar de usar el hilo, no 
    guardando ningun dato
    
        
                         
                         
                         
    La clase tiene tambien una señal cuyo nombre es 'salirPorError' el cual
    se ejecuta cuando el proceso se ha terminado...
    Retornara el numero 1 si: Se se termino satisfactoriamente el servicio del hilo
    Retornara el numero 2 si: Se decidio cancelar el hilo...
    Retornara el numero 3 si: Si el hilo se termino por algun error de arduino
     
'''


#_Requisitos para usar esta clase...(puerto,velocidad,noDatosEsperan,separador,nameFile)
class HiloArduino(QThread):
    salirPorError = pyqtSignal(int)  # generar señal por si se cometio algun error...

    def __init__(self, puerto,velocidad,noDatosEsperan,separador,nameFile):
        super().__init__()

        #Obteniendo los datos del arduino del que nos queremos conectar....
        #Atributos necesarios para entablar comunicacion con arduino
        self.port = puerto
        self.velCom = velocidad

        #Atributo que se necesita para serciorar de que hubo
        #una correcta y completa entrega de datos
        self.noDatosEsperan = noDatosEsperan
        self.separador = separador

        #Atributo necesario para saber donde guardaremos los datos
        self.nameFile = nameFile

        #Atributos criticos
        self.terminarHilo= True #Se acabo de usar el hilo satisfactoriamente
        self.cancelarHilo=False #Por alguna razon se decidio cancelar la funcion del hilo
        self.hiloPausado = False

    def run(self):
        try:
            #Abrimos comunicacion con arduino
            self.arduino = serial.Serial(self.port, self.velCom)
            #Esperamos dos segundos para una correcta comunicacion
            time.sleep(2)
            self.arduino.reset_input_buffer()  # limpiamos bufer de entrada
            self.arduino.reset_output_buffer()  # se limpia bufer antes de enviar
            self.archivo = open(self.nameFile, "w")  # creando  archivo de escritura al final
            #Mientras NO se quiera terminar el hilo y tampoco se quiera cancelar
            #vamos a repetir....
            while  self.terminarHilo==False and self.cancelarHilo==False:
                dato = self.arduino.readline()  # esperando hasta un salto de linea
                noDatosRecibidos=len(dato.split(self.separador))
                #Si el numero de datos recibido es igual al umero de datos que se esperan
                #significa que llego  completo el mensaje...
                self.arduino.reset_input_buffer()  # limpiamos bufer de entrada
                # Si el hilo no esta pausado significa que no podemos escribir datos en el fichero
                if noDatosRecibidos==self.noDatosEsperan and self.hiloPausado==False:
                      self.archivo.write(dato.decode("utf-8")) # decodificando los bytes en le fichero...

            self.arduino.reset_input_buffer()  # limpiamos bufer de entrada
            self.arduino.reset_output_buffer()  # se limpia bufer antes de enviar
            self.arduino.close()
            self.archivo.close()

            if self.terminarHilo==True:  # se ha ternado el proceso con exito...
                self.salirPorError.emit(1)
            else:  # el proceso se ha cancelado...
                os.remove(self.nameFile)
                self.salirPorError.emit(2)

        except serial.serialutil.SerialException as error:
            self.archivo.close()
            os.remove(self.nameFile)  # borrando el archivo que se cancelo
            self.salirPorError.emit(3)
        except:
            self.archivo.close()
            os.remove(self.nameFile)  # borrando el archivo que se cancelo
            self.salirPorError.emit(3)


