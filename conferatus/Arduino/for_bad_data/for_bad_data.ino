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
#define VOL_THRESHOLD 80
#define VOL_SILENCE 40
#define minSoundCount 4
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
  attachInterrupt(digitalPinToInterrupt(2), button, RISING);
  Serial.begin(230400);
}
void button() {
  running = false;
}


static int index = 0;
static int vol[3][RememberMax];
static String str;

static bool ready = true;
static int silence_counter=0;
int vol1 =0;
int vol2 =0;
int vol3 =0;
void loop() {
  while(1){
    //start and continue
    if (Serial.available() > 0) {  //
      // start
      str = Serial.readString();
      if (str[0] == 'i') {
        digitalWrite(Led, HIGH);
        running = true;
      }
      if (str[0] == 'c'){
         digitalWrite(Led, HIGH);
        running = true;
      }
      if (str[0] == 's'){
        digitalWrite(Led, LOW);
        running = false;
      }
    }
    index = 0;    
    if (running){
      Serial.println("S");
      int count = 0;
      while (index < RememberMax){
        vol[0][index] = analogRead(MIC_PIN_0) - bias;
        vol[1][index] = analogRead(MIC_PIN_1) - bias;
        vol[2][index] = analogRead(MIC_PIN_2) - bias;
        index++;
      }
      index=0;
      while (RememberMax > index){
        Serial.print(vol[0][index]);
        Serial.print(" ");
        Serial.print(vol[1][index]);
        Serial.print(" ");
        Serial.println(vol[2][index]);

        index++;
        
      }


      // Serial.flush();
      Serial.println("E");
      running=false;
      digitalWrite(Led, LOW);
    }
    // else{
    //   delay(1000);
    // }
  }
}
