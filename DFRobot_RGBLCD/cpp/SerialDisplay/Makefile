
objs := SerialDisplay.o ../DFRobot_RGBLCD.o 

SerialDisplay : $(objs)
	g++ -Wall -lwiringPi -o SerialDisplay $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f SerialDisplay *.o
