#include<Servo.h>
Servo throttle,yaw,aileron,elevator,aux;
int set=1;
void setup()
{
  Serial.begin(57600);
  throttle.attach(5);
  yaw.attach(6);
  aileron.attach(3);
  elevator.attach(4);
  aux.attach(2);
  pinMode(8,INPUT);
  pinMode(12,INPUT);
  pinMode(11,INPUT);
  pinMode(10,INPUT);
}
void arm()
{
  
  aux.writeMicroseconds(1996);
  throttle.writeMicroseconds(1100);
  yaw.writeMicroseconds(964);
  delay(2000);
  Serial.print("armed");
 }

void throttleUp()
{
  
  for(int i=0;i<15;i++)
  {
    throttle.writeMicroseconds(1100+30*i);
    delay(500);
  
  }
}
void yawLeft()
{
  for(int b=0;b<15;b++)
  {
    yaw.writeMicroseconds(1496+15*b);
    delay(400);
  }
}
void throttleDown()
{
  for(int c=0;c<35;c++)
  {
    throttle.writeMicroseconds(1350-10*c);
    delay(1000);
  }
}
void loop()
{
int ON = digitalRead(7);
int STOP = digitalRead(8);
int ULTRA = digitalRead(9);

if(ON==1)
{
  set=1;
}
if(set==1)
{
 arm();
 throttle();
 a++;
}
if(a==2)
{
 yaw();
  yaw.writeMicroseconds(1496);
  a++;
}
if(a==2)
{
  down();
  a++;
  }
if(a=3)
{
  throttle.writeMicroseconds(1100);
  yaw.writeMicroseconds(1964);
  delay(2000);
  a++;
} 
 
}
    
