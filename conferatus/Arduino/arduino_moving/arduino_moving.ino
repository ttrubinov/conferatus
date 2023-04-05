#include <ServoSmooth.h>

ServoSmooth servo;
uint8_t targetAngle;

void setup() {
    Serial.begin(9600);
    servo.attach(2);        // привод на d2
    servo.setSpeed(70);
    servo.setAccel(0.3);
}

void loop() {
    servo.tick();

    if (Serial.available() > 0) {
        targetAngle = Serial.read();
        servo.setTargetDeg(targetAngle);
    }

    delay(15);
}
