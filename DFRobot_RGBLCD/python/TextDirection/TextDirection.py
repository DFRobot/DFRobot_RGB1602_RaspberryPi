import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row
thisChar = 'a'

lcd.cursor()

while True:
  # reverse directions at 'm':
  if ((thisChar) == 'm'):
    # go right for the next letter
    lcd.rightToLeft()
  
  # reverse again at 's':
  if ((thisChar) == 's'):
    # go left for the next letter
    lcd.leftToRight()
  
  # reset at 'z':
  if ((thisChar) > 'z'):
    # go to (0,0):
    lcd.home()
    # start again at 0
    thisChar = 'a'
  
  # print the character
  lcd.write(ord(thisChar))
  # wait a second:
  time.sleep(0.5)
  # increment the letter:
  thisChar = chr(ord(thisChar) +1)

