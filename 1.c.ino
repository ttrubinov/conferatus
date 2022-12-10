
#define MOD 0

static int a5, a6, a7;

static int a5f = 0, a6f = 0, a7f = 0;

//inline void expRunningAverage() {
//  a5f += (a5 - a5f) / 5;
//  a6f += (a6 - a6f) / 5;
//  a7f += (a7 - a7f) / 5;
//}

void setup() {
    Serial.begin(9600);
}
 
void loop() {
    a5 = analogRead(A5);
    a6 = analogRead(A6);
    a7 = analogRead(A7);

    a5 -= MOD;
    if (a5 < 0) {
      a5 = -a5;
    }


    a6 -= MOD;
    if (a6 < 0) {
      a6 = -a6;
    }

    a7 -= MOD;
    if (a7 < 0) {
      a7 = -a7;
    }

    a5f += (a5 - a5f) / 5;
  a6f += (a6 - a6f) / 5;
  a7f += (a7 - a7f) / 5;
   
    
    Serial.print(a5f);
    Serial.print(" ");
    Serial.print(a6f);
    Serial.print(" ");
    Serial.println(a7f);

    delay(3);
}
 
