
objs := Display.o ../DFRobot_RGBLCD.o 

Display : $(objs)
	g++ -Wall -lwiringPi -o Display $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f Display *.o
