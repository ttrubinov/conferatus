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
#define VOL_THRESHOLD 90
#define VOL_SILENCE 60
#define minSoundCount 5
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
        //digitalWrite(Led, HIGH);
        running = true;
      }
      if (str[0] == 's'){
        digitalWrite(Led, LOW);
        running = false;
      }
    }
    if (running){
      Serial.println("S");
        // Finding silence
      bool silence = false;
      silence_counter = 0;
      index = 0;
      while(!silence)
      {
        vol[0][index] = analogRead(MIC_PIN_0) - bias;
        vol[1][index] = analogRead(MIC_PIN_1) - bias;
        vol[2][index] = analogRead(MIC_PIN_2) - bias;
        if (abs(vol[0][index]) < VOL_SILENCE){
          silence_counter++;
        }
        else{
          silence_counter = 0;
        }
        if (abs(vol[1][index]) < VOL_SILENCE){
          silence_counter++;
        }
        else{
          silence_counter = 0;
        }
        
        if (abs(vol[2][index]) < VOL_SILENCE){
          silence_counter++;
        }
        else{
          silence_counter = 0;
        }

        index++;
        if (index == RememberMax){
          index = 0;
        }
        if (silence_counter >= (3 * RememberMax)){
          silence = true;
        }
      }
      digitalWrite(Led, HIGH);
      //Ищет превышение звука
      int prev1=0, prev2=0, prev3=0;
      while(1){
        
        vol[0][index] = analogRead(MIC_PIN_0) - bias;
        vol[1][index] = analogRead(MIC_PIN_1) - bias;
        vol[2][index] = analogRead(MIC_PIN_2) - bias;
        
        if (abs(vol[0][index]) >= VOL_THRESHOLD){
          prev1++;
          if (prev1== minSoundCount){
            break;
          }
        }
        else{
          prev1 = 0;
        }
        
        if (abs(vol[1][index]) >= VOL_THRESHOLD){
        prev2++;
          if (prev2== minSoundCount){
            break;
          }
        }
        else{
          prev2 = 0;
        }
      
        if (abs(vol[2][index]) >= VOL_THRESHOLD){
          prev3++;
          if (prev3== minSoundCount){
            break;
          }
        }
        else{
          prev3 = 0;
        }
        
        index++;
        if (index >= RememberMax){
          index = 0;
        }
      }
      int count = 0;
      while (count < RememberMax - minSoundCount){
        vol[0][index] = analogRead(MIC_PIN_0) - bias;
        vol[1][index] = analogRead(MIC_PIN_1) - bias;
        vol[2][index] = analogRead(MIC_PIN_2) - bias;
        index++;
        if (index >= RememberMax){
          index = 0;
        }
        count++;
      }

      int start = index;
      index+=1;
      if (index == RememberMax){
        index = 0;
      }
      digitalWrite(Led, LOW);
      while (start != index){
        Serial.print(vol[0][index]);
        Serial.print(" ");
        Serial.print(vol[1][index]);
        Serial.print(" ");
        Serial.println(vol[2][index]);

        index++;
        if (index >= RememberMax){
          index = 0;
        }
      }
      Serial.print(vol[0][index]);
      Serial.print(" ");
      Serial.print(vol[1][index]);
      Serial.print(" ");
      Serial.println(vol[2][index]);


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
