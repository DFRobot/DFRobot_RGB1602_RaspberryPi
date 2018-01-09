
objs := Fade.o ../DFRobot_RGBLCD.o 

Fade : $(objs)
	g++ -Wall -lwiringPi -o Fade $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f Fade *.o
