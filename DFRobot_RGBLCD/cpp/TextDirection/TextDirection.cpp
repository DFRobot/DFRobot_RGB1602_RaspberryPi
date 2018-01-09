#include "../DFRobot_RGBLCD.h"

using namespace std;

int main(){
  int thisChar = 'a';
  DFRobot_RGBLCD lcd(16, 2);
  // initialize
  lcd.init();
  // turn on the cursor:
  lcd.cursor();
  
  while(1){
    // reverse directions at 'm':
    if (thisChar == 'm') {
      // go right for the next letter
      lcd.rightToLeft();
    }
    // reverse again at 's':
    if (thisChar == 's') {
      // go left for the next letter
      lcd.leftToRight();
    }
    // reset at 'z':
    if (thisChar > 'z') {
      // go to (0,0):
      lcd.home();
      // start again at 0
      thisChar = 'a';
    }
    // print the character
    lcd.write(thisChar);
    // wait a second:
    delay(1000);
    // increment the letter:
    thisChar++;
  }
  return 0;
}

