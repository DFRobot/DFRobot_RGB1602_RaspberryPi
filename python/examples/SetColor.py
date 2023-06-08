import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

# Print a message to the LCD.
lcd.printout("set color")
print("set color")
while True:  
  while True:
    r = int(input("r = "))
    if r < 256 and r >= 0:
      break 
    else:
      print("r is wrong number,input r in 0 ~255")
  while True:
    g = int(input("g = "))
    if g < 256 and g >= 0:
      break 
    else:
      print("g is wrong number,input g in 0 ~255")
  while True:
    b = int(input("b = "))
    if b <256 and b >= 0:
      break
    else:
      print("b is wrong number,input b in 0 ~255")
  lcd.setRGB(r, g, b)
  print("get data:r = %s,g = %s,b = %s" %(r,g,b))


