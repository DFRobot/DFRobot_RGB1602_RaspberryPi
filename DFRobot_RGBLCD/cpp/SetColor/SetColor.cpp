#include "../DFRobot_RGBLCD.h"
#include <iostream>
#include <string>

using namespace std;

int main(){
  int r,g,b;

  DFRobot_RGBLCD lcd(16, 2);
  // initialize
  lcd.init();
  // Print a message to the LCD.
  lcd.print("set cllor");
  
  while(1){
    cout << "r:";
    cin >> r;
    cout << "g:";
    cin >> g;
    cout << "b:";
    cin >> b; 
          
    lcd.setRGB(r, g, b);
  
    cout << "r = " << r 
         << "g = " << g
         << "b = " << b
         << endl;
  }
  return 0;
}
