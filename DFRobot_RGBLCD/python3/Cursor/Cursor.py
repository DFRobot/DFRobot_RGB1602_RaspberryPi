import sys
sys.path.append('../')
import time
import rgb1602

lcd = rgb1602.RGB1602(16,2)

lcd.print("hello, world!")

while True:
  # Turn off the cursor:
  lcd.noCursor();
  time.sleep(0.5);
  # Turn on the cursor:
  lcd.cursor();
  time.sleep(0.5);
