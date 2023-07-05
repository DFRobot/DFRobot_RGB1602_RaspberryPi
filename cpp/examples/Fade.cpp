#include "../DFRobot_RGBLCD.h"

DFRobot_RGBLCD lcd(16, 2);

void breath(unsigned char color){
  for(int i=0; i<255; i++){
    lcd.setPWM(color, i);
    delay(5);
  }
  delay(500);
  
  for(int i=254; i>=0; i--){
    lcd.setPWM(color, i);
    delay(5);
  }
  delay(500);
}

int main(){
  lcd.init();
  lcd.print("fade demo");
  lcd.setColorAll();

  while (1) {
    breath(REG_RED);
    breath(REG_GREEN);
    breath(REG_BLUE);
  }
  return 0;
}
