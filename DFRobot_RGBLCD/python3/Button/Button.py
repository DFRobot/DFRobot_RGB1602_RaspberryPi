import sys
sys.path.append('../')
import RPi.GPIO as GPIO
import rgb1602
import time

lcd = rgb1602.RGB1602(16,2)
GPIO.setmode(GPIO.BCM)
# Define keys
lcd_key     = 0
key_in  = 0

btnRIGHT  = 0
btnUP     = 1
btnDOWN   = 2
btnLEFT   = 3
btnSELECT = 4

GPIO.setup(16, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(20, GPIO.IN)


#Read the key value
def read_LCD_buttons():
  key_in16 = GPIO.input(16)
  key_in17 = GPIO.input(17)
  key_in18 = GPIO.input(18)
  key_in19 = GPIO.input(19)
  key_in20 = GPIO.input(20)
 
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
lcd.print("Push the buttons"); #print“Push the buttons”

while True:
  lcd.setCursor(0,1)
  lcd_key = read_LCD_buttons()  #  Reading keys

  if (lcd_key == btnRIGHT):
    lcd.print("RIGHT ")
  elif (lcd_key == btnLEFT):
    lcd.print("LEFT  ")
  elif (lcd_key == btnUP):
    lcd.print("UP    ")
  elif (lcd_key == btnDOWN):
    lcd.print("DOWN  ")
  elif (lcd_key == btnSELECT):
    lcd.print("SELECT")
