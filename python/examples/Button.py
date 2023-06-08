import sys
sys.path.append('../')
import rgb1602
import time

if rgb1602.THIS_BOARD_TYPE:
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(16, GPIO.IN)
  GPIO.setup(17, GPIO.IN)
  GPIO.setup(18, GPIO.IN)
  GPIO.setup(19, GPIO.IN)
  GPIO.setup(20, GPIO.IN)

else:
  import mraa
  pin_SELECT = mraa.Gpio(36)
  pin_SELECT.dir(mraa.DIR_IN)
  pin_UP = mraa.Gpio(11)
  pin_UP.dir(mraa.DIR_IN)
  pin_DOWN = mraa.Gpio(12)
  pin_DOWN.dir(mraa.DIR_IN)
  pin_LEFT = mraa.Gpio(35)
  pin_LEFT.dir(mraa.DIR_IN)
  pin_RIGHT = mraa.Gpio(38)
  pin_RIGHT.dir(mraa.DIR_IN)

lcd = rgb1602.RGB1602(16,2)

# Define keys
lcd_key     = 0
key_in  = 0

btnRIGHT  = 0
btnUP     = 1
btnDOWN   = 2
btnLEFT   = 3
btnSELECT = 4


#Read the key value
def read_LCD_buttons():
  if rgb1602.THIS_BOARD_TYPE:
    key_in16 = GPIO.input(16)
    key_in17 = GPIO.input(17)
    key_in18 = GPIO.input(18)
    key_in19 = GPIO.input(19)
    key_in20 = GPIO.input(20)
  else:
    key_in16 = pin_SELECT.read()
    key_in17 = pin_UP.read()
    key_in18 = pin_DOWN.read()
    key_in19 = pin_LEFT.read()
    key_in20 = pin_RIGHT.read()

  if (key_in16 == 1):
    return btnSELECT
  if (key_in17 == 1):
    return btnUP
  if (key_in18 == 1):
    return btnDOWN
  if (key_in19 == 1):
    return btnLEFT
  if (key_in20 == 1):
    return btnRIGHT

lcd.setCursor(0,0)
lcd.printout("Push the buttons")
while True:
  lcd.setCursor(0,1)
  lcd_key = read_LCD_buttons()  #  Reading keys
  time.sleep(0.2)
  lcd_key = read_LCD_buttons()

  if (lcd_key == btnRIGHT):
    lcd.printout("RIGHT ")
  elif (lcd_key == btnLEFT):
    lcd.printout("LEFT  ")
  elif (lcd_key == btnUP):
    lcd.printout("UP    ")
  elif (lcd_key == btnDOWN):
    lcd.printout("DOWN  ")
  elif (lcd_key == btnSELECT):
    lcd.printout("SELECT")
