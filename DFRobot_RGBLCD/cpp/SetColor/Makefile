
objs := SetColor.o ../DFRobot_RGBLCD.o 

SetColor : $(objs)
	g++ -Wall -lwiringPi -o SetColor $(objs) 

%.o : %.c
	g++ -c -o $@ $<

clean:
	rm -f SetColor *.o
