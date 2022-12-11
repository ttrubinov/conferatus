#ifndef clearSfrBit
#define clearSfrBit(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif

#ifndef setSfrBit
#define setSfrBit(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

static int sum_a, sum_b, sum_c;
static int middle_a, middle_b, middle_c;
static int avexp_a, avexp_b, avexp_c;
static int a1, a2, a3, b1, b2, b3, c1, c2, c3;

void setup() {
//    pinMode(A1, INPUT);
//    pinMode(A4, INPUT);
//    pinMode(A7, INPUT);
    
    setSfrBit(ADCSRA,ADPS2);
    clearSfrBit(ADCSRA,ADPS1);
    clearSfrBit(ADCSRA,ADPS0);
  
    Serial.begin(9600);
}

void loop() {

    sum_a = 0;
    sum_b = 0;
    sum_c = 0;
    
    for (int i=0; i<2; i++){
        a1 = analogRead(A1);
        b1 = analogRead(A4);
        c1 = analogRead(A7);
        
        a2 = analogRead(A1);
        b2 = analogRead(A4);
        c2 = analogRead(A7);
        
        a3 = analogRead(A1);
        b3 = analogRead(A4);
        c3 = analogRead(A7);
        
        middle_a = (a1 < a2) ? ((a2 < a3) ? a2: ((a3 < a1) ? a1: a3)): ((a1 < a3) ? a1: ((a3 < a2) ? a2: a3));
        sum_a += a3;
        middle_b = (b1 < b2) ? ((b2 < b3) ? b2: ((b3 < b1) ? b1: b3)): ((b1 < b3) ? b1: ((b3 < b2) ? b2: b3));
        sum_b += b3;
        middle_c = (c1 < c2) ? ((c2 < c3) ? c2: ((c3 < c1) ? c1: c3)): ((c1 < c3) ? c1: ((c3 < c2) ? c2: c3));
        sum_c += c3;
    }
    
    sum_a = sum_a/2;
    avexp_a += (sum_a - avexp_a) >>3;
    sum_b = sum_b/2;
    avexp_b += (sum_b - avexp_b) >>3;
    sum_c = sum_c/2;
    avexp_c += (sum_c - avexp_c) >>3;
    
    Serial.print(avexp_a - 250);
    Serial.print(" ");
    Serial.print(avexp_b - 250);
    Serial.print(" ");
    Serial.println(avexp_c - 250);

    delay(10);
}
 
