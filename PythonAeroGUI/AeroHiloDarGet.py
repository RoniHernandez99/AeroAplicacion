# re utiliza el modulo re para la validacion
import os
import time
import serial.tools.list_ports
import serial
from PyQt5.QtCore import pyqtSignal, QThread  # hilos

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


    La clase tiene tambien una señal cuyo nombre es 'datosRecibidos' la cual
    se ejecuta cada vez que recibe un dato de arduino...
    Retornara una lista de strings de los datos que le llegan


LOS DATOS QUE RECIBE LA SEGUNDA PANTALLA.....
//Los datos a recibir son 4:
//      A)  CDA Altitude
//      B)  Payload Altitude
//      C)  Si ya se lanzaron los CDA     (1=SI 2=NO)
//      D)  Si ya se lanzaron los Payload (1=SI 2=NO)
//Recordar que para que una cadena de datos sea valida tiene
//que iniciar con el simbolo INICIO el cual me parece es asterisco
//Recordar que cada dato va separado por un caracter


LOS DATOS QUE RECIBE LA PRIMERA PANTALLA
//Los datos a recibir son 5:
//      A)  Aicreaft Altitude
//      B)  Speed
//      C)  Latitude
//      D)  Longitude
//      E)  Distance to target


¿Como me llegara la cadena de informacion?
//  [0] Altura   [1] velocidad  [2]latitud [3]longitude  [4]distanceTarget

//Recordar que para que una cadena de datos sea valida tiene
//que iniciar con el simbolo INICIO el cual me parece es asterisco
//Recordar que cada dato va separado por un caracter


