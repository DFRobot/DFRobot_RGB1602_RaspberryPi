#include "../DFRobot_RGBLCD.h"

int main(){
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();
  
  while(1){
    // set the cursor to (0,0):
    lcd.setCursor(0, 0);
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++){
      lcd.print(thisChar);
      delay(500);
    }

    // set the cursor to (16,1):
    lcd.setCursor(16,1);
    // set the show to automatically scroll:
    lcd.autoScroll();
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++){
      lcd.print(thisChar);
      delay(500);
    }
    // turn off automatic scrolling
    lcd.noAutoScroll();

    // clear screen for the next loop:
    lcd.clear();
  }
  return 0;
}
