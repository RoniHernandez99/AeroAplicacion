# re utiliza el modulo re para la validacion
import os
import time
import serial.tools.list_ports
import serial
from PyQt5.QtCore import pyqtSignal, QThread  # hilos

'''


'''


# _Requisitos para usar esta clase...(puerto,velocidad,noDatosEsperan,separador,nameFile)
class HiloArduinos(QThread):
    salirPorError = pyqtSignal(int)  # generar señal por si se cometio algun error...
    dispositivoConecto= pyqtSignal(str)# te dira el nombre del dispositivo que se conecto
    dispositivoDesconecto=pyqtSignal(str)#te dira el nombre del dispositivo que se desconecto
    hiloTerminadoExitosamente=pyqtSignal(bool)#Cuando terminemos de usarlo terminarlo
                                              #pero est señal nos dira que ha terminado
                                              #de manera exitosa para ya poder eliminarlo


    def __init__(self,velocidad,nombresDispositivos,clave):
        super().__init__()
        self.velocidad=velocidad
        self.nombresDipositivos=nombresDispositivos
        self.clave=clave
        # puertosRegistrados[id]=[arduino,idArduino]
        self.puertosRegistrados={}

        # Atributos criticos
        self.terminarHilo = False  # Se acabo de usar el hilo satisfactoriamente
        self.cancelarHilo = False  # Por alguna razon se decidio cancelar la funcion del hilo
        self.hiloPausado = True  # Lo pausamos ini cialmente para que solo cree el archivo
        # pero todavia no empieze a almacenar los datos


###############################################################################################################################33
## ¿Que hace la función?
#  Esta funcion se encargara de revisar que los arduinos que tenemos registrados
#  sigan conectados, de no ser ese el caso, los elimina del diccionario que
#  contiene dicho registro
#
#  puertosRegistrados==>Representa un diccionario, que contiene:
#               {
#                   nombrePantalla1:objetoSerial,
#                   nombrePantalla2:objetoSerial,
#                   nombreTransmisor:objetoSerial
#                 }
#
#  listaConectados==>Representa la lista de str que son los nombres de los
#                    puertos seriales que se encontraron
    def cerrarArduinosDesconectados(self,puertosRegistrados,listaPuertosConectados):
        #puertosRegistrados.items===> (nombreArduino,objetoArduino)
        puertosYaRegistramos=tuple(puertosRegistrados.items())
        for arduinoRegistrado in puertosYaRegistramos:
            #Si no esta el arduino en los arduinosRegistrado en la lista de puertos actualizada
            #significa que ya fue desconectado y por lo tanto tenemos que eliminarlo del registro
            if not(arduinoRegistrado[1].port in listaPuertosConectados):
              self.dispositivoDesconecto.emit(str(arduinoRegistrado[0]) )#mandar señal de que se desconecto X dispositivo
              # cerrar el puerto del arduino que ya no se encuentra registrado
              puertosRegistrados[arduinoRegistrado[0]].close()
              # eliminarlo del diccionario el arduino que ya no es cuentra registrado
              print(f"arduino {arduinoRegistrado[0]} va a morir")
              del puertosRegistrados[ arduinoRegistrado[0] ]
              print(puertosRegistrados)



