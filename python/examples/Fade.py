import sys
sys.path.append('../')
import rgb1602
import time

#define REG_RED         0x04        // pwm2
#define REG_GREEN       0x03        // pwm1
#define REG_BLUE        0x02        // pwm0

def breath(color):
  for i in range(0,255,1):
    lcd.setPWM(color, i)
    time.sleep(0.005)
    
  time.sleep(0.5)
  for i in range(254,0,-1):
    lcd.setPWM(color, i)
    time.sleep(0.005)

  time.sleep(0.5)


lcd=rgb1602.RGB1602(16,2)                               #create LCD object,specify col and row
lcd.printout("fade demo")
lcd.setColorAll()


while True:
  breath(0x04)
  breath(0x03)
  breath(0x02)
