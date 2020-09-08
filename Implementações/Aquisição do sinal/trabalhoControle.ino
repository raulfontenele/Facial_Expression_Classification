#include <ArduinoJson.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <math.h>

#define LED_MA 13
#define LED_MF 26
#define LED_MB 12
#define LED_MC 14
#define size_arrays 1000

int StartAt = 7;
String am[] = {"Neutro","Sorriso","Aberto","Surpreso","Grumpy"};
String string [5];
const long interval = 5000;
const char* ssid = "Gardenal";
const char* password =  "123456789";
//const char* ssid = "PAUNOGATO";
//const char* password =  "12345678";
unsigned long RealTime;
unsigned long previousTime=0;
String route;
int sens1[size_arrays];
int sens2[size_arrays];
String status_application ="Trab_Controle";
String status_esp32 ="a";
String gesture1 ="a";
String gesture2 ="a";
String gesture3 ="a";
String gesture4 ="a";
String gesture5 ="a";
String json;

String pertinent_info ="a";
String adtional_info ="a";

double weights1 = 2;
double weights2 = 3;
double weights3 = 5;

int sensor1Value;
int sensor2Value;
unsigned long first;
unsigned long last;



void setup() {
  // put your setup code here, to run once:
   sensor1Value = analogRead(32);
   sensor2Value= analogRead(34);
   
    
    pinMode(LED_MF,OUTPUT);
    pinMode(LED_MB,OUTPUT);
    pinMode(LED_MA,OUTPUT);
    pinMode(LED_MC,OUTPUT);
    Serial.begin(115200);
    delay(4000); 
 
    WiFi.begin(ssid, password); 
    while (WiFi.status() != WL_CONNECTED) { //Check for the connection
      
      
      digitalWrite(LED_MF,HIGH);
      digitalWrite(LED_MB,HIGH);
      digitalWrite(LED_MA,HIGH);
      digitalWrite(LED_MC,HIGH);
      delay(500);
      Serial.println("Connecting to WiFi..");      
      digitalWrite(LED_MF,LOW);
      digitalWrite(LED_MB,LOW);
      digitalWrite(LED_MA,LOW);
      digitalWrite(LED_MC,LOW);      
      delay(500);
    }
    Serial.println("CONNECTED");      
    int x;
    for(x=0;x<10;x++){
      digitalWrite(LED_MF,!digitalRead(LED_MF));
      digitalWrite(LED_MB,!digitalRead(LED_MB));
      digitalWrite(LED_MA,!digitalRead(LED_MA));
      digitalWrite(LED_MC,!digitalRead(LED_MC));
      delay(200);
    }
    digitalWrite(LED_MF,LOW);
    digitalWrite(LED_MB,LOW);
    digitalWrite(LED_MA,LOW);
    digitalWrite(LED_MC,LOW);
    delay(1000);
    
    
      

}

String ultimateCharConverter(){
  int i;
  String json1="{\"status_application\":\""+status_application+"\",";
  json1+="\"status_esp32\":\""+status_esp32+"\",";
  json1+="\"gesture1\":\""+gesture1+"\",";
  json1+="\"gesture2\":\""+gesture2+"\",";
  json1+="\"gesture3\":\""+gesture3+"\",";
  json1+="\"gesture4\":\""+gesture4+"\",";
  json1+="\"gesture5\":\""+gesture5+"\",";
  json1+="\"pertinent_info\":\""+pertinent_info+"\",";
  json1+="\"adtional_info\":\""+adtional_info+"\",\"sensor1\":[";
  for(i=0;i<size_arrays;i++){
    if(i!=size_arrays-1){
      json1+= "\""+String(sens1[i])+"\",";
    }else{
      json1+= "\""+String(sens1[i])+"\"";
    }
  }
  json1+="],\"sensor2\":[";
   for(i=0;i<size_arrays;i++){
     if(i!=size_arrays-1){
      json1+= "\""+String(sens2[i])+"\",";
    }else{
      json1+= "\""+String(sens2[i])+"\"";
    }
  }
  json1+="],";
  json1+="\"weights1\":[\""+String(weights1)+"\"],";
  json1+="\"weights2\":[\""+String(weights2)+"\"],";
  json1+="\"weights3\":[\""+String(weights3)+"\"]}";
  

  return json1;
}

void ClearArrayElements(){
  int i;
  for(i=0;i<size_arrays;i++){
    sens1[i] =0;
    sens2[i] =0;
  }
}

void PutRequest(int id){  
  String message = ultimateCharConverter();

  ClearArrayElements();
  route = "http://192.168.0.17/webapp/tcc/public/api/info/"+String(id)+"/edit";
  //route = "http://192.168.137.1/webapp/tcc/public/api/info/"+String(id)+"/edit";

  delay(5000);
  HTTPClient http;
  http.begin(route);
  
  http.addHeader("Content-Type", "application/json");             //Specify content-type header

  int httpResponseCode = http.PUT(message);  
  if(httpResponseCode>0){   
      String response = http.getString(); 
      Serial.println(response);
  }else{
      Serial.println("ERRO");
      Serial.println(httpResponseCode);
  }
   
   http.end(); 

}

void TrainRoutine(){
 
  int i;
  int d=0;
  int blob=1;
  for(i=1;i<=50;i++){
       if(blob==i){
        digitalWrite(LED_MC,LOW);
        blob+=5;
       }


       PreSettingsRecording();       
       gesture3 = am[d];
      
       if(i%5==0){
        digitalWrite(LED_MC,HIGH);
       }
       delay(1000);
       PutRequest(StartAt);
       
       delay(2000);
       StartAt++;
       d++;
       if(d>4){
        d=0;
       }
   }
  
}

void PreSettingsRecording(){
   int i;  
   digitalWrite(LED_MF,HIGH);
   delay(3000);
   digitalWrite(LED_MA,HIGH);
   //delay(1000);
   
  for(i=0;i<size_arrays;i++){
    //sensor1Value = 9999;
    //sens1[i] = sensor1Value;    
    //delay(1);
    //sensor2Value= 8888;    
    //sens2[i] = sensor2Value;

    sensor2Value= analogRead(34);    
    sens2[i] = sensor2Value;
    delay(3
    );  
    sensor1Value = analogRead(32);
    sens1[i] = sensor1Value;
    if(i>(size_arrays/2)){      
      digitalWrite(LED_MB,HIGH);      
      digitalWrite(LED_MC,HIGH);
    }

  }
  Serial.println("FIM AQUISICAO");
  digitalWrite(LED_MF,LOW);
  digitalWrite(LED_MA,LOW);
  digitalWrite(LED_MB,LOW);      
  digitalWrite(LED_MC,LOW);
}
bool control = true;
void loop() {
  // put your main code here, to run repeatedly:

  if ((WiFi.status() == WL_CONNECTED)) {
    if(control){
      first = millis();
      TrainRoutine();
      control = false;
      last = millis();

      
      long x =((last-first)/1000)/60;
      Serial.println(x);
      digitalWrite(LED_MF,HIGH);
      digitalWrite(LED_MB,HIGH);
      digitalWrite(LED_MA,HIGH);
      digitalWrite(LED_MC,HIGH);
    }
    
  }else{
    
  }

}
