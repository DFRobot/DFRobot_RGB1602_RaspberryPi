import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

while True:
  data = input()
  lcd.clear()
  lcd.setCursor(0,0)
  length = len(data)
  if length < 17:
    lcd.printout(data)
  elif length >16:
    lcd.printout(data[:16])
    lcd.setCursor(0,1)
    lcd.printout(data[16:])