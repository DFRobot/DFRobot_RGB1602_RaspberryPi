
objs := SetCursor.o ../DFRobot_RGBLCD.o 

SetCursor : $(objs)
	g++ -Wall -lwiringPi -o SetCursor $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f SetCursor *.o
