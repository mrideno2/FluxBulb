import urllib2
import json

# json_data = urllib2.urlopen("http://fluxbulb.hackmason.org:3000/hi")
# data = json.load(json_data)
# print(data["user"])


response = urllib2.urlopen("http://fluxbulb.hackmason.org:3000/arduinoCommand").read()
print(response)	
