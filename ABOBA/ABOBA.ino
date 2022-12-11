#define MIC_PIN_0 A1
#define MIC_PIN_1 A4
#define MIC_PIN_2 A7

#ifndef clearBit
#define clearBit(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef setBit
#define setBit(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif
#define T 1000000
#define WAIT_LIMIT 200
#define VOL_THRESHOLD 300

void setup()
{
  pinMode(MIC_PIN_0, INPUT);
  pinMode(MIC_PIN_1, INPUT);
  pinMode(MIC_PIN_2, INPUT);
  setBit(ADCSRA,ADPS2) ;
  clearBit(ADCSRA,ADPS1) ;
  clearBit(ADCSRA,ADPS0) ;
  Serial.begin(9600);
}


int vol[] = {0,0,0};
//Сюда будем писать на каком шаге звук пришёл на каждый из микрофонов
int tick[] = {0,0,0};
//Микрофоны должны ловить один и тот же звук, а значит, разница в приходе звука на микрофоны 
//не должна быть очень большой
static int floatRes = 0;
int wait = 0;
void loop() 
{
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
      Serial.print(j);
      Serial.print("_");
      Serial.println(vol[j]);
      if (!tick[j]) tick[j] = i;
    }
    
    //Если сигнал пришёл на все три микрофона, определим положение сервопривода
    if (tick[0] && tick[1] && tick[2]) {
      //Весь этот отладочный вывод необязателен, но очень полезен
      Serial.print(0);
      Serial.print(": ");
      Serial.println(tick[0]);
      Serial.print(1);
      Serial.print(": ");
      Serial.println(tick[1]);
      Serial.print(2);
      Serial.print(": ");
      Serial.println(tick[2]);
      Serial.println("######################");
      
      //Реализуем алгоритм определения положения источника звука, как было описано выше
      int delta01 = tick[0]-tick[1];
      int delta21 = tick[2]-tick[1];
      tick[0] = tick[1] = tick[2] = 0;
      if (delta01 <= delta21 && delta21 <= 0) {
        floatRes += (0  - floatRes) / 2;
        Serial.println(floatRes);

        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
      if (delta21 <= delta01 && delta01 <= 0) {
        floatRes += (180  - floatRes) / 2;
        Serial.println(floatRes);
        
        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
      if (delta01 >= delta21 && delta21 >= 0) {
        float q = (float) (delta21) / delta01;
        floatRes += (135 - 45 * q  - floatRes) / 2;
        Serial.println(floatRes);
        
        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
      if (delta21 >= delta01 && delta01 >= 0) {
        float q = (float) (delta01) / delta21;
        floatRes += (45 + 45 * q  - floatRes) / 2;
        Serial.println(floatRes);

        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
      if (delta01 >= 0 && delta21 <= 0) {
        float q = (float) (-delta21) / (delta01 - delta21);
        floatRes += (135 + 45 * q  - floatRes) / 2;
        Serial.println(floatRes);
        
        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
      if (delta21 >= 0 && delta01 <= 0) {
        float q = (float) (-delta01) / (delta21 - delta01);
        floatRes += (45 * (1 - q)  - floatRes) / 2;
        Serial.println(floatRes);
        
        Serial.println("++++++++++++++++++++++");
        delay(1000);
        continue;
      }
    }
  }
  delay(1000);
}
