#define MIC_PIN_0 A1
#define MIC_PIN_1 A4
#define MIC_PIN_2 A7
#define Led A3

#ifndef clearBit
#define clearBit(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif

#ifndef setBit
#define setBit(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

#define T 1000000
#define WAIT_LIMIT 10
#define VOL_THRESHOLD 65
#define VOL_SILENCE 35
#define minSoundCount 8
#define RememberMax 250
#define bias 250


#define bitADPS0 1
#define bitADPS1 0
#define bitADPS2 0

#define delayM 0
static bool running = false;
void setup() {
  pinMode(MIC_PIN_0, INPUT);
  pinMode(MIC_PIN_1, INPUT);
  pinMode(MIC_PIN_2, INPUT);
  pinMode(Led, OUTPUT);

#if bitADPS0 == 0
  clearBit(ADCSRA, ADPS0);
#else
  setBit(ADCSRA, ADPS0);
#endif
#if bitADPS1 == 0
  clearBit(ADCSRA, ADPS1);
#else
  setBit(ADCSRA, ADPS1);
#endif
#if bitADPS0 == 0
  clearBit(ADCSRA, ADPS2);
#else
  setBit(ADCSRA, ADPS2);
#endif
  Serial.begin(230400);
}

int vol1, vol2, vol3;
void loop() {
  vol1 = analogRead(MIC_PIN_0) - bias;
  vol2 = analogRead(MIC_PIN_1) - bias;
  vol3 = analogRead(MIC_PIN_2) - bias;

  Serial.print(vol1);
  Serial.print(" ");
  Serial.print(vol2);
  Serial.print(" ");
  Serial.println(vol3);
  
  
  
}
