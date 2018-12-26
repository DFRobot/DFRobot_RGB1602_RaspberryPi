# -*- coding: utf-8 -*-
import time
import sys
import wiringpi

LCD_ADDRESS   =  (0x7c>>1)
RGB_ADDRESS   =  (0xc0>>1)

#color define
WHITE      =     0
RED        =     1
GREEN      =     2
BLUE       =     3
REG_RED    =     0x04
REG_GREEN  =     0x03
REG_BLUE   =     0x02
REG_MODE1  =     0x00
REG_MODE2  =     0x01
REG_OUTPUT =     0x08
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

#flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

#flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

#flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

#flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

#class LCD:
#  def __init__(self, row, col):
#    self._row = row
#    self._col = col
#    print("LCD _row=%d _col=%d"%(self._row,self._col))
#
#  def printout(self,arg):
#    if(isinstance(arg,int)):
#      arg=str(arg)
#
#    for x in bytearray(arg,'utf-8'):
#      self.write(x)

class RGB1602:
  def __init__(self, col, row):
    #self.i2c=i2c
    self._row = row
    self._col = col
    print("LCD _row=%d _col=%d"%(self._row,self._col))
    self.LCD = wiringpi.wiringPiI2CSetup(LCD_ADDRESS)
    self.RGB = wiringpi.wiringPiI2CSetup(RGB_ADDRESS)
    self._showfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
    self.begin(self._row,self._col)
#    for cmd in(
#    LCD_FUNCTIONSET | LCD_2LINE,
#    LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF,
#    LCD_CLEARDISPLAY,
#    LCD_ENTRYMODESET | LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
#    ):

#      self.command(cmd)
#      time.sleep(0.1)
#    self.setReg(REG_MODE1, 0)
#    self.setReg(REG_OUTPUT, 0xFF)
#    self.setReg(REG_MODE2, 0x20)
        
  def command(self,cmd):
    b=bytearray(2)
    b[0]=0x80
    b[1]=cmd
    wiringpi.wiringPiI2CWriteReg8(self.LCD,0x80,cmd)

  def write(self,data):
    b=bytearray(2)
    b[0]=0x40
    b[1]=data
    wiringpi.wiringPiI2CWriteReg8(self.LCD,0x40,data)
    
  def setReg(self,reg,data):
    b=bytearray(1)
    b[0]=data
    wiringpi.wiringPiI2CWriteReg8(self.RGB,reg,data)

