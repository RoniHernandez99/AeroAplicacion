#include <LCDWIKI_GUI.h> //Core graphics library
#include <LCDWIKI_KBV.h> //Hardware-specific library

//the definiens of 16bit mode as follow:
//if the IC model is known or the modules is unreadable,you can use this constructed function
LCDWIKI_KBV mylcd(ILI9486,40,38,39,-1,41); //model,cs,cd,wr,rd,reset

//define some colour values
#define  BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF
#define GREEN_NELLY 0x5BBF09


void setup() {
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//    CLAVE DE ACCESO 
          int claveAcceso=1928;  //clave que debe mandar python para que la pantalla sepa que se quiere comunicar con ella
          int claveRecibida=0;    //variable que almacenara las claves que manden los dispositivos
          char charAcceso='*';
          String nombreDispositivo="pantalla_1";
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
  mylcd.Init_LCD();
  showScreen_espera();
  Serial.begin(9600);
  while(claveRecibida!=claveAcceso){
    while(Serial.read()!=charAcceso){
    }
    claveRecibida=Serial.parseInt(); 
  }
  Serial.println(nombreDispositivo);
  Serial.println(nombreDispositivo);
  Serial.println(nombreDispositivo);
  showScreen_emparejada();
  delay(2000);
  mylcd.Fill_Screen(BLACK);


}

enum mensajesPantalla{ALTITUD,RAPIDEZ,LATITUD,LONGITUD,DISTANCIA};

char titleMain[]={"Aircraft Altitude: "};
char medidaMain[]={"[ft/s]"};
char G_espacio[]={"    "};


byte G_xInicioDatos=25;

char mensaje[][70]={
                      {"125.5     "  },   //apartir de la posicion 0 escribiremos los numeros
                      {"Speed:    "}, //apartir de la posicion 11 escribiremos los numeros
                      {"Latitude: "}, //apartir de la posicion 11 escribiremos los numeros
                      {"Longitude:"},    //apartir de la posicion 11 escribiremos los numeros
                      {"Distance\n"
                       " to target:"}     //apartir de la posicion 11 escribiremos los numeros
                }; 


byte G_noDatos=5;
float G_datos[5]={125.5,125.5,125.5,125.5,125.5};

//Los datos a recibir son 5:
//      A)  Aicreaft Altitude
//      B)  Speed
//      C)  Latitude
//      D)  Longitude
//      E)  Distance to target
//Recordar que para que una cadena de datos sea valida tiene
//que iniciar con el simbolo INICIO el cual me parece es asterisco
//Recordar que cada dato va separado por un caracter



void loop() {
   procesarDatos();
   imprimirMatrizDatos();
}


void imprimirMatrizDatos(){

  //numero,noDecimales,posX,posY,simboloDecimal,noTotalSimbolos,caracterPonerSiNoHayNumeros
  //Print_Number_Float(double num, uint8_t dec, int16_tx, int16_t y, uint8_t divider, int16_t length, uint8_t filler)
  
  mylcd.Set_Rotation(1); //en que posicion vamos a escribir en la pantalla...
  mylcd.Set_Text_Mode(0); //modo del texto sin color de fondo
  mylcd.Set_Text_colour(WHITE); //color de la letra
  mylcd.Set_Text_Back_colour(BLACK);
 

  
  mylcd.Set_Text_Size(3); //tamaño de la letra
  mylcd.Print_String(titleMain, 80,10);
  mylcd.Set_Text_Size(10); //tamaño de la letra

  

  mylcd.Set_Text_Size(3); //tamaño de la letra
  
  mylcd.Print_String(medidaMain,365,100);
  mylcd.Set_Text_Size(10); //tamaño de la letra
  mylcd.Print_String(G_espacio,70,50);
  mylcd.Print_Number_Float(G_datos[ALTITUD],1,70,50 ,'.',5,' ');
 



 // G_xInicioDatos=25  ==>representa apartir de donde se 
 // empezaran a escribir los datos...
 mylcd.Set_Text_Size(3); //tamaño de la letra
 mylcd.Print_String(mensaje[RAPIDEZ],G_xInicioDatos,150);
 mylcd.Print_String(G_espacio, G_xInicioDatos+200,150);
 mylcd.Print_Number_Float(G_datos[RAPIDEZ],1, G_xInicioDatos+200,150 ,'.',5,' ');
 
 mylcd.Print_String(mensaje[LATITUD], G_xInicioDatos,190);
 mylcd.Print_String(G_espacio, G_xInicioDatos+200,190);
 mylcd.Print_Number_Float(G_datos[LATITUD],1,  G_xInicioDatos+200,190 ,'.',5,' ');

 mylcd.Print_String(mensaje[LONGITUD],G_xInicioDatos,230);
 mylcd.Print_String(G_espacio, G_xInicioDatos+200,230);
 mylcd.Print_Number_Float(G_datos[LONGITUD],1, G_xInicioDatos+200,230 ,'.',5,' ');

 mylcd.Print_String(mensaje[DISTANCIA],G_xInicioDatos,270); 
 mylcd.Print_String(G_espacio, G_xInicioDatos+200,290);
 mylcd.Print_Number_Float(G_datos[DISTANCIA],1,G_xInicioDatos+200,290 ,'.',5,' ');

 
  
  
  
  

}



/*
   NO DATOS= Speed,Latitude,Longitude,Distance to target
                      {"125.5     "  },   //apartir de la posicion 0 escribiremos los numeros
                      {"Speed:           [ft/s]"}, //apartir de la posicion 11 escribiremos los numeros
                      {"Latitude:        [\xDF]"}, //apartir de la posicion 11 escribiremos los numeros
                      {"Longitude:       [m]"},    //apartir de la posicion 11 escribiremos los numeros
                      {"Distance\n "
                       "to target:       [m]"}     //apartir de la posicion 11 escribiremos los numeros   
-*/

void procesarDatos(){
  const char INICIO='*';
        while(Serial.read()!=INICIO){
          
        }
        for(int c=0;c<G_noDatos;c++){
           G_datos[c]=Serial.parseFloat();Serial.read();  
          } 
}

void showScreen_espera(){
  mylcd.Fill_Screen(RED); 
  char* nombrePantalla="SCREEN 1";
  char* mensaje="  Without\n connection!";
//PROPIEDADES DEL TEXTO...
  mylcd.Set_Rotation(1); //en que posicion vamos a escribir en la pantalla...
  mylcd.Set_Text_colour(WHITE); //color de la letra
  mylcd.Set_Text_Size(7); //tamaño de la letra
  mylcd.Print_String(nombrePantalla,20,20);
  mylcd.Set_Text_Size(6); //tamaño de la letra
  mylcd.Print_String(mensaje,45,140);
  //mylcd.Set_Text_Mode(1); //modo del texto sin color de fondo

}


void showScreen_emparejada(){
  mylcd.Fill_Screen(GREEN_NELLY); 
  char* nombrePantalla="SCREEN 1";
  char* mensaje=" Successful\n connection!";
  mylcd.Set_Text_Mode(1); //modo del texto sin color de fondo
//PROPIEDADES DEL TEXTO...
  mylcd.Set_Rotation(1); //en que posicion vamos a escribir en la pantalla...
  mylcd.Set_Text_colour(WHITE); //color de la letra
  mylcd.Set_Text_Size(7); //tamaño de la letra
  mylcd.Print_String(nombrePantalla,20,20);
  mylcd.Set_Text_Size(6); //tamaño de la letra
  mylcd.Print_String(mensaje,45,140);
  //mylcd.Set_Text_Mode(1); //modo del texto sin color de fondo

}