'''


# _Requisitos para usar esta clase...(puerto,velocidad,noDatosEsperan,separador,nameFile)
class HiloArdDarGet(QThread):
    salirPorError = pyqtSignal(int)  # generar señal por si se cometio algun error...
    datosRecibidos = pyqtSignal(str)
    senalLanzado_CDA=pyqtSignal(str) #esta señal solo se mandara una vez y es cuando se lanzan CDA(planeadores)
    senalLanzado_payLoad=pyqtSignal(str)#esta señal solo se mandara una vez y es cuando se han lanzado los PayLoads(carga)

    hiloTerminadoExitosamente=pyqtSignal(int)#Cuando terminemos de usarlo terminarlo
                                              #pero est señal nos dira que ha terminado
                                              #de manera exitosa para ya poder eliminarlo
                                              #aparte de que retorna el numero de datos recopilados

    hiloListoUsarse=pyqtSignal(bool)

    def __init__(self,dictArduinos,noDatosEsperan, separador, nameFile):
        self.objetoReferencia=dictArduinos
        #    pantalla_1
        #    pantalla_2
        #    transmisor
        super().__init__()
        self.dictArduinos=dictArduinos

        # Atributo que se necesita para serciorar de que hubo
        # una correcta y completa entrega de datos
        self.noDatosEsperan = noDatosEsperan
        self.separador = separador

        # Atributo necesario para saber donde guardaremos los datos
        self.nameFile = nameFile

        # Atributos criticos
        self.terminarHilo = False  # Se acabo de usar el hilo satisfactoriamente
        self.cancelarHilo = False  # Por alguna razon se decidio cancelar la funcion del hilo
        self.hiloPausado = True  # Lo pausamos inicialmente para que solo cree el archivo
        # pero todavia no empieze a almacenar los datos

    def run(self):
        #DATOS PARTICULARES DEL VUELO.....
        dates_objeto1LanzadoCDA = []
        dates_objeto2LanzadoPayLoad = []
        cadaCuando = 4
        contador = 0

        print("HOla que pedo carnales")
        self.hiloListoUsarse.emit(True)
        self.archivo=""


        #Por si se llega a desconectar el transmisor...
        while self.terminarHilo == False and self.cancelarHilo == False:
            try:
                self.dictArduinos["transmisor"].reset_input_buffer()  # limpiamos el bufer de entrada del arduino transmisor
                self.dictArduinos["transmisor"].reset_output_buffer()  # limpiamos el bufer antes de enviar
                self.archivo = open(self.nameFile, "w")  # creando  archivo de escritura al final
                # Mientras NO se quiera terminar el hilo y tampoco se quiera cancelar
                # vamos a repetir....
                break
            except:
                print("error al inicio, intentaremos nuvamente...")

        while self.terminarHilo == False and self.cancelarHilo == False:
            try:
                dato = self.dictArduinos["transmisor"].readline()  # esperando hasta un salto de linea
                dato = str(dato.decode("utf-8"))
                # print(dato,end="===>")
                lista=dato.split(self.separador)  #la cadena que nos llego la convertimos en una lista
                noDatosRecibidos = len(dato.split(self.separador))#contamos el tamaño de la cadena
                # print(noDatosRecibidos) lo utilizamos para visualizar a los datos
                # Si el numero de datos recibido es igual al umero de datos que se esperan
                # significa que llego  completo el mensaje...
                self.dictArduinos["transmisor"].reset_input_buffer()  # limpiamos bufer de entrada
                # Si el hilo no esta pausado significa que no podemos escribir datos en el fichero
                if noDatosRecibidos == self.noDatosEsperan and self.hiloPausado == False:
                    self.archivo.write(dato)  # decodificando los bytes en le fichero...
                    print(dato)
                    # Altitude,Speed,Latitude,Longitude,Time
                    # Tiempo,planeador1,planeador2
                    self.datosRecibidos.emit(dato)

                    #SIEMPRE SERCIOARAR QUE DEBEMOS GUARDAR ESE DATO
                    #Solo sucedera esto una vez,ya que la lista se
                    #se llenara una vez y apartir de ahi ya no estara vacia
                    # c h e  c a  r .....
                    print("QUE PASA AQUI SEÑO GARCIA..")
                    print(f"CDA==> {lista[-2]}==1?????????  ")
                    if dates_objeto1LanzadoCDA==[]  and int(float(lista[-2]))==1:
                        self.senalLanzado_CDA.emit(lista[0])
                        dates_objeto1LanzadoCDA = lista
                    print(f"payLoad==> {lista[-1]}==1?????????  ")
                    if dates_objeto2LanzadoPayLoad==[] and int(float(lista[-1]))==1:
                        self.senalLanzado_payLoad.emit(lista[0])
                        dates_objeto2LanzadoPayLoad = lista

                    print("holaaaaaaaaaaaaaaaaaaa")
                    #¿Ya es nuestro tiempo?
                    if (contador % cadaCuando == 0):
                        print("R\no\nn\ni")
                        cadena="*"

                        # P A N T A L L A       S E G U N D A :
                        try: #la segunda pantalla...
                            #¿tu lista sigue vacia porque no has recarga sin combustible?
                            if dates_objeto1LanzadoCDA==[]:
                                cadena+=lista[0]+",0,"
                            else:
                                cadena+=dates_objeto1LanzadoCDA[0]+",1,"

                            if dates_objeto2LanzadoPayLoad==[]:
                                cadena+=lista[0]+",0"
                            else:
                                cadena+=dates_objeto2LanzadoPayLoad[0]+",1"

                            print("Cadena mandada a la pantalla de los planeadores...",cadena)
                            self.dictArduinos["pantalla_2"].write(bytes(cadena,'utf-8'))
                        except:
                            pass

                        #P A N T A L L A     U N O :
                        try:#la primera pantalla

                            cadena=",".join(lista[:5])# [altura,vel,lat,long,dist]....planeadores,payload
                            cadena="*"+cadena
                            print(cadena)
                            self.dictArduinos["pantalla_1"].write(bytes(cadena,'utf-8') )#manda clave de mensaje...
                        except:
                            pass
                    contador += 1
            except:
                print("Hola que hace")
                pass
        if self.archivo!="":
          self.archivo.close()
        print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjoooooooooooooooooooooooooorrrrrrrrrrrrrrrr")
        self.hiloTerminadoExitosamente.emit(contador)#indicamos que el hilo ha sid terminado exitosamente
        print("PROCESO TERMINADO CON MUCHO PUTO EXITO dimos mucho hilo AJUA!!!")