#  def send(self,addr,len,data):
#    for i in range(0,len):
#      wiringpi.write(LCD_ADDRESS,data)
#      self.i2c.write_i2c_block_data(LCD_ADDRESS,addr,data)
#      time.sleep(0.005)

  def setRGB(self,r,g,b):
    self.setReg(REG_RED,r)
    self.setReg(REG_GREEN,g)
    self.setReg(REG_BLUE,b)

  def setCursor(self,col,row):
    if(row == 0):
      col|=0x80
    else:
      col|=0xc0;
    self.command(col)

  def clear(self):
    self.command(LCD_CLEARDISPLAY)
    time.sleep(0.002)

  def scrollDisplayLeft(self):
    self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)

  def scrollDisplayRight(self):
    self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

  def printout(self,arg):
    if(isinstance(arg,int)):
      arg=str(arg)

    for x in bytearray(arg,'utf-8'):
      self.write(x)

  def home(self):
    self.command(LCD_RETURNHOME)        # set cursor position to zero
    time.sleep(1)        # this command takes a long time!

  def noDisplay(self):
    self._showcontrol &= ~LCD_DISPLAYON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def display(self):
    self._showcontrol |= LCD_DISPLAYON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def stopBlink(self):
    self._showcontrol &= ~LCD_BLINKON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def blink(self):
    self._showcontrol |= LCD_BLINKON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def noCursor(self):
    self._showcontrol &= ~LCD_CURSORON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def cursor(self):
    self._showcontrol |= LCD_CURSORON 
    self.command(LCD_DISPLAYCONTROL | self._showcontrol)

  def leftToRight(self):
    self._showmode |= LCD_ENTRYLEFT 
    self.command(LCD_ENTRYMODESET | self._showmode)

  def rightToLeft(self):
    self._showmode &= ~LCD_ENTRYLEFT 
    self.command(LCD_ENTRYMODESET | self._showmode)

  def noAutoscroll(self):
    self._showmode &= ~LCD_ENTRYSHIFTINCREMENT 
    self.command(LCD_ENTRYMODESET | self._showmode)

  def autoscroll(self):
    self._showmode |= LCD_ENTRYSHIFTINCREMENT 
    self.command(LCD_ENTRYMODESET | self._showmode)

  def customSymbol(self,location, charmap):
    location &= 0x7  # we only have 8 locations 0-7
    self.command(LCD_SETCGRAMADDR | (location << 3))
    #data = bytearray(9);
    data = 0x40 
    #for i in range(0,8):
    #  data[i+1] = charmap[i]
    #self.send(data,9,charmap)
    
    for i in range(0,8):
      wiringpi.wiringPiI2CWriteReg8(self.LCD,0x40,charmap[i])


  def blinkLED(self):
    # blink period in seconds = (<reg 7> + 1) / 24
    # on/off ratio = <reg 6> / 256
    self.setReg(0x07, 0x17)  # blink every second
    self.setReg(0x06, 0x7f)  # half on, half off

  def noBlinkLED(self):
    self.setReg(0x07, 0x00)
    self.setReg(0x06, 0xff)

  def blink_on(self):
    self.blink()

  def blink_off(self):
    self.stopBlink()

  def cursor_on(self):
    self.cursor()

  def cursor_off(self):
    self.noCursor()

  def setBacklight(self,new_val):
    if(new_val):
      self.blinkLED()      # turn backlight on
    else:
      self.noBlinkLED()        # turn backlight off

  def load_custom_character(self,char_num,rows):
    self.customSymbol(char_num, rows)

  def printstr(self,c):
    #/< This function is not identical to the function used for "real" I2C displays
    #/< it's here so the user sketch doesn't have to be changed 
    self.printout(c)
 

#*******************************private*******************************#
  def begin(self,cols,lines,dotsize=LCD_5x8DOTS):
    if (lines > 1):
        self._showfunction |= LCD_2LINE 
     
    self._numlines = lines 
    self._currline = 0 

    # for some 1 line displays you can select a 10 pixel high font
    if ((dotsize != 0) and (lines == 1)) :
        self._showfunction |= LCD_5x10DOTS 
     
    # SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
    # according to datasheet, we need at least 40ms after power rises above 2.7V
    # before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
    #delayMicroseconds(50000);
    time.sleep(0.05)

    # this is according to the hitachi HD44780 datasheet
    # page 45 figure 23

    # Send function set command sequence
    self.command(LCD_FUNCTIONSET | self._showfunction);
    #delayMicroseconds(4500);  # wait more than 4.1ms
    time.sleep(0.005)
    # second try
    self.command(LCD_FUNCTIONSET | self._showfunction);
    #delayMicroseconds(150);
    time.sleep(0.005)
    # third go
    self.command(LCD_FUNCTIONSET | self._showfunction)
    # finally, set # lines, font size, etc.
    self.command(LCD_FUNCTIONSET | self._showfunction)
    # turn the display on with no cursor or blinking default
    self._showcontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF 
    self.display()
    # clear it off
    self.clear()
    # Initialize to default text direction (for romance languages)
    self._showmode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT 
    # set the entry mode
    self.command(LCD_ENTRYMODESET | self._showmode);
    # backlight init
    self.setReg(REG_MODE1, 0)
    # set LEDs controllable by both PWM and GRPPWM registers
    self.setReg(REG_OUTPUT, 0xFF)
    # set MODE2 values
    # 0010 0000 -> 0x20  (DMBLNK to 1, ie blinky mode)
    self.setReg(REG_MODE2, 0x20)
    self.setColorWhite()

  def setColorWhite(self):
    self.setRGB(255, 255, 255)
    
  def setPWM(self,color,pwm):
    self.setReg(color, pwm)
    
  def setColorAll(self):
    self.setRGB(0, 0, 0)
