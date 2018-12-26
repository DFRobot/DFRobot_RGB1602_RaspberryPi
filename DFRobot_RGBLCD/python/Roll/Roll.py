import sys
sys.path.append('../')
import rgb1602
import time

lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row

# Print a message to the LCD.
lcd.printout("hello, world!")
time.sleep(1)


while True:
  # scroll 13 positions (string length) to the left
  # to move it offscreen left:
  for positionCounter in range (0,13):
    # scroll one position left:
    lcd.scrollDisplayLeft()
    # wait a bit:
    time.sleep(0.15)

  # scroll 29 positions (string length + show length) to the right
  # to move it offscreen right:
  for positionCounter in range (0,29):
    # scroll one position right:
    lcd.scrollDisplayRight()
    # wait a bit:
    time.sleep(0.15)

  # scroll 16 positions (show length + string length) to the left
  # to move it back to center:
  for positionCounter in range(0,16):
    # scroll one position left:
    lcd.scrollDisplayLeft()
    # wait a bit:
    time.sleep(0.15)
    

    # delay at the end of the full loop:
  time.sleep(1)


