#!/usr/bin/python
import time

while 1:
	tempfile = open("/sys/bus/w1/devices/28-00043e92adff/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n") [1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	temperature = (temperature * 1.8) + 32	
	print temperature

	time.sleep(1)
