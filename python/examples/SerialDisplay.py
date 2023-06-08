import sys
sys.path.append('../')
import rgb1602
import time
import six

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

while True:
  data = None
  if six.PY2:
    data = raw_input()
  else:
    data = input()
  lcd.clear()
  lcd.setCursor(0,0)
  lcd.printout(data)
  if len(data) >16:
    lcd.setCursor(0,1)
    lcd.printout(data[16:])
