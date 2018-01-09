import sys
sys.path.append('../')
import rgb1602
import time

def _map(x,inMin,inMax,outMin,outMax):
  return (x-inMin)*(outMax-outMin)/(inMax-inMin)+outMin


# make some custom characters:
heart = [
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000
]

smiley = [
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b10001,
  0b01110,
  0b00000
]

frownie = [
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b00000,
  0b01110,
  0b10001
]

armsDown = [
  0b00100,
  0b01010,
  0b00100,
  0b00100,
  0b01110,
  0b10101,
  0b00100,
  0b01010
]

armsUp = [
  0b00100,
  0b01010,
  0b00100,
  0b10101,
  0b01110,
  0b00100,
  0b00100,
  0b01010
]

lcd = rgb1602.RGB1602(16,2)  #16 characters and 2 lines of show
# create a new character
lcd.customSymbol(0, heart)
# create a new character
lcd.customSymbol(1, smiley)
# create a new character
lcd.customSymbol(2, frownie)
# create a new character
lcd.customSymbol(3, armsDown)
# create a new character
lcd.customSymbol(4, armsUp)
#set up the lcd's number of columns and rows:

lcd.setCursor(0, 0)
# Print a message to the lcd.
lcd.print("I ")
lcd.write(0)
lcd.print(" raspberry ")
lcd.write(1)
while True:
  lcd.setCursor(4, 1)
  lcd.write(3)
  time.sleep(0.5)
  lcd.setCursor(4, 1)
  lcd.write(4)
  time.sleep(0.5)
