
objs := AutomateRoll.o ../DFRobot_RGBLCD.o 

AutomateRoll : $(objs)
	g++ -Wall -lwiringPi -o AutomateRoll $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f AutomateRoll *.o
