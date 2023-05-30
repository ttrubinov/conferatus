#include <ServoSmooth.h>

ServoSmooth servo;
uint8_t targetAngle;

void setup() {
    Serial.begin(230400);
//    servo.attach(2, 1000, 2000);        // привод на d2
    servo.attach(2);
    servo.setSpeed(40);
    servo.setAccel(0.8);

    servo.setTargetDeg(90);
}

//uint32_t tmr;
//boolean flag;

void loop() {
    if (Serial.available() > 0) {
        targetAngle = Serial.read();
        if (targetAngle >= 0 && targetAngle <= 180) {
          servo.setTargetDeg(targetAngle);
          Serial.println(targetAngle);
        }
    }

//if (millis() - tmr >= 4000) {   // каждые 3 сек
//    tmr = millis();
//    flag = !flag;
//    servo.setTargetDeg(flag ? 0 : 180);  // двигаем на углы 50 и 120
//  }
//
    servo.tick();
}
