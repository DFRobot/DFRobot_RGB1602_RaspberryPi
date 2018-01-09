#include "../DFRobot_RGBLCD.h"

#define btnRIGHT   5
#define btnUP      1
#define btnDOWN    2
#define btnLEFT    3
#define btnSELECT  4

int read_LCD_buttons(){
  int key_in16 = digitalRead(27);
  int key_in17 = digitalRead(0);
  int key_in18 = digitalRead(1);
  int key_in19 = digitalRead(24);
  int key_in20 = digitalRead(28);
 
  if (key_in20 == 1)
    return btnRIGHT;
  if (key_in16 == 1)
    return btnSELECT;
  if (key_in17 == 1)
    return btnUP;
  if (key_in18 == 1)
    return btnDOWN;
  if (key_in19 == 1)
    return btnLEFT;
}

int main(){
  wiringPiSetup();
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();
  pinMode(27,INPUT);
  pinMode(0,INPUT);
  pinMode(1,INPUT);
  pinMode(24,INPUT);
  pinMode(28,INPUT);
  lcd.setCursor(0,0);
  lcd.print("Push the buttons");
  
  while(1){
    // Turn off the blinking cursor:
    lcd.setCursor(0,1);
    int lcd_key = read_LCD_buttons();

    
    if (lcd_key == btnLEFT)
      lcd.print("LEFT  ");
    else if (lcd_key == btnUP)
      lcd.print("UP    ");
    else if (lcd_key == btnDOWN)
      lcd.print("DOWN  ");
    else if (lcd_key == btnSELECT)
      lcd.print("SELECT");
    else if (lcd_key == btnRIGHT)
      lcd.print("RIGHT ");
  }
  return 0;
}
