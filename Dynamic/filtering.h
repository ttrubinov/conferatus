#include <math.h>
#include <set>

using namespace std;

void filteringMediana(float *mic1Sound, float *mic2Sound, float *mic3Sound, float *mic4Sound, Point source, Point mic1, Point mic2, Point mic3, Point mic4) {
    float avg1 = 0, avg2 = 0, avg3 = 0, avg4 = 0;
    int n = 20;
    multiset<float> avg1Arr, avg2Arr, avg3Arr, avg4Arr;
    for(int i = 0; i < n; i++) {
        avg1Arr.insert(getValue(source, mic1));
        avg2Arr.insert(getValue(source, mic2));
        avg3Arr.insert(getValue(source, mic3));
        avg4Arr.insert(getValue(source, mic4));
    }
    for(int i = 9; i <= 11; i++) {
        avg1 += *next(avg1Arr.begin(), i);
        avg2 += *next(avg2Arr.begin(), i);
        avg3 += *next(avg3Arr.begin(), i);
        avg4 += *next(avg4Arr.begin(), i);
    }
    avg1 /= 3;
    avg2 /= 3;
    avg3 /= 3;
    avg4 /= 3;
    *mic1Sound = avg1;
    *mic2Sound = avg2;
    *mic3Sound = avg3;
    *mic4Sound = avg4;
}

void filteringAvg(float *mic1Sound, float *mic2Sound, float *mic3Sound, float *mic4Sound, Point source, Point mic1, Point mic2, Point mic3, Point mic4) {
    float avg1 = 0, avg2 = 0, avg3 = 0, avg4 = 0;
    int n = 20;
    float avg1Arr[n], avg2Arr[n], avg3Arr[n], avg4Arr[n];
    for(int i = 0; i < n; i++) {
        avg1 += getValue(source, mic1);
        avg2 += getValue(source, mic2);
        avg3 += getValue(source, mic3);
        avg4 += getValue(source, mic4);
    }
    avg1 /= n;
    avg2 /= n;
    avg3 /= n;
    avg4 /= n;
    *mic1Sound = avg1;
    *mic2Sound = avg2;
    *mic3Sound = avg3;
    *mic4Sound = avg4;
}

void filteringRunningAvg(float *mic1Sound, float *mic2Sound, float *mic3Sound, float *mic4Sound, Point source, Point mic1, Point mic2, Point mic3, Point mic4) {
    float avg1 = 0, avg2 = 0, avg3 = 0, avg4 = 0;
    float newAvg1 = 0, newAvg2 = 0, newAvg3 = 0, newAvg4 = 0;
    int n = 20;
    float k = 0.01;
    for(int i = 0; i < n; i++) {
        avg1 += (getValue(source, mic1) - avg1) * k;
        avg2 += (getValue(source, mic2) - avg2) * k;
        avg3 += (getValue(source, mic3) - avg3) * k;
        avg4 += (getValue(source, mic4) - avg4) * k;
    }
    *mic1Sound = avg1;
    *mic2Sound = avg2;
    *mic3Sound = avg3;
    *mic4Sound = avg4;
}

float median1(float newVal) {
    static float buf1[3];
    static byte count1 = 0;
    if (++count1 >= 3) count1 = 0;
    return (max(buf1[0], buf1[1]) == max(buf1[1], buf1[2])) ? max(buf1[0], buf1[2]) : max(buf1[1], min(buf1[0], buf1[2]));
}

float median2(float newVal) {
    static float buf2[3];
    static byte count2 = 0;
    if (++count2 >= 3) count2 = 0;
    return (max(buf2[0], buf2[1]) == max(buf2[1], buf2[2])) ? max(buf2[0], buf2[2]) : max(buf2[1], min(buf2[0], buf2[2]));
}

float median3(float newVal) {
    static float buf3[3];
    static byte count3 = 0;
    if (++count3 >= 3) count3 = 0;
    return (max(buf3[0], buf3[1]) == max(buf3[1], buf3[2])) ? max(buf3[0], buf3[2]) : max(buf3[1], min(buf3[0], buf3[2]));
}

float median4(float newVal) {
    static float buf4[3];
    static byte count4 = 0;
    if (++count4 >= 3) count4 = 0;
    return (max(buf4[0], buf4[1]) == max(buf4[1], buf4[2])) ? max(buf4[0], buf4[2]) : max(buf4[1], min(buf4[0], buf4[2]));
}


void filteringMedianRunningAvg(float *mic1Sound, float *mic2Sound, float *mic3Sound, float *mic4Sound, Point source, Point mic1, Point mic2, Point mic3, Point mic4) {
    float avg1 = 0, avg2 = 0, avg3 = 0, avg4 = 0;
    float newAvg1 = 0, newAvg2 = 0, newAvg3 = 0, newAvg4 = 0;
    int n = 20;
    float k = 0.01;
    for(int i = 0; i < n; i++) {
        avg1 = median1(getValue(source, mic1));
        avg2 = median2(getValue(source, mic2));
        avg3 = median3(getValue(source, mic3));
        avg4 = median4(getValue(source, mic4));
    }
    *mic1Sound = avg1;
    *mic2Sound = avg2;
    *mic3Sound = avg3;
    *mic4Sound = avg4;
}
