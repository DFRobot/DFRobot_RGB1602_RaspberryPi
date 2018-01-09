#include "../DFRobot_RGBLCD.h"
#include <iostream>
#include <string>

using namespace std;

int main(){
  const int numRows = 2;
  const int numCols = 16;

  DFRobot_RGBLCD lcd(16, 2);
  // initialize
  lcd.init();
  
  while(1){
    // loop from ASCII 'a' to ASCII 'z':
    for (int thisLetter = 'a'; thisLetter <= 'z'; thisLetter++){
      // loop over the columns:
      for (int thisCol = 0; thisCol < numRows; thisCol++){
        // loop over the rows:
        for (int thisRow = 0; thisRow < numCols; thisRow++){
          // set the cursor position:
          lcd.setCursor(thisRow,thisCol);
          // print the letter:
          lcd.write(thisLetter);
          delay(200);
        }
      }
    }
  }
  return 0;
}

