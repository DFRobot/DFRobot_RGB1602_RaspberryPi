import sys
sys.path.append('../')
import rgb1602
import time

colorR = 255
colorG = 0
colorB = 0

lcd=rgb1602.RGB1602(16,2)

lcd.setRGB(colorR, colorG, colorB)
    
# Print a message to the LCD.
lcd.printout("hello, world!")

time.sleep(1)
i = 0

while True:
  i = i+1
  # set the cursor to column 0, line 1
  # (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1)
  # print the number of seconds since reset:
  lcd.printout(i)
  time.sleep(1)

