#include "../DFRobot_RGBLCD.h"
#include "stdio.h"

int main(){

  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();

  lcd.print("Hello World!");
  delay(1000);
  
  while(1){
    printf("hello\r\n");
    //Turn off the blinking cursor:
    lcd.stopBlink();
    delay(3000);
    //Turn on the blinking cursor:
    lcd.blink();
    // printf("===");
    // delay(3000);
    delay(3000);
  }
  return 0;
}
