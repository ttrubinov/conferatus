#ifndef UNICODE
#define UNICODE
#define UNICODE_WAS_UNDEFINED
#endif
#include <tchar.h>
#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <chrono>
#include <thread>

#include "maths.h"
#include "window.h"

float min(float a, int b) {
    if(a < (float) b) return a;
    return b;
}

float max(float a, int b) {
    if(a > (float) b) return a;
    return b;
}

using namespace std;

int main() {
    int windowScale = 2;
	int width = 120 * windowScale;
	int height = 30 * windowScale;
	float aspect = (float)width / height;
	float pixelAspect = 11.0f / 24.0f;
	float rt = aspect * pixelAspect;

	wchar_t* screen = new wchar_t[width * height];
	HANDLE hConsole = CreateConsoleScreenBuffer(GENERIC_READ | GENERIC_WRITE, 0, NULL, CONSOLE_TEXTMODE_BUFFER, NULL);
	SetConsoleActiveScreenBuffer(hConsole);
	DWORD dwBytesWritten = 0;

	srand(time(NULL));

	Point mic1 = {100, 5};
    Point mic2 = {110, 10};
    Point mic3 = {120, 5};
    Point mic4 = {130, 10};
    Point source; source.x = 100; source.y = 50;

	for (int t = 0; t < 10000; t++) {
        if(t % 100 < 50) {
            int f = 39;
            source.x += (rand() % f) - (f / 2);
            source.y += (rand() % f) - (f / 2);
            source.x = max(min(source.x, width - 5), 10);
            source.y = max(min(source.y, height * rt - 5), 15);
        }
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
        float mic1Sound = avg1, mic2Sound = avg2, mic3Sound = avg3, mic4Sound = avg4;
        Line line = midperpendicular(mic1, mic2);
        Circle circ1 = calcCircle(mic1, mic2, sqrt(mic1Sound / mic2Sound));
        Circle circ2 = calcCircle(mic2, mic3, sqrt(mic2Sound / mic3Sound));
        Circle circ3 = calcCircle(mic3, mic4, sqrt(mic3Sound / mic4Sound));

        float cnt = 0;
        Point circ12 = circleIntersection(circ1, circ2);
        if(circ12.x > -20.0 && circ12.x < width && circ12.y < height * rt) cnt++;
        else {
            circ12 = mult(circ12, 0.0);
        }
        Point circ23 = circleIntersection(circ2, circ3);
        if(circ23.x > -20.0 && circ23.x < width && circ23.y < height * rt) cnt++;
        else {
            circ23 = mult(circ23, 0.0);
        }
        Point circ13 = circleIntersection(circ1, circ3);
        if(circ13.x > -20.0 && circ13.x < width && circ13.y < height * rt) cnt++;
        else {
            circ13 = mult(circ13, 0.0);
        }
        Point mySource;
        if(cnt == 3) {
            Point p1 = circ23;
            Point p2 = circ13;
            Point p3 = circ12;
            float d1 = distance(p2, p3);
            float d2 = distance(p1, p3);
            float d3 = distance(p1, p2);
            float k1 = 1 / d1, k2 = 1 / d2, k3 = 1 / d3;
            mySource = (Point) {((k2 + k3) * p1.x + (k1 + k3) * p2.x + (k1 + k2) * p3.x) / (2 * (k1 + k2 + k3)),
                                ((k2 + k3) * p1.y + (k1 + k3) * p2.y + (k1 + k2) * p3.y) / (2 * (k1 + k2 + k3))};
        }
        else {
            mySource = mult(add(add(circ12, circ23), circ13), (1.0 / cnt));
        }
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
			    if((equal(i, source.x) && equalE(j * rt, source.y, 1)) && (equalE(i, mySource.x, 0.5) && equalE(j * rt, mySource.y, 1))) {
			        screen[i + j * width] = '@';
			    }
                else if(equal(i, source.x) && equalE(j * rt, source.y, 1)) {
                    screen[i + j * width] = 'S';
                }
                else if(equalE(i, mySource.x, 0.5) && equalE(j * rt, mySource.y, 1)) {
                    screen[i + j * width] = '&';
                }
                else if(equalE(i, mySource.x, 0.5) && equalE(j * rt, mySource.y, 0.5)) {
                    screen[i + j * width] = '&';
                }
                else if(equal(i, mic1.x) && equalE(j * rt, mic1.y, 1)) {
                    screen[i + j * width] = '1';
                }
                else if(equal(i, mic2.x) && equalE(j * rt, mic2.y, 1)) {
                    screen[i + j * width] = '2';
                }
                else if(equal(i, mic3.x) && equalE(j * rt, mic3.y, 1)) {
                    screen[i + j * width] = '3';
                }
                else if(equal(i, mic4.x) && equalE(j * rt, mic4.y, 1)) {
                    screen[i + j * width] = '4';
                }
                else if(i == 0 || j == 0 || equal(i, width - 4) || equal(j, height - 1)) {
                    screen[i + j * width] = '.';
                }
                /*else if(pointOnCircle((Point) {i, j * rt}, circ1)) {
                    screen[i + j * width] = '`';
                }
                else if(pointOnCircle((Point) {i, j * rt}, circ2)) {
                    screen[i + j * width] = '~';
                }
                else if(pointOnCircle((Point) {i, j * rt}, circ3)) {
                    screen[i + j * width] = '^';
                }*/
                else
                    screen[i + j * width] = ' ';
			}
		}
		char s1[60];
		char s2[60];
		char s3[60];
		sprintf(s1, "mySource coords: %f %f %f", mySource.x, mySource.y, cnt);
		sprintf(s2, "micsSound: %f %f %f %f", mic1Sound, mic2Sound, mic3Sound, mic4Sound);
		sprintf(s3, "Pogreshnost: %f", distance(source, mySource) / ((distance(source, mic1) + distance(source, mic2) + distance(source, mic3) + distance(source, mic4)) / 4) * 100);
        s1[strlen(s1)] = '\0';
        s2[strlen(s2)] = '\0';
        s3[strlen(s3)] = '\0';
        for(int pr = 0; pr < strlen(s1); pr++)
            screen[170 + 55 * width + pr] = s1[pr];
        for(int pr = 0; pr < strlen(s2); pr++)
            screen[170 + 56 * width + pr] = s2[pr];
        for(int pr = 0; pr < strlen(s3); pr++)
            screen[170 + 57 * width + pr] = s3[pr];
		screen[width * height - 1] = '\0';
		WriteConsoleOutputCharacter(hConsole, screen, width * height, { 0, 0 }, &dwBytesWritten);
		this_thread::sleep_for(chrono::milliseconds(300));
	}
}

#ifdef UNICODE_WAS_UNDEFINED
#undef UNICODE
#endif
