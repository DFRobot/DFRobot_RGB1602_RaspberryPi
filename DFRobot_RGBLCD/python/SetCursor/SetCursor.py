import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

numRows = 2
numCols = 16
lcd.setRGB(0,100,0)
while True:
  # loop from ASCII 'a' to ASCII 'z':
  for thisLetter in range(ord('a'),ord('z')):
    #lcd.clear()
    # loop over the columns:
    for thisRow in range(0,numRows):
      # loop over the rows:
      for thisCol in range(0,numCols):
        # set the cursor position:
        lcd.setCursor(thisCol,thisRow)
        # print the letter:
        lcd.write(thisLetter)
        time.sleep(0.2)
