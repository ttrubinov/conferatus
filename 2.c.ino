static int a5, a6, a, b, c, middle, eee, lll;
static int sum=0;
static int a5f = 0, a6f = 0, a7f = 0;

void setup() {
    Serial.begin(9600);
}
 
void loop() {
    sum = 0;
    for (int i=0; i<4; i++){
        a = analogRead(A7);
        b = analogRead(A7);
        c = analogRead(A7);
        
//        a -= 250;
//        
//        if (a < 0) {
//          a = -a;
//        }
//    
//        b -= 250;
//        if (b < 0) {
//          b = -b;
//        }
//    
//    
//        c -= 250;
//        if (c < 0) {
//          c = -c;
//        }
        
        middle = (a < b) ? ((b < c) ? b : ((c < a) ? a : c)) : ((a < c) ? a : ((c < b) ? b : c));
        sum+=middle;
        lll += (a - lll) / 5;
        lll += (b - lll) / 5;
        lll += (c - lll) / 5;
    }

    sum = sum >> 2; // "/4"
    
    eee += (sum - eee) / 5;

//    Serial.print(lll);
//    Serial.print(" ");
    Serial.println(eee);

    delay(10);
}
 
