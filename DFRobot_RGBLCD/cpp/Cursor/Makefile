
objs := Cursor.o ../DFRobot_RGBLCD.o 

Cursor : $(objs)
	g++ -Wall -lwiringPi -o Cursor $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f lcd_1602 *.o
