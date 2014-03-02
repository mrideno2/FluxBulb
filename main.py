# def main(filename):

import urllib2
import time
import calendar
import datetime
import math
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)


def computeBrightness(initialTime, curTime, cycleTime):
    
    if curTime<initialTime:
        raise Exception("Value Error")
    else:
        curTime -= 5*60*60 #adjust for timezone, so that brightness peaks at noon (local time)
        curTime = curTime % cycleTime   # no need to compute with super large numbers
        
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


while (True):
    command = urllib2.urlopen("http://fluxbulb.hackmason.org:3000/arduinoCommand").read()

    comChar = command[0]

    curTime = calendar.timegm(datetime.datetime.now().utctimetuple())

    if (comChar == 's'):
            brightness = computeBrightness(0,curTime,86400)
    elif (comChar == 'i'):
            duration = int(command[1:])
            brightness = computeBrightness(0,curTime,duration)
    elif (comChar == 'c'):
            level = int(command[1:])
            brightness = level
    else:
        print("COULD NOT IDENTIFY")    
    

    ser.write(b+brightness)
    print brightness
    time.sleep(1)