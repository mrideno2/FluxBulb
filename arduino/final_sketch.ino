// testing infrared sensor on arduino board
#include <Servo.h>
Servo potservo; // create servo object to control a servo
int angle = 0; // variable to store the servo position
int brightness=0;
int potpin = 0;
int led1pin = 3;
int led2pin = 5;
int inf,mV,cm,d,pot;
const int infpin = 4;
const long referencemV = 5000;

void setup()
{
Serial.begin(9600);

//Serial.println("write '0' for 'timing' or '1' for 'infrared' to select between modes");
potservo.attach(9); // attaches the servo on pin 9 to the servo object
pinMode(potpin, INPUT);
pinMode(infpin,INPUT);
pinMode(led1pin, OUTPUT);
pinMode(led2pin, OUTPUT);

}

void loop()
{
  if (Serial.available()){
   
    char ch[16];
    Serial.readBytesUntil(',', ch,16);
    if (ch[0] == 'b'){
      brightness = Serial.parseInt();
      analogWrite(led1pin, brightness);
      analogWrite(led2pin, brightness);
      delay(200);
    }

    else if (ch[0] == 'i'){
      inf = analogRead(infpin);
      mV = (inf * referencemV)/1023;
      cm = getDistance(mV);
      Serial.print(mV);
      Serial.print(",");
      Serial.print(cm);
      if (cm<60){
        for(brightness = 0; brightness <256; brightness+=1){
           analogWrite(led1pin,brightness);
           analogWrite(led2pin, brightness);
           delay(50);
        }
      }
       else // makes a timer that sets an "off" delay time if the user command isn't recognized
       {
         analogWrite(led1pin, 0);
         analogWrite(led2pin,0);
       }
    }
  else
  {
    analogWrite(led1pin, 0);
    analogWrite(led2pin,0);
    
      delay(1000);
  }
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
