#include <ServoSmooth.h>

ServoSmooth servo;
uint8_t targetAngle;

void setup() {
    Serial.begin(9600);
    servo.attach(2, 1000, 2000);        // привод на d2
    servo.setSpeed(60);
    servo.setAccel(0.2);
}

void loop() {
    servo.tick();
    
    if (Serial.available() > 0) {
        targetAngle = Serial.read();
        if (targetAngle >= 0) {
          servo.setTargetDeg(targetAngle);
          Serial.print(targetAngle);
        }
    }

    delay(2);
}
