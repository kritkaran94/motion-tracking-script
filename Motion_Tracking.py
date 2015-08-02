''' 

 Motion tracking using SimpleCV

'''

from SimpleCV import *

import time
import os
import sys

cam = Camera()

threshold = 3.0

dis = Display()

prev = cam.getImage()

prev.show()

while(dis.isNotDone()):

	time.sleep(0.2) #200 milli-sec
	
	current = cam.getImage()
	
	current.show()
	
	diff = current - prev
	
	matrix = diff.getNumpy()
	
	mean = matrix.mean()
	
	diff.show()

	if(mean>=threshold):
		os.system("./t2s.sh \"Krit Motion Detected\"")
	elif(mean<threshold):
		print('Undetected')

	prev = current


