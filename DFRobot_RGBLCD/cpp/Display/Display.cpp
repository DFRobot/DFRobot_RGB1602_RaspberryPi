#include "../DFRobot_RGBLCD.h"

int main(){
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();

  lcd.print("Hello World!");
  
  while(1){
    // Turn off the display:
    lcd.noDisplay();
    delay(500);
    // Turn on the display:
    lcd.display();
    delay(500);
  }
  return 0;
}
