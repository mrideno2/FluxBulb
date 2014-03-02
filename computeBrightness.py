# param     initialTime     A time
# param     curTime         A time
# param     cycleTime       The duration of a full cycle (000 -> 255 -> 001)
# throws exception if (curTime < initialTime)
# returns   brightness 		A brightness level from 0-255
import math

def computeBrightness(initialTime, curTime, cycleTime):
	
	if curTime<initialTime:
		raise Exception("Value Error")
	else:
		brightness = (2*math.pi)
		print brightness
		brightness = brightness/cycleTime
		print brightness
		brightness = brightness * (curTime-initialTime)
		print brightness
		brightness = math.sin(brightness*0.5)
		print brightness
		brightness = (255.0/2)*brightness
		print brightness
		brightness = brightness+(255.0/2)
		#brightness = int((255/2)*math.sin((2*math.pi)/cycleTime*(curTime-initialTime))+(255/2))

	print brightness
	return brightness



initialTime = input("Enter the initial time: ")
curTime = input("Enter the current time: ")
cycleTime = input("Enter the cycle range: ")

computeBrightness(initialTime,curTime,cycleTime)