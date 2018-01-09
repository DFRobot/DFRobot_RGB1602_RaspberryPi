
objs := CustomSymbol.o ../DFRobot_RGBLCD.o 

CustomSymbol : $(objs)
	g++ -Wall -lwiringPi -o CustomSymbol $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f CustomSymbol *.o
