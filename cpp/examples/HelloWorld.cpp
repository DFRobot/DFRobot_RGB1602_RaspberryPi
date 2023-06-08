#include "../DFRobot_RGBLCD.h"

int main(){
  const int colorR = 255;
  const int colorG = 0;
  const int colorB = 0;
  int i = 0;
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();
  lcd.setRGB(colorR, colorG, colorB);
  lcd.print("Hello World!");
  delay(1000);
  
  while(1){
    lcd.setCursor(0, 1);
    lcd.print(i++);
    delay(1000);
  }
  return 0;
}
