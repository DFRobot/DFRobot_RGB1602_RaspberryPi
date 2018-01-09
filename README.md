RGB1602 of RaspberryPi with C++ and Python3
---------------------------------------------------------
## Enable I2C:
    * 1. Input: sudo raspi-config in terminal
    * 2. Select: Interfacing Options
    * 3. Select: I2C; enable I2C

## C++:
### install wiringPi(Please skip this step if you have already installed the library.)
    * 1. git clone git://git.drogon.net/wiringPi
    * 2. cd wiringPi
    * 3. ./build
    
### API
#### Change Color of Backlight
One of Grove - LCD RGB Backlight's most important feature is changing the backlight color. It's very simple; just use the folowing function:

    void setRGB(int r, int g, int b);

#### Clear display

You can clear the display by this function:

    void clear();

#### Turn on and turn off display

    void noDisplay();     // turn off display
    void display();       // turn on display

#### Blink

    void stopBlink();
    void blink();

#### Cursor

    void noCursor();
    void cursor();

#### Blink LED Backlight

    void blinkLED();
    void noBlinkLED();

## Library of python3

### install wiringpi
    1. pip3 install wiringpi
    
#### Change Color of Backlight
One of Grove - LCD RGB Backlight's most important feature is changing the backlight color. It's very simple; just use the folowing function:

    setRGB(r,g,b)

#### Clear display

You can clear the display by this function:

    clear()

#### Turn on and turn off display

    noDisplay()           // turn off display
    display()             // turn on display

#### Blink

    stopBlink()
    blink()

#### Cursor

    noCursor()
    cursor()

#### Blink LED Backlight

    blinkLED()
    noBlinkLED()


* @n [Get the module here]
* @n This example Set the volume size and play music snippet.
* @n [Connection and Diagram]
*
* Copyright	[DFRobot](http://www.dfrobot.com), 2016
* Copyright	GNU Lesser General Public License


## History

- data 2017-9-27
- version V1.0

## Credits

- author [Luyuhao  <yuhao.lu@dfrobot.com>]
