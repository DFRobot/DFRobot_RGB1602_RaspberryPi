
objs := HelloWorld.o ../DFRobot_RGBLCD.o 

HelloWorld : $(objs)
	g++ -Wall -lwiringPi -o HelloWorld $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f HelloWorld *.o
