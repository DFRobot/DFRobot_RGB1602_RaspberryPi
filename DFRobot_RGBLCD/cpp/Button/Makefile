
objs := Button.o ../DFRobot_RGBLCD.o 

Button : $(objs)
	g++ -Wall -lwiringPi -o Button $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f Button *.o
