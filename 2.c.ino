static int a5, a6, a, b, c, middle, eee, lll;
static int sum=0;
static int a5f = 0, a6f = 0, a7f = 0;

void setup() {
    Serial.begin(9600);
}

void loop() {

    sum_a = 0;
    sum_b = 0;
    sum_c = 0;
    for (int i=0; i<4; i++){
        a1 = analogRead(A5);
        b1 = analogRead(A6);
        c1 = analogRead(A7);
        a2 = analogRead(A5);
        b2 = analogRead(A6);
        c2 = analogRead(A7);
        a3 = analogRead(A5);
        b3 = analogRead(A6);
        c3 = analogRead(A7);
        middle_a = (a1 < a2) ? ((a2 < a3) ? a2: ((a3 < a1) ? a1: a3)): ((a1 < a3) ? a1: ((a3 < a2) ? a2: a3));
        sum_a += middle_a;
        middle_b = (b1 < b2) ? ((b2 < b3) ? b2: ((b3 < b1) ? b1: b3)): ((b1 < b3) ? b1: ((b3 < b2) ? b2: b3));
        sum_b += middle_b;
        middle_c = (c1 < c2) ? ((c2 < c3) ? c2: ((c3 < c1) ? c1: c3)): ((c1 < c3) ? c1: ((c3 < c2) ? c2: c3));
        sum_c += middle_c;
    }
    sum_a = sum_a/4;
    avexp_a += (sum_a - avexp_a) / 5;
    sum_b = sum_b/4;
    avexp_b += (sum_b - avexp_b) / 5;
    sum_c = sum_c/4;
    avexp_c += (sum_c - avexp_c) / 5;
    Serial.print(avexp_c);
    Serial.print("");
    Serial.print(avexp_b);
    Serial.print("");
    Serial.print(avexp_c);

    delay(10);
}
 
