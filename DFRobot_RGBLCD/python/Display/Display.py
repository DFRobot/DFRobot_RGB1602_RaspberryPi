import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

lcd.printout("hello world!")
while True:
  lcd.noDisplay()
  time.sleep(0.5)
  lcd.display()
  time.sleep(0.5)

