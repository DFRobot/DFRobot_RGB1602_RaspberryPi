#include "../DFRobot_RGBLCD.h"
#include <iostream>
#include <string>
#include <string.h>
using namespace std; 

int main(){
  int fd;
  char line1[16];
  char line2[16];
  string str;
  DFRobot_RGBLCD lcd(16, 2);
  lcd.init();
  
  while(1){
    if(getline(cin,str)){
      lcd.clear();
      lcd.setCursor(0,0);
      strncpy(line1, str.c_str(), 16);
      lcd.print(line1);
      if (str.size() > 16) {
        lcd.setCursor(0,1);
        strncpy(line2,str.c_str()+16,16);
        lcd.print(line2);
      }
    }
  }
  return 0;
}
