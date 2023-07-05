.PHONY: AutomateRoll Blink Button Cursor CustomSymbol Display Fade HelloWorld Roll SerialDisplay SetColor SetCursor TextDirection clean

objs_common := ../DFRobot_RGBLCD.o
objs :=
target :=

ifeq ($(filter AutomateRoll,$(MAKECMDGOALS)),AutomateRoll)
    objs := AutomateRoll.o $(objs_common)
    target := AutomateRoll
endif

ifeq ($(filter Blink,$(MAKECMDGOALS)),Blink)
    objs := Blink.o $(objs_common)
    target := Blink
endif

ifeq ($(filter Button,$(MAKECMDGOALS)),Button)
    objs := Button.o $(objs_common)
    target := Button
endif

ifeq ($(filter Cursor,$(MAKECMDGOALS)),Cursor)
    objs := Cursor.o $(objs_common)
    target := Cursor
endif

ifeq ($(filter CustomSymbol,$(MAKECMDGOALS)),CustomSymbol)
    objs := CustomSymbol.o $(objs_common)
    target := CustomSymbol
endif

ifeq ($(filter Display,$(MAKECMDGOALS)),Display)
    objs := Display.o $(objs_common)
    target := Display
endif

ifeq ($(filter Fade,$(MAKECMDGOALS)),Fade)
    objs := Fade.o $(objs_common)
    target := Fade
endif

ifeq ($(filter HelloWorld,$(MAKECMDGOALS)),HelloWorld)
    objs := HelloWorld.o $(objs_common)
    target := HelloWorld
endif

ifeq ($(filter Roll,$(MAKECMDGOALS)),Roll)
    objs := Roll.o $(objs_common)
    target := Roll
endif

ifeq ($(filter SerialDisplay,$(MAKECMDGOALS)),SerialDisplay)
    objs := SerialDisplay.o $(objs_common)
    target := SerialDisplay
endif

ifeq ($(filter SetColor,$(MAKECMDGOALS)),SetColor)
    objs := SetColor.o $(objs_common)
    target := SetColor
endif

ifeq ($(filter SetCursor,$(MAKECMDGOALS)),SetCursor)
    objs := SetCursor.o $(objs_common)
    target := SetCursor
endif

ifeq ($(filter TextDirection,$(MAKECMDGOALS)),TextDirection)
    objs := TextDirection.o $(objs_common)
    target := TextDirection
endif

$(target): $(objs)
	g++ -Wall -o $(target) $(objs) -lwiringPi
	rm -f *.o
	./$(target)

%.o: %.c
	g++ -c -o $@ $<

clean:
	rm -f AutomateRoll Blink Button Cursor CustomSymbol Display Fade HelloWorld Roll SerialDisplay SetColor SetCursor TextDirection *.o
