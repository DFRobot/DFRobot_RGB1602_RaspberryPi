import sys
sys.path.append('../')
import rgb1602
import time

lcd = rgb1602.RGB1602(16,2)

lcd.printout("hello world!");
time.sleep(1)
while True:
  lcd.stopBlink()
  time.sleep(3)
  lcd.blink()
  time.sleep(3)
