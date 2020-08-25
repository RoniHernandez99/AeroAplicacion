#include <LCDWIKI_GUI.h> //Core graphics library
#include <LCDWIKI_KBV.h> //Hardware-specific library

//the definiens of 16bit mode as follow:
//if the IC model is known or the modules is unreadable,you can use this constructed function
LCDWIKI_KBV mylcd(ILI9486,40,38,39,-1,41); //model,cs,cd,wr,rd,reset

//define some colour values
#define  BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
//#define GREEN   0x07E0
#define GREEN 0x2D760B  //COLOR ELEGIDO
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

#define GREEN_NELLY 0x5BBF09


void setup(){
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//    CLAVE DE ACCESO 
          int claveAcceso=1928;  //clave que debe mandar python para que la pantalla sepa que se quiere comunicar con ella
          int claveRecibida=0;    //variable que almacenara las claves que manden los dispositivos
          char charAcceso='*';
          String nombreDispositivo="pantalla_2";
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


enum mensajesPantalla{altitud_CDA,fueLanzado_CDA,altitud_PAYLOAD,fueLanzado_PAYLOAD};
//enum mensajesPantalla{altitud_CDA,altitud_PAYLOAD,fueLanzado_CDA,fueLanzado_PAYLOAD};
char G_espacio[]={"     "};


char G_mensaje[][30]={
                      {"CDA Altitude:    "},    //0
                      {"Payload Altitude: "},   //1
                }; 
                
char G_medida[][5]={
                      {"[ft]"}, 
                      {"[ft]"}, 
                };                 
                
byte G_noDatos=4;


//Los datos a recibir son 4:
//      A)  CDA Altitude
//      B)  Payload Altitude
//      C)  Si ya se lanzaron los CDA     (1=SI 2=NO)
//      D)  Si ya se lanzaron los Payload (1=SI 2=NO)
//Recordar que para que una cadena de datos sea valida tiene
//que iniciar con el simbolo INICIO el cual me parece es asterisco
//Recordar que cada dato va separado por un caracter


float G_datos[4]={125.5,125.5,0,0};

bool yaSeNotifico[2]={false,false}; //ya fue lanzado...

void loop() {
  procesarDatos();
  if( G_datos[fueLanzado_CDA] || G_datos[fueLanzado_PAYLOAD]){
      if(G_datos[fueLanzado_CDA] && !yaSeNotifico[fueLanzado_CDA-2]){
        yaSeNotifico[fueLanzado_CDA-2]=true;
        mylcd.Set_Text_Mode(0); //modo del texto sin color de fondo
        mylcd.Set_Text_Back_colour(GREEN);
        mylcd.Set_Rotation(1); //en que posicion vamos a escribir en la pantalla...
        mylcd.Fill_Rect(0,10,480,150,GREEN);
        imprimirDatos_CDA();
      }
  
      if(G_datos[fueLanzado_PAYLOAD] && !yaSeNotifico[fueLanzado_PAYLOAD-2]){
        yaSeNotifico[fueLanzado_PAYLOAD-2]=true;
        mylcd.Set_Text_Mode(0); //modo del texto sin color de fondo
        mylcd.Set_Text_Back_colour(GREEN);
        mylcd.Set_Rotation(1); //en que posicion vamos a escribir en la pantalla...
        mylcd.Fill_Rect(0,180,480,150,GREEN);
        //imprimir PAYLOAD && el cuadro
        imprimirDatos_PAYLOAD();
      
      }
  }

  if( !yaSeNotifico[fueLanzado_CDA-2]  ){ //IMPRIMIR DATOS
    //imprimir CDA
    mylcd.Set_Text_Mode(0); //modo del texto sin color de fondo
    mylcd.Set_Text_Back_colour(BLACK);
    imprimirDatos_CDA();
  }
  if( !yaSeNotifico[fueLanzado_PAYLOAD-2]){
    //imprimir PAYLOAD
    mylcd.Set_Text_Mode(0); //modo del texto sin color de fondo
    mylcd.Set_Text_Back_colour(BLACK);
    imprimirDatos_PAYLOAD();
  }

}


void imprimirDatos_CDA(){
   mylcd.Set_Text_Size(3); //tamaño de la letra
   mylcd.Print_String(G_mensaje[0],30,20);//altitud_CDA==>0
   
     mylcd.Set_Text_Size(10); //tamaño de la letra
     mylcd.Print_String(G_espacio,70,65);   
     mylcd.Print_Number_Float(G_datos[altitud_CDA],1,70,65 ,'.',5,' ');
     mylcd.Set_Text_Size(3); //tamaño de la letra
     mylcd.Print_String(G_medida[altitud_PAYLOAD],380,120);
}

void imprimirDatos_PAYLOAD(){
   mylcd.Set_Text_Size(3); //tamaño de la letra
   mylcd.Print_String(G_mensaje[1],30,190);//altitud_PAYLOAD==>1
   
     mylcd.Set_Text_Size(10); //tamaño de la letra
     mylcd.Print_String(G_espacio,70,235);
     
     mylcd.Print_Number_Float(G_datos[altitud_PAYLOAD],1,70,235 ,'.',5,' ');
     mylcd.Set_Text_Size(3); //tamaño de la letra
     mylcd.Print_String(G_medida[altitud_PAYLOAD],380,280);  
}



//    *10,20,0,0
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
  char* nombrePantalla="SCREEN 2";
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
  char* nombrePantalla="SCREEN 2";
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
