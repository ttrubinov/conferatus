#include <ServoSmooth.h>

ServoSmooth servo;
uint8_t targetAngle;

void setup() {
    Serial.begin(9600);
    servo.attach(2, 1000, 2000);        // привод на d2
    servo.setSpeed(60);
    servo.setAccel(0.2);

    servo.setTargetDeg(90);
}

void loop() {
    servo.tick();
    
    if (Serial.available() > 0) {
        targetAngle = Serial.read();
        if (targetAngle >= 0 && targetAngle != 10) {
          servo.setTargetDeg(targetAngle);
          Serial.println(targetAngle);
        }
    }
//    Serial.print(23);
//    servo.setTargetDeg(60);

    delay(20);
}
