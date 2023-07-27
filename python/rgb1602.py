# -*- coding: utf-8 -*-
import time
import sys
import smbus

# Select the driver library according to the type of development board
ROCK_PI_BOARD = 0
RASPBERRY_PI_BOARD = 1
THIS_BOARD_TYPE = RASPBERRY_PI_BOARD
try:
    with open('/proc/device-tree/model', 'r') as f:
        model = f.read()
        if 'ROCK PI' in model:
            THIS_BOARD_TYPE = ROCK_PI_BOARD
except:
    pass

LCD_ADDRESS   =  (0x7c>>1)
# RGB_ADDRESS   =  (0xc0>>1)   # Colour base old (0x60)
RGB_ADDRESS   =  (0x5a>>1)   # Color base new (0x2d)

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

lcd_charmap = {
    ord(u'ä'): chr(0xe1),
    ord(u'Ä'): chr(0xe1),
    ord(u'ö'): chr(0xef),
    ord(u'Ö'): chr(0xef),
    ord(u'ü'): chr(0xf5),
    ord(u'Ü'): chr(0xf5),
    ord(u'°'): chr(0xdf),
    ord(u'α'): chr(0xe0),
    ord(u'β'): chr(0xe2),
    ord(u'ε'): chr(0xe3),
    ord(u'σ'): chr(0xe5),
    ord(u'ρ'): chr(0xe6),
    ord(u'π'): chr(0xf7),
    ord(u'√'): chr(0xe8),
    ord(u'μ'): chr(0xe4),
    ord(u'¢'): chr(0xec),
    ord(u'£'): chr(0xed),
    ord(u'ñ'): chr(0xee),
    ord(u'ϴ'): chr(0xf2),
    ord(u'∞'): chr(0xf3),
    ord(u'Σ'): chr(0xf6),
    ord(u'Ω'): chr(0xf4),
    ord(u'÷'): chr(0xfd),
}


class RGB1602:
  def __init__(self, col, row):
    global RGB_ADDRESS  # 声明 RGB_ADDRESS 为全局变量
    self._row = row
    self._col = col
    # print("LCD _row=%d _col=%d"%(self._row,self._col))
    if THIS_BOARD_TYPE:
        self._bus = smbus.SMBus(1)
    else:
        self._bus = smbus.SMBus(7)
    self._showfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS

    try:
        # 通过发送一个简单的读取命令来检测设备是否存在
        self._bus.read_byte(RGB_ADDRESS)
    except IOError:
        # 如果捕获到 IOError 异常，则说明在该地址没有找到设备
        RGB_ADDRESS   =  (0xc0>>1)   # Colour base old (0x60)

    self.begin(self._row,self._col)

  def command(self,cmd):
    b=bytearray(2)
    b[0]=0x80
    b[1]=cmd
    self._bus.write_i2c_block_data(LCD_ADDRESS, 0x80, [cmd])

  def write(self,data):
    b=bytearray(2)
    b[0]=0x40
    b[1]=data
    self._bus.write_i2c_block_data(LCD_ADDRESS, 0x40, [data])
    
  def setReg(self,reg,data):
    b=bytearray(1)
    b[0]=data
    self._bus.write_i2c_block_data(RGB_ADDRESS, reg, [data])

  def setRGB(self,r,g,b):
    self.setReg(REG_RED,r)
    self.setReg(REG_GREEN,g)
    self.setReg(REG_BLUE,b)

  def setCursor(self,col,row):
    if(row == 0):
      col|=0x80
    else:
      col|=0xc0
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
    if sys.version_info.major == 2:
      # note : python2 special character display problem, python3 is recommended
      # arg = arg.decode('utf-8').translate(lcd_charmap).encode('utf-8')
      # pass
      keys = u"".join([unichr(key) for key in lcd_charmap.keys()])
      values = u"".join([lcd_charmap[key].decode('latin-1') for key in lcd_charmap.keys()])
      arg = arg.decode('utf-8').translate({ord(key): ord(value) for key, value in zip(keys, values)})
    else:
      arg = arg.translate(lcd_charmap)
    for char in arg:
      self.write(ord(char))
    # for x in bytearray(arg,'utf-8'):
    #   self.write(x)

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
    
    for i in range(0,8):
      self._bus.write_i2c_block_data(LCD_ADDRESS, 0x40, [charmap[i]])


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
