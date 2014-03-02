# def main(filename):

while (true):
    command = urllib2.urlopen("http://fluxbulb.hackmason.org:3000/arduinoCommand").read()

    comChar = command[0]


    if (comChar == 's'):
            brightness = computeBrightness(0,calendar.timegm(datetime.datetime.now().utctimetuple()),86400)
            print "Standard Brightness"

    
    elif (comChar == 'i'):
            #set brightness to computeBrightness(...)				#"b0" "b143" "b255"
            duration = int(command[1:])
            brightness = computeBrightness(0,calendar.timegm(datetime.datetime.now().utctimetuple()),duration)
            print "Set Duration"
    elif (comChar == 'c'):
            #set brightness to level 
            level = int(command[1:])								#"b12" "b12" "b12" "b12"
            brightness = level
            print "Set Level"
	else
		print("COULD NOT IDENTIFY")    
    }

    print brightness