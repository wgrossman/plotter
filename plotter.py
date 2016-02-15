# python code to do host side plotting

# plotter 

import time
import numpy as np
import matplotlib.pyplot as plt
import serial

ser = serial.Serial('/dev/cu.usbmodem1412', 115200, timeout = 0)
print "Connecting to serial port " + ser.name

plt.axis([0, 100, 0, 1])
#plt.show()

data_points = []

while(1):

	if (ser.inWaiting() > 0):
		value = ser.readline().rstrip()
		try:
			formatted_value = float(value)
			print formatted_value
			data_points.append(formatted_value)
			if len(data_points) > 100:
				data_points = data_points[-100:]
			plt.plot(data_points)
			plt.pause(.0001)
		except:
			# do nothing
			print "uh oh"
