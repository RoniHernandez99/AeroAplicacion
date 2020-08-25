
#define NODATOS 7  //va a mandar 6+1 dato el otro dato debido al tiempo...
double datos[NODATOS];


void setup() {
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//    CLAVE DE ACCESO 
          int claveAcceso=1928;  //clave que debe mandar python para que la pantalla sepa que se quiere comunicar con ella
          int claveRecibida=0;    //variable que almacenara las claves que manden los dispositivos
          char charAcceso='*';
          String nombreDispositivo="transmisor";
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
  Serial.begin(9600);
  while(claveRecibida!=claveAcceso){
    while(Serial.read()!=charAcceso){
    }
    claveRecibida=Serial.parseInt(); 
  }
  Serial.println(nombreDispositivo);
  Serial.println(nombreDispositivo);
  Serial.println(nombreDispositivo);
  delay(2000);

  //Establecemos la semilla en un pin analogico
  //randomSeed();    
}
int contadorDatos=0;
int inter[2]={0,9999};
void loop() {
  generarDatos(datos,NODATOS,inter,contadorDatos);
  mandarDatos(datos,NODATOS);
  delay(250);
  contadorDatos++;
  
}


void generarDatos(double* arrayDatos,int tam,int intervalo[2],int noDato){
  //Con la finalidad de obtener dos numeros decimales de cada numero
  int objeto1_tirado=0;
  int objeto2_tirado=0;
  int horaTirar=150;
  int inicio=intervalo[0]; 
  int fin=intervalo[1];
  arrayDatos[0]=double(millis()) /100.0;
  arrayDatos[0]=long(arrayDatos[0]);
  arrayDatos[0]=double(arrayDatos[0]/10.0);
  for(int c=1;c<tam-2;c++){//iniciamos en 1 por el tiempo
    arrayDatos[c]=double(random(inicio,fin))/100;
  }
  if (noDato>horaTirar){
        objeto1_tirado=1;
  }
  if (noDato>horaTirar+20){
        objeto2_tirado=1;
  }
  arrayDatos[tam-1]=objeto1_tirado;
  arrayDatos[tam-2]=objeto2_tirado;

  
}

void mandarDatos(double* arrayDatos,int tam){
  for(int c=0;c<tam;c++){
   Serial.print(arrayDatos[c]);
   if(c<tam-1)
    Serial.print(",");
  }
  Serial.println();
}

/*

  Random(max): Se obtiene un numero “aleatorio” desde 0 hasta max.
  Random(min, max): Se obtiene un numero “aleatorio” desde min hasta max

  Para conseguir que cada vez que iniciemos el skecth tengamos secuencias 
  diferentes tenemos que pasarle cada vez una semilla diferente.
  Esto lo conseguimos si como semilla le pasamos el valor de una entrada 
  analógica que no utilicemos en nuestro sketch mediante la función analogRead(). 
  Estos pin analógicos cuando no son utilizados no tienen ninguna tensión de
  referencia y devolverá un valor de ruido que será diferente cada vez que 
  preguntemos por su valor.

  //Establecemos la semilla en un pin analogico
  randomSeed(analogRead(A0));  
  

*/
