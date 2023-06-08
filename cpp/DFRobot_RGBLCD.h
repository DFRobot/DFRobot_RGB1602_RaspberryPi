/*!
 * @file DFRobot_RGBLCD.h
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

#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>
//typedef unsigned int  uint16_t;
typedef unsigned char uint8_t;


#ifndef __DFRobot_RGBLCD_H__
#define __DFRobot_RGBLCD_H__

//#include <inttypes.h>
//#include "Print.h"

/*!
 *  @brief Device I2C Arress
 */
#define LCD_ADDRESS     (0x7c>>1)
#define RGB_ADDRESS     (0xc0>>1)


/*!
 *  @brief color define
 */ 
#define WHITE           0
#define RED             1
#define GREEN           2
#define BLUE            3

#define REG_RED         0x04        // pwm2
#define REG_GREEN       0x03        // pwm1
#define REG_BLUE        0x02        // pwm0

#define REG_MODE1       0x00
#define REG_MODE2       0x01
#define REG_OUTPUT      0x08

/*!
 *  @brief commands
 */
#define LCD_CLEARDISPLAY 0x01
#define LCD_RETURNHOME 0x02
#define LCD_ENTRYMODESET 0x04
#define LCD_DISPLAYCONTROL 0x08
#define LCD_CURSORSHIFT 0x10
#define LCD_FUNCTIONSET 0x20
#define LCD_SETCGRAMADDR 0x40
#define LCD_SETDDRAMADDR 0x80

/*!
 *  @brief flags for display entry mode
 */
#define LCD_ENTRYRIGHT 0x00
#define LCD_ENTRYLEFT 0x02
#define LCD_ENTRYSHIFTINCREMENT 0x01
#define LCD_ENTRYSHIFTDECREMENT 0x00

/*!
 *  @brief flags for display on/off control
 */
#define LCD_DISPLAYON 0x04
#define LCD_DISPLAYOFF 0x00
#define LCD_CURSORON 0x02
#define LCD_CURSOROFF 0x00
#define LCD_BLINKON 0x01
#define LCD_BLINKOFF 0x00

/*!
 *  @brief flags for display/cursor shift
 */
#define LCD_DISPLAYMOVE 0x08
#define LCD_CURSORMOVE 0x00
#define LCD_MOVERIGHT 0x04
#define LCD_MOVELEFT 0x00

/*!
 *  @brief flags for function set
 */
#define LCD_8BITMODE 0x10
#define LCD_4BITMODE 0x00
#define LCD_2LINE 0x08
#define LCD_1LINE 0x00
#define LCD_5x10DOTS 0x04
#define LCD_5x8DOTS 0x00

class DFRobot_RGBLCD  
{

public:

  /*!
   *  @brief Constructor
   */
  DFRobot_RGBLCD(uint8_t lcd_cols,uint8_t lcd_rows,uint8_t lcd_Addr=LCD_ADDRESS,uint8_t RGB_Addr=RGB_ADDRESS);
  
  /*!
   *  @brief initialize
   */ 
  void init();
  
  void clear();
  void home();

  /*!
   *  @brief Turn the display on/off (quickly)
   */
  void noDisplay();
  void display();

  /*!
   *  @brief Turn on and off the blinking showCursor
   */
  void stopBlink();
  void blink();

  /*!
   *  @brief Turns the underline showCursor on/off
   */
  void noCursor();
  void cursor();

  /*!
   *  @brief These commands scroll the display without changing the RAM
   */
  void scrollDisplayLeft();
  void scrollDisplayRight();
 
  /*!
   *  @brief This is for text that flows Left to Right
   */
  void leftToRight();
 
  /*!
   *  @brief This is for text that flows Right to Left
   */
  void rightToLeft();

  /*!
   *  @brief This will 'left justify' text from the showCursor
   */
  void noAutoScroll();
 
  /*!
   *  @brief This will 'right justify' text from the showCursor
   */
  void autoScroll();
   
  /*!
   *  @brief Allows us to fill the first 8 CGRAM locations
   *         with custom characters
   */
  void customSymbol(uint8_t, uint8_t[]);
  void setCursor(uint8_t, uint8_t);  
  
  /*!
   *  @brief color control
   */
  void setRGB(uint8_t r, uint8_t g, uint8_t b);               // set rgb
  void setPWM(uint8_t color, uint8_t pwm){setReg(color, pwm);}      // set pwm 
  void setColor(uint8_t color);
  void setColorAll(){setRGB(0, 0, 0);}
  void setColorWhite(){setRGB(255, 255, 255);}

  /*!
   *  @brief blink the LED backlight
   */
  void blinkLED(void);
  void noBlinkLED(void);

  /*!
   *  @brief send data
   */
  //virtual size_t write(uint8_t);
  //inline
   size_t  write(uint8_t value);
  /*!
   *  @brief send command
   */
  void command(uint8_t);
  
  /*!
   *  @brief compatibility API function aliases
   */
  void blink_on();                          // alias for blink()
  void blink_off();                         // alias for noBlink()
  void cursor_on();                         // alias for cursor()
  void cursor_off();                        // alias for noCursor()
  void setBacklight(uint8_t new_val);       // alias for backlight() and nobacklight()
  void load_custom_character(uint8_t char_num, uint8_t *rows);  // alias for createChar()
  void print(const char[]);
  void print(uint16_t dat);
  /*!
   *  @brief Unsupported API functions (not implemented in this library)
   */
  uint8_t status();
  void setContrast(uint8_t new_val);
  uint8_t keypad();
  void setDelay(int,int);
  void on();
  void off();
  uint8_t init_bargraph(uint8_t graphtype);
  void draw_horizontal_graph(uint8_t row, uint8_t column, uint8_t len,  uint8_t pixel_col_end);
  void draw_vertical_graph(uint8_t row, uint8_t column, uint8_t len,  uint8_t pixel_col_end);
  //  using Print::write;
  
private:
  void begin(uint8_t cols, uint8_t rows, uint8_t charsize = LCD_5x8DOTS);
  //  void send(uint8_t *data, uint8_t len);
  void setReg(uint8_t addr, uint8_t data);
  uint8_t _showfunction;
  uint8_t _showcontrol;
  uint8_t _showmode;
  uint8_t _initialized;
  uint8_t _numlines,_currline;
  uint8_t _lcdAddr;
  uint8_t _RGBAddr;
  uint8_t _cols;
  uint8_t _rows;
  uint8_t _backlightval;
  int fdLCD;
  int fdRGB;
};

#endif
