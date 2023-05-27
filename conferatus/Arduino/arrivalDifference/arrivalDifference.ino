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
#define WAIT_LIMIT 15
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
static int vol[3];
static String str;

static bool ready = true;
static int silence_counter=0;
int vol1 =0;
int vol2 =0;
int vol3 =0;

//Сюда будем писать на каком шаге звук пришёл на каждый из микрофонов
int tick[] = {0,0,0};
//Микрофоны должны ловить один и тот же звук, а значит, разница в приходе звука на микрофоны 
//не должна быть очень большой
static int floatRes = 0;
int wait = 0;
void loop() 
{
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
        // digitalWrite(Led, HIGH);
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
      while(!silence){
        vol[0] = analogRead(MIC_PIN_0) - bias;
        vol[1] = analogRead(MIC_PIN_1) - bias;
        vol[2] = analogRead(MIC_PIN_2) - bias;
        if (abs(vol[0]) < VOL_SILENCE){
          silence_counter++;
        }
        else{
          silence_counter = 0;
        }
        if (abs(vol[1]) < VOL_SILENCE){
          silence_counter++;
        }
        else{
          silence_counter = 0;
        }
        
        if (abs(vol[2]) < VOL_SILENCE){
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
      break;
    }
  }




  for (unsigned long i = 0; i < T; ++i) {
    vol[0] = analogRead(MIC_PIN_0);
    vol[1] = analogRead(MIC_PIN_1);
    vol[2] = analogRead(MIC_PIN_2);
    
    for (int j = 0; j < 3; ++j) {
      //Если хоть на один микрофон уже пришёл звук, мы должны следить, чтобы он пришёл 
      //и на остальные не позднее определённого WAIT_LIMIT момента
      if (tick[0] || tick[1] || tick[2]) {
        ++wait;
        if (wait > WAIT_LIMIT) {
          tick[0] = tick[1] = tick[2] = 0;
          wait = 0;
        }
      }
      if (vol[j] < VOL_THRESHOLD) {
        continue;
      }
      if (!tick[j]) tick[j] = i;
    }
    
    //Если сигнал пришёл на все три микрофона, определим положение сервопривода
    if (tick[0] && tick[1] && tick[2]) {
      //Реализуем алгоритм определения положения источника звука, как было описано выше
      int delta01 = tick[0]-tick[1];
      int delta21 = tick[2]-tick[1];
      tick[0] = tick[1] = tick[2] = 0;
      if (delta01 <= delta21 && delta21 <= 0) {
        floatRes += (0  - floatRes) / 2;
        Serial.println(floatRes);
        delay(1000);
        continue;
      }
      if (delta21 <= delta01 && delta01 <= 0) {
        floatRes += (180  - floatRes) / 2;
        Serial.println(floatRes);
        delay(1000);
        continue;
      }
      if (delta01 >= delta21 && delta21 >= 0) {
        float q = (float) (delta21) / delta01;
        floatRes += (135 - 45 * q  - floatRes) / 2;
        Serial.println(floatRes);
        continue;
      }
      if (delta21 >= delta01 && delta01 >= 0) {
        float q = (float) (delta01) / delta21;
        floatRes += (45 + 45 * q  - floatRes) / 2;
        Serial.println(floatRes);
        continue;
      }
      if (delta01 >= 0 && delta21 <= 0) {
        float q = (float) (-delta21) / (delta01 - delta21);
        floatRes += (135 + 45 * q  - floatRes) / 2;
        Serial.println(floatRes);
        continue;
      }
      if (delta21 >= 0 && delta01 <= 0) {
        float q = (float) (-delta01) / (delta21 - delta01);
        floatRes += (45 * (1 - q)  - floatRes) / 2;
        Serial.println(floatRes);
        continue;
      }
    }
  }
  delay(1000);
}