#¿Que hace la funcion?
# La funcion se comunica con el posible arduino, le manda un codigo, que solo los
# arduinos programados para recibir dicho codigo entenderan.Despues de mandar el
# codigo esperara una respuesta deseada, si no recibe lo esperado, o el arduino
# no responde, se eliminara el objeto,pero en caso contrario se agregara a los
#puertos registrados
#  puertosRegistrados==>Representa un diccionario, que contiene:
#               {
#                   nombrePantalla1:objetoSerial,
#                   nombrePantalla2:objetoSerial,
#                   nombreTransmisor:objetoSerial
#                 }
#
#  arduino==>Representa el puntero al obeto serial creado para poder comunicarnos via serial
#            con los arduinos
    def esArduinoDeseado(self,puertosRegistrados,arduino):
        arduino.timeout=3 #tiempo de espera a 1 respuesta sera 1 segundo
        try:
            #Repetimos el proceso 3 veces...
            for _ in range(3):
                #arduino.reset_input_buffer()#vaciamos el bufer de entrada
                #arduino.reset_output_buffer()#vaciamos el buder de salida
                arduino.write( bytes(self.clave,'utf-8') )#manda clave de mensaje...
                nombreArduino=arduino.readline()#espera la respuesta del dispositivo
                print("datorecibido=",nombreArduino)
                print("\t1)SEÑAL INSISTENTE")
                nombreArduino=nombreArduino.decode("utf-8")[:-2]#quitamos el \r\n y decidificamos ya estan en bytes
                if nombreArduino in self.nombresDipositivos: #checamos si el dispositivo que queremos es el que deseamos....
                  print("\t\ŧRESPUES RECIPROCA: ",type(arduino))
                  print(f"\ŧ\ŧBievenido {nombreArduino} a python!! :)")#le damos la bienvenida al dispositivo
                  puertosRegistrados[nombreArduino]=arduino
                  self.dispositivoConecto.emit(nombreArduino)#enviamos el nombre del arduino que se acabo de conectar
                  return True
            arduino.close()#como no es un arduino deseado nos desconectamos de el...
            del(arduino)#destruimos el objeto
            return False
        except:
            print("Arduino desconectado")
            arduino.close()
            del(arduino)#destruimos el objeto



    def revisarPorts(self,puertosRegistrados):
        puertosFind= serial.tools.list_ports.comports()  # obtenemos la lista de los puertos encontrados...                                                  #que fueron localizados por la computadora
        puertosFind = sorted(puertosFind)  # ordenamos los puertos de forma acendiente...
        listPuertosFind=[x.device for x in puertosFind]  # lista de los nombres de los puertos seriales encontrados...
        listRegistrados = tuple((ard.port for ard in puertosRegistrados.values()))#lista de los nombres de los puertos
                                                                                  #registrados
        puertosNoDeseados = ["/dev/ttyAMA0"]

        print("PUERTOS ENCONTRADOS....",listPuertosFind)
        #Checamos que no tengamos ningun arduinoRegistrado si no esta conectado....
        #Se manda el diccionario de puertos registrados debido a que este se modificara
        #por paso por referencia de ser que se haya desconectado un arduino...
        self.cerrarArduinosDesconectados(puertosRegistrados,listPuertosFind)
        for puertoFind in listPuertosFind:
            #si no esta en el dispositivo registrado....
            if not(puertoFind in listRegistrados) and not(puertoFind in puertosNoDeseados): #si el puerto detectado no se encuentra ya registrado
              try:
                arduino=serial.Serial(port=puertoFind,baudrate=self.velocidad)#conectandonos a posible arduino
                print("PUERTO A EVALUAR..",arduino.port)
                self.esArduinoDeseado(puertosRegistrados,arduino)#nos sercioramos que de que sea el dispositivo
                                                                  #que nosotros buscamos
              except:
                print("u_U")

# puertos registrados
#  puertosRegistrados==>Representa un diccionario, que contiene:
#               {
#                   nombrePantalla1:objetoSerial,
#                   nombrePantalla2:objetoSerial,
#                   nombreTransmisor:objetoSerial
#                 }
    def run(self):
        #puertosRegistrados[id]=[arduino,idArduino]
        #self.puertosRegistrados = {}
        while not(self.terminarHilo):
            self.revisarPorts(self.puertosRegistrados)
            time.sleep(.2)
        #Cerrando todos los puertos seriales antes de irnos
        for idArduino,arduino in self.puertosRegistrados.items():
            arduino.close()

        self.hiloTerminadoExitosamente.emit(True)
        print("PROCESO TERMINADO CON MUCHO PUTO EXITO HILOARDUINO AJUA!!!")




