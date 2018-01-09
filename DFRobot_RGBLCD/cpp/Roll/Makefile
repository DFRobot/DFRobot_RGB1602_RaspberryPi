
objs := Roll.o ../DFRobot_RGBLCD.o 

Roll : $(objs)
	g++ -Wall -lwiringPi -o Roll $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f Roll *.o
