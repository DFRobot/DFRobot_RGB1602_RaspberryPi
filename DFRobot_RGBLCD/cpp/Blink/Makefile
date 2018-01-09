
objs := Blink.o ../DFRobot_RGBLCD.o 

Blink : $(objs)
	g++ -Wall -lwiringPi -o Blink $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f Blink *.o
