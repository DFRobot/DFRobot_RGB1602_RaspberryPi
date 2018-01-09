
objs := TextDirection.o ../DFRobot_RGBLCD.o 

TextDirection : $(objs)
	g++ -Wall -lwiringPi -o TextDirection $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f TextDirection *.o
