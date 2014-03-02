# NOTE, for whatever reason, use curTime = calendar.timegm(datetime.datetime.now().utctimetuple()).


# param     initialTime     A unix timestamp
# param     curTime         A unix timestamp
# param     cycleTime       The duration of a full cycle (000 -> 255 -> 001) in seconds
# throws exception if (curTime < initialTime)
# returns   brightness 		A brightness level from 0-255
import math

def computeBrightness(initialTime, curTime, cycleTime):
	
	if curTime<initialTime:
		raise Exception("Value Error")
	else:
		curTime -= 5*60*60 #adjust for timezone, so that brightness peaks at noon (local time)
		curTime = curTime % cycleTime	# no need to compute with super large numbers
		
		brightness = 2*math.pi

		brightness = brightness / cycleTime
		
		brightness = brightness * curTime

		brightness = math.sin(brightness)

		brightness = brightness + 1

		brightness = brightness * 255/2
		brightness = int(brightness)
	        brightness = str(brightness)
	        brightness = 'b'+brightness

		return brightness

# import time
# import datetime
# import calendar

# initialTime = 0
# # curTime = int(time.time()) # avoid?
# curTime = calendar.timegm(datetime.datetime.now().utctimetuple())
# cycleTime = 24*60*60

# --- use this block to compute FUTURE timestamps for testing purposes ---
# future = datetime.datetime.now() + datetime.timedelta(hours = 0)
# curTime = calendar.timegm(future.utctimetuple())

# --- use this block to accept test data from stdin ---
#initialTime = input("Enter the initial time: ")
#curTime = input("Enter the current time: ")
#cycleTime = input("Enter the cycle range: ")

# print(computeBrightness(initialTime,curTime,cycleTime))
