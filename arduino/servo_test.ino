//led voltage divider test

int pot;

int brightness1;
int brightness2;
int potpin = 0;
int led1pin = 3;
int led2pin = 5;

void setup()
{

Serial.begin(9600);
pinMode(potpin, INPUT);
//pinmode(led1pin, OUTPUT);
//pinmode(led2pin, OUTPUT);

}

void loop()
{
  pot = analogRead(potpin);
  Serial.println(pot);
  brightness1 = map(pot, 0,1023,0,255);
  brightness2 = map(pot,0, 1023, 255, 0);
  analogWrite(led1pin, brightness1);
  analogWrite(led2pin, brightness2);
  delay(1000);
}
