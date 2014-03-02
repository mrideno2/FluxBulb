// testing infrared sensor on arduino board
#include <Servo.h>
Servo potservo; // create servo object to control a servo
int angle = 0; // variable to store the servo position
int brightness1=0;
int brightness2=255;
int potpin = 0;
int led1pin = 3;
int led2pin = 5;
int inf,mV,cm;
const int infpin = 4;
const long referencemV = 5000;

void setup()
{
Serial.begin(9600);
Serial.println("write 0 for 'timing' or 1 for'enter exit' to select between modes");
potservo.attach(9); // attaches the servo on pin 9 to the servo object
pinMode(led1pin, OUTPUT);
}

void loop()
{
  if (Serial.available()){
   
    char ch = Serial.read();
    if (ch == "1"){
    for(d = 0, d<181, d+=90){
    angle = d;
    potservo.write(angle);
    pot = analogRead(potpin);
    Serial.println(pot);
    brightness1 = map(pot, 0,1023,0,255);
    brightness2 = map(pot,0, 1023, 255, 0);
    analogWrite(led1pin, brightness1);
    analogWrite(led2pin, brightness2);
    delay(5000);
    }
    }
    else if (ch == "0"){
      inf = analogRead(infpin);
      mV = (inf * referencemV)/1023;
      cm = getDistance(mV);
      Serial.print(mV);
      Serial.print(",");
      Serial.print(cm);
      if (cm<60){
        for(brightness1 = 0, brightness <256, brightness+=1){
           analogWrite(led1pin,brightness1);
           analogWrite(led2pin, 255-brightness1);
           delay(1000)
        }
       else // makes a timer that sees distance, have some other sort of thing irl that 
       {
         delay(30000);//delays 30s for demo version
       }
      }
    }
  
      delay(1000);
  }

}

// the following is used to interpolate the distance from a table
// table entries are distances in steps of 250 millivolts
const int TABLE_ENTRIES = 12;
const int firstElement = 250; // first entry is 250 mV
const int INTERVAL = 250; // millivolts between each element
static int distance[TABLE_ENTRIES] = {150,140,130,100,60,50,40,35,30,25,20,15};
int getDistance(int mV)
{
if( mV > INTERVAL * TABLE_ENTRIES-1 )
return distance[TABLE_ENTRIES-1];
else
{
int index = mV / INTERVAL;
float frac = (mV % 250) / (float)INTERVAL;
return distance[index] - ((distance[index] - distance[index+1]) * frac);
}
}
