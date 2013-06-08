// Amber Fechko, quick and dirty motor/button solution for peristaltic pump driver.
// amber@kelpforest.org

int buttonPin = 4;              // which pin is the button switch connected to?
int pinI1 = 8;                  // motor shield interface I1
int pinI2 = 11;                 // motor shield interface I2
int speedpinA=9;                // enable motor A
int pwmSpeed = 255;            // define the pwmSpeed of motor
int buttonState = 0;            // tracking whether button is pressed or not
 
void setup() {
    pinMode(pinI1,OUTPUT);      // configure pinI1 as output
    pinMode(pinI2,OUTPUT);      // configure pinI2 as output
    pinMode(speedpinA,OUTPUT);  // enable motor pin as output
    pinMode(buttonPin, INPUT);  // enable buttonPin as input
    digitalWrite(pinI1,LOW);
    digitalWrite(pinI2,LOW);
}
 
void forward() {
     analogWrite(speedpinA,pwmSpeed);      // input a simulation value to set the speed
     digitalWrite(pinI2,LOW);              // turn DC Motor clockwise
     digitalWrite(pinI1,HIGH);
}
void backward() {
     analogWrite(speedpinA,pwmSpeed);      // input a simulation value to set the speed
     digitalWrite(pinI2,HIGH);             // turn DC Motor counterclockwise
     digitalWrite(pinI1,LOW);
}
void stop() {
     digitalWrite(speedpinA,LOW);          // disable the pin to stop the motor -- this should be done to avid damaging the motor. 
     delay(1000);
}

void loop() {
    buttonState = digitalRead(buttonPin);  // check button pin for pressed button
    //Serial.print(buttonState);
    if (buttonState == HIGH) {             // if button is being pressed..
        forward();                         // move forward for ...
        delay(1000);                       // .. two seconds ..
        stop();                            // .. then stop the motor...
        delay(100);                        // .. and hold everything for a half second.
    } else {    
      delay(100);
    }
}
