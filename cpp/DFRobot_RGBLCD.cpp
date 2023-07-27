/*!
 * @file DFRobot_RGBLCD.cpp
 * @brief DFRobot's LCD
 * @n High Accuracy Ambient Light Sensor
 *
 * @copyright   [DFRobot](http://www.dfrobot.com), 2016
 * @copyright   GNU Lesser General Public License
 *
 * @author [yangyang](971326313@qq.com)
 * @version  V1.0
 * @date  2017-2-10
 */

 //#include <Arduino.h>
 //#include <stdio.h>
 //#include <string.h>
 //#include <inttypes.h>
 //#include <Wire.h>
#include "DFRobot_RGBLCD.h"
#include <string.h>
const uint8_t color_define[4][3] =
{
  {255, 255, 255},            // white
  {255, 0, 0},                // red
  {0, 255, 0},                // green
  {0, 0, 255},                // blue
};

/*******************************public*******************************/
DFRobot_RGBLCD::DFRobot_RGBLCD(uint8_t lcd_cols, uint8_t lcd_rows, uint8_t lcd_Addr, uint8_t RGB_Addr)
{
  _lcdAddr = lcd_Addr;
  _RGBAddr = RGB_Addr;
  _cols = lcd_cols;
  _rows = lcd_rows;
}

void DFRobot_RGBLCD::init()
{
  //	Wire.begin();
  wiringPiSetup();
  fdLCD = wiringPiI2CSetup(_lcdAddr);
  fdRGB = wiringPiI2CSetup(_RGBAddr);
  // if (fdRGB == -1) {
  if (wiringPiI2CRead(fdRGB) == -1) {
    _RGBAddr = 0xc0 >> 1;
    fdRGB = wiringPiI2CSetup(_RGBAddr);
  }
  _showfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
  begin(_cols, _rows);
}

void DFRobot_RGBLCD::clear()
{
  command(LCD_CLEARDISPLAY);        // clear display, set cursor position to zero
  delayMicroseconds(2000);          // this command takes a long time!
}

void DFRobot_RGBLCD::home()
{
  command(LCD_RETURNHOME);        // set cursor position to zero
  delayMicroseconds(2000);        // this command takes a long time!
}

void DFRobot_RGBLCD::noDisplay()
{
  _showcontrol &= ~LCD_DISPLAYON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}

void DFRobot_RGBLCD::display()
{
  _showcontrol |= LCD_DISPLAYON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}

void DFRobot_RGBLCD::stopBlink()
{
  _showcontrol &= ~LCD_BLINKON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}
void DFRobot_RGBLCD::blink()
{
  _showcontrol |= LCD_BLINKON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}

void DFRobot_RGBLCD::noCursor()
{
  _showcontrol &= ~LCD_CURSORON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}

void DFRobot_RGBLCD::cursor()
{
  _showcontrol |= LCD_CURSORON;
  command(LCD_DISPLAYCONTROL | _showcontrol);
}

void DFRobot_RGBLCD::scrollDisplayLeft(void)
{
  command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT);
}

void DFRobot_RGBLCD::scrollDisplayRight(void)
{
  command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT);
}

void DFRobot_RGBLCD::leftToRight(void)
{
  _showmode |= LCD_ENTRYLEFT;
  command(LCD_ENTRYMODESET | _showmode);
}

void DFRobot_RGBLCD::rightToLeft(void)
{
  _showmode &= ~LCD_ENTRYLEFT;
  command(LCD_ENTRYMODESET | _showmode);
}

void DFRobot_RGBLCD::noAutoScroll(void)
{
  _showmode &= ~LCD_ENTRYSHIFTINCREMENT;
  command(LCD_ENTRYMODESET | _showmode);
}

void DFRobot_RGBLCD::autoScroll(void)
{
  _showmode |= LCD_ENTRYSHIFTINCREMENT;
  command(LCD_ENTRYMODESET | _showmode);
}

void DFRobot_RGBLCD::customSymbol(uint8_t location, uint8_t charmap[])
{
  location &= 0x7; // we only have 8 locations 0-7
  command(LCD_SETCGRAMADDR | (location << 3));

  for (int i = 0; i < 8; i++) {
    wiringPiI2CWriteReg8(fdLCD, 0x40, charmap[i]);
  }
}

void DFRobot_RGBLCD::setCursor(uint8_t col, uint8_t row)
{
  col = (row == 0 ? col | 0x80 : col | 0xc0);
  wiringPiI2CWriteReg8(fdLCD, 0x80, col);
}

void DFRobot_RGBLCD::setRGB(uint8_t r, uint8_t g, uint8_t b)
{
  setReg(REG_RED, r);
  setReg(REG_GREEN, g);
  setReg(REG_BLUE, b);
}

void DFRobot_RGBLCD::setColor(uint8_t color)
{
  if (color > 3)return;
  setRGB(color_define[color][0], color_define[color][1], color_define[color][2]);
}

