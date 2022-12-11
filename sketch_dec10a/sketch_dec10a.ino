#define MIC_PIN A7
#define ITERATIONS 10000

#ifndef clearSfrBit
#define clearSfrBit(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif

#ifndef setSfrBit
#define setSfrBit(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() {
  pinMode(MIC_PIN, INPUT);
  
  clearSfrBit(ADCSRA,ADPS2);
  clearSfrBit(ADCSRA,ADPS1);
  clearSfrBit(ADCSRA,ADPS0);
  
  Serial.begin(9600);
}

int t1, t2;

void loop() {
  t1 = millis();
  for (int i = 0; i < ITERATIONS; i++) {
      analogRead(MIC_PIN);
  }
  Serial.println(millis() - t1);
}

// около 9000 опросов за секунду (без любых вычислений вообщще!!!!!!!)
