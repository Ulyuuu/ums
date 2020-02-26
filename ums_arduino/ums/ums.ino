#include <LiquidCrystal.h>
LiquidCrystal lcd1(8, 9, 7, 6, 5, 4);
LiquidCrystal lcd2(8, 10, 7, 6, 5, 4);

String s;

int bds = 9600;

int red = 11;
int green = 12;
int blue = 13;


void setup()
{
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  
  Serial.begin(bds);
  
  lcd1.begin(16, 2);
  lcd2.begin(16, 2);
  
  lcd1.setCursor(0, 0);
  lcd1.print("--- Ulyu MS ----");
  lcd2.setCursor(0, 0);
  lcd2.print(bds);
  lcd2.setCursor(5, 0);
  lcd2.print("Bds");
  lcd2.setCursor(0, 2);
  lcd2.print("COM3");
}
                                
void loop() {
  
    while(Serial.available()) {
   
   s = Serial.readString();

   lcd1.setCursor(0, 0);
   lcd1.print(s.substring(0, 16));
   
   lcd1.setCursor(0, 2);
   lcd1.print(s.substring(16, 32));
   
   lcd2.setCursor(0, 0);
   lcd2.print(s.substring(32, 48));
   
   lcd2.setCursor(0, 2);
   lcd2.print(s.substring(48, 64));

   if (s.substring(0, 3) == "red"){
    digitalWrite(red, HIGH);
   }

   if (s.substring(0, 6) == "redoff"){
    digitalWrite(red, LOW);
   }

      if (s.substring(0, 5) == "green"){
    digitalWrite(green, HIGH);
   }

   if (s.substring(0, 8) == "greenoff"){
    digitalWrite(green, LOW);
   }

      if (s.substring(0, 4) == "blue"){
    digitalWrite(blue, HIGH);
   }

   if (s.substring(0, 7) == "blueoff"){
    digitalWrite(blue, LOW);
   }
  
   
   delay(200);
   
   }
}
