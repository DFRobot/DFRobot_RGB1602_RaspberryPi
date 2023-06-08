#include "../DFRobot_RGBLCD.h"

int main(){
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();

  lcd.print("Hello World!");
  delay(1000);
  
  while(1){
    // scroll 13 positions (string length) to the left
    // to move it offscreen left:
    for (int positionCounter = 0; positionCounter < 13; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayLeft();
      // wait a bit:
      delay(150);
    }

    // scroll 29 positions (string length + show length) to the right
    // to move it offscreen right:
    for (int positionCounter = 0; positionCounter < 29; positionCounter++) {
      // scroll one position right:
      lcd.scrollDisplayRight();
      // wait a bit:
      delay(150);
    }

    // scroll 16 positions (show length + string length) to the left
    // to move it back to center:
    for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayLeft();
      // wait a bit:
      delay(150);
    }
    // delay at the end of the full loop:
    delay(1000);
  }
  return 0;
}