void DFRobot_RGBLCD::blinkLED(void)
{
  ///< blink period in seconds = (<reg 7> + 1) / 24
  ///< on/off ratio = <reg 6> / 256
  setReg(0x07, 0x17);  // blink every second
  setReg(0x06, 0x7f);  // half on, half off
}

void DFRobot_RGBLCD::noBlinkLED(void)
{
  setReg(0x07, 0x00);
  setReg(0x06, 0xff);
}

//inline 
size_t DFRobot_RGBLCD::write(uint8_t value)
{
  uint8_t data[3] = { 0x40, value };
  wiringPiI2CWriteReg8(fdLCD, 0x40, value);
  delay(5);
  return 1; // assume sucess
}

inline void DFRobot_RGBLCD::command(uint8_t value)
{
  uint8_t data[3] = { 0x80, value };
  wiringPiI2CWriteReg8(fdLCD, 0x80, value);
  delay(5);
}

void DFRobot_RGBLCD::blink_on()
{
  blink();
}

void DFRobot_RGBLCD::blink_off()
{
  stopBlink();
}

void DFRobot_RGBLCD::cursor_on()
{
  cursor();
}

void DFRobot_RGBLCD::cursor_off()
{
  noCursor();
}

void DFRobot_RGBLCD::setBacklight(uint8_t new_val)
{
  if (new_val) {
    blinkLED();     // turn backlight on
  } else {
    noBlinkLED();       // turn backlight off
  }
}

void DFRobot_RGBLCD::load_custom_character(uint8_t char_num, uint8_t* rows)
{
  customSymbol(char_num, rows);
}

void DFRobot_RGBLCD::print(uint16_t dat)
{
  uint8_t i = 0;
  char buff[16];
  sprintf(buff, "%d", dat);
  while (buff[i] != '\0')
    write(buff[i++]);
}

void DFRobot_RGBLCD::print(const char c[])
{
  ///< This function is not identical to the function used for "real" I2C displays
  ///< it's here so the user sketch doesn't have to be changed 
  int i = 0;
  while (c[i] != '\0') {
    write(c[i]);
    i++;
  }
}

/*******************************private*******************************/
void DFRobot_RGBLCD::begin(uint8_t cols, uint8_t lines, uint8_t dotsize)
{
  if (lines > 1) {
    _showfunction |= LCD_2LINE;
  }
  _numlines = lines;
  _currline = 0;

  ///< for some 1 line displays you can select a 10 pixel high font
  if ((dotsize != 0) && (lines == 1)) {
    _showfunction |= LCD_5x10DOTS;
  }

  ///< SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
  ///< according to datasheet, we need at least 40ms after power rises above 2.7V
  ///< before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
  delay(50);


  ///< this is according to the hitachi HD44780 datasheet
  ///< page 45 figure 23

  ///< Send function set command sequence
  command(LCD_FUNCTIONSET | _showfunction);
  delay(5);  // wait more than 4.1ms

  ///< second try
  command(LCD_FUNCTIONSET | _showfunction);
  delay(5);

  ///< third go
  command(LCD_FUNCTIONSET | _showfunction);

  ///< turn the display on with no cursor or blinking default
  _showcontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF;
  display();

  ///< clear it off
  clear();
  ///< Initialize to default text direction (for romance languages)
  _showmode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT;
  ///< set the entry mode
  command(LCD_ENTRYMODESET | _showmode);


  ///< backlight init
  setReg(REG_MODE1, 0);
  ///< set LEDs controllable by both PWM and GRPPWM registers
  setReg(REG_OUTPUT, 0xFF);
  ///< set MODE2 values
  ///< 0010 0000 -> 0x20  (DMBLNK to 1, ie blinky mode)
  setReg(REG_MODE2, 0x20);

  setColorWhite();
}

void DFRobot_RGBLCD::setReg(uint8_t addr, uint8_t data)
{
  //    Wire.beginTransmission(_RGBAddr); // transmit to device #4
  //    Wire.write(addr);
  //    Wire.write(data);
  //    Wire.endTransmission();    // stop transmitting
  wiringPiI2CWriteReg8(fdRGB, addr, data);
}

/************************unsupported API functions***************************/
void DFRobot_RGBLCD::off() {}
void DFRobot_RGBLCD::on() {}
void DFRobot_RGBLCD::setDelay(int cmdDelay, int charDelay) {}
uint8_t DFRobot_RGBLCD::status() { return 0; }
uint8_t DFRobot_RGBLCD::keypad() { return 0; }
uint8_t DFRobot_RGBLCD::init_bargraph(uint8_t graphtype) { return 0; }
void DFRobot_RGBLCD::draw_horizontal_graph(uint8_t row, uint8_t column, uint8_t len, uint8_t pixel_col_end) {}
void DFRobot_RGBLCD::draw_vertical_graph(uint8_t row, uint8_t column, uint8_t len, uint8_t pixel_row_end) {}
void DFRobot_RGBLCD::setContrast(uint8_t new_val) {}

