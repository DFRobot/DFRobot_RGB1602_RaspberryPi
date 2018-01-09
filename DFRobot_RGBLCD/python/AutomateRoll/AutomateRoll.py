import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row


while True:
  lcd.setCursor(0, 0)
  #print from 0 to 9:
  for thisChar in range(0,10):
    lcd.print(thisChar)
    time.sleep(0.5)
    

  # set the cursor to (16,1):
  lcd.setCursor(16,1)
  # set the show to automatically scroll:
  lcd.autoscroll()
  # print from 0 to 9:
  for thisChar in range (0,10):
    lcd.print(thisChar)
    time.sleep(0.5)
  # turn off automatic scrolling
  lcd.noAutoscroll()

  # clear screen for the next loop:
  lcd.clear()
