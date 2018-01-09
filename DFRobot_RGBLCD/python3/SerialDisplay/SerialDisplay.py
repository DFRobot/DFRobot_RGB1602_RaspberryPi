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
    lcd.print(data)
  elif length >16:
    lcd.print(data[:16])
    lcd.setCursor(0,1)
    lcd.print(data[16:])