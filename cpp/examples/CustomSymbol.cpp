#include "../DFRobot_RGBLCD.h"

// make some custom characters:
uint8_t heart[8] = {
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000
};

uint8_t smiley[8] = {
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b10001,
    0b01110,
    0b00000
};

uint8_t frownie[8] = {
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b10001
};

uint8_t armsDown[8] = {
    0b00100,
    0b01010,
    0b00100,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010
};

uint8_t armsUp[8] = {
    0b00100,
    0b01010,
    0b00100,
    0b10101,
    0b01110,
    0b00100,
    0b00100,
    0b01010
};

int main(){
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();
 #if 1   
  // create a new character
  lcd.customSymbol(0, heart);
  // create a new character
  lcd.customSymbol(1, smiley);
  // create a new character
  lcd.customSymbol(2, frownie);
  // create a new character
  lcd.customSymbol(3, armsDown);
  // create a new character
  lcd.customSymbol(4, armsUp);
#endif 
  // set up the lcd's number of columns and rows:
    
    
  lcd.setCursor(0, 0);
  // Print a message to the lcd.
  lcd.print("I ");
  lcd.write((unsigned char)0);
  lcd.print(" raspberry! ");
  lcd.write(1);
  
  while(1){
    // set the cursor to the bottom row, 5th position:
    lcd.setCursor(4, 1);
    // draw the little man, arms down:
    lcd.write(3);
    delay(500);
    lcd.setCursor(4, 1);
    // draw him arms up:
    lcd.write(4);
    delay(500);
  }
  return 0;
}













