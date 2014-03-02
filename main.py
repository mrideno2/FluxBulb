# def main(filename):

import urllib2
import time
import calendar
import datetime
import math
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

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

    temp = datetime.datetime.now().utctimetuple()
    curTime = calendar.timegm(datetime.datetime.now().utctimetuple())
    curTime += datetime.datetime.now().microsecond/1e6 # sub-second precision

    arduinoCommand = ""

    if (comChar == 's'):
            brightness = computeBrightness(0,curTime,86400)
            arduinoCommand = "b"+str(brightness)            
    elif (comChar == 'i'):
            duration = int(command[1:])
            brightness = computeBrightness(0,curTime,duration)
            arduinoCommand = "b"+str(brightness)
    elif (comChar == 'c'):
            level = int(command[1:])
            brightness = level
            arduinoCommand = "b"+str(brightness)
    elif (comChar == 'm'):
            time.sleep(0.7)
            arduinoCommand = "i"
    else:
        print("COULD NOT IDENTIFY")    
    

    print(arduinoCommand)
    ser.write(arduinoCommand + ",")
    time.sleep(0.3)