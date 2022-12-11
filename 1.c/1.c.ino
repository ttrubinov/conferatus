#ifndef clearSfrBit
#define clearSfrBit(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif

#ifndef setSfrBit
#define setSfrBit(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

#define MOD 250

static int a1, a4, a7;

static int a1f = 0, a4f = 0, a7f = 0;

//inline void expRunningAverage() {
//  A1f += (A1 - A1f) / 5;
//  A4f += (A4 - A4f) / 5;
//  a7f += (a7 - a7f) / 5;
//}

void setup() {
    clearSfrBit(ADCSRA,ADPS2);
    clearSfrBit(ADCSRA,ADPS1);
    clearSfrBit(ADCSRA,ADPS0);
  
    
    Serial.begin(9600);
}
 
void loop() {
    a1 = analogRead(A1);
    a4 = analogRead(A4);
    a7 = analogRead(A7);

    a1 -= MOD;
    if (a1 < 0) {
      a1 = -a1;
    }


    a4 -= MOD;
    if (a4 < 0) {
      a4 = -a4;
    }

    a7 -= MOD;
    if (a7 < 0) {
      a7 = -a7;
    }

    a1f += (a1 - a1f) / 5;
  a4f += (a4 - a4f) / 5;
  a7f += (a7 - a7f) / 5;
   
    
    Serial.print(a1f);
    Serial.print(" ");
    Serial.print(a4f);
    Serial.print(" ");
    Serial.println(a7f);

    delay(7);
}
 
