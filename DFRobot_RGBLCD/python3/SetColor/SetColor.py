import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

# Print a message to the LCD.
lcd.print("set color")
print("set color")
while True:
  print("r:",end = '')
  r = int(input())
  print("g:",end = '')
  g = int(input())
  print("b:",end = '')
  b = int(input())    
        
  lcd.setRGB(r, g, b)

  print("get data:r = %s,g = %s,b = %s" %(r,g,b))


