#include <math.h>
#include <stdio.h>
#include <string.h>

typedef struct point {
    float x, y;
} Point;

//distance from 2 points
float dist(Point a, Point b) {
    return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y)* (b.y - a.y));
}

//comparing two floats
int equal(float a, float b) {
    float diff = a - b;
    float epsilon = 0.001;
    return (diff < epsilon && (-diff < epsilon));
}

//comparing two floats but with a larger error
int equal1(float a, float b) {
    float diff = a - b;
    float epsilon = 0.7;
    return (diff < epsilon && (-diff < epsilon));
}

int main() {

    //Change this values from 0 to 50:
    //Microphones
    Point mic1; mic1.x = 5; mic1.y = 21;
    Point mic2; mic2.x = 45; mic2.y = 45;
    Point mic3; mic3.x = 25; mic3.y = 5;

    //Source of sound
    Point source; source.x = 25; source.y = 25;

    //Camera
    Point cam; cam.x = 7; cam.y = 38;



    //printing given data
    for(float i = 0; i <= 50; i++) {
        for(float j = 0; j <= 50; j++) {
            if(equal(i, source.x) && equal(j, source.y)) {
                printf("S ");
            }
            else if(equal(i, mic1.x) && equal(j, mic1.y)) {
                printf("M ");
            }
            else if(equal(i, mic2.x) && equal(j, mic2.y)) {
                printf("M ");
            }
            else if(equal(i, mic3.x) && equal(j, mic3.y)) {
                printf("M ");
            }
            else if(equal(i, cam.x) && equal(j, cam.y)) {
                printf("C ");
            }
            else printf(". ");
        }
        printf("\n");
    }

    //calculating distances from each mic to source of sound
    float dist1 = dist(mic1, source);
    float dist2 = dist(mic2, source);
    float dist3 = dist(mic3, source);
    printf("\nDistances from Source of sound to mics:\nmic1: %f mic2: %f mic3: %f\n\n", dist(mic1, source), dist(mic2, source), dist(mic3, source));

    //triangulation
    float a = dist1, b = dist2, c = dist(mic1, mic2);
    float cosa = (a * a + c * c - b * b) / (2 * a * c);
    float sina = sqrt(1 - cosa * cosa);
    if(equal(cosa, 0) || equal(sina, 0)) {
        printf("AAAAAAAAAAAAAAAAAAAAAAAAA COS = 0 OR SIN = 0 AAAAAAAAAAAAAAAAAAAA"); //microphones and camera must not be at the same line
        return 0;
    }
    float x = mic1.x + (a / c) * (mic2.x - mic1.x) * cosa + (a / c) * (mic2.y - mic1.y) * sina;
    float y = mic1.y + (a / c) * (mic2.y - mic1.y) * cosa - (a / c) * (mic2.x - mic1.x) * sina;
    printf("Source coordinates:\n");
    printf("Answer: x = %f; y = %f\n", source.x, source.y);
    printf("Calculations: x = %f; y = %f\n\n", x, y);

    //calculating direction of camera (y = m * x + b)
    float m = (cam.x - x) / (cam.y - y);
    float c1 = cam.x - m * cam.y;
    float flag = 0;
    if(equal(cam.y - y, 0)) flag = 1; //if camera and source are at the same Y coordinates

    //printing result
    for(float i = 0; i <= 50; i++) {
        for(float j = 0; j <= 50; j++) {
            if(equal(i, x) && equal(j, y)) {
                printf("S ");
            }
            else if(equal(i, mic1.x) && equal(j, mic1.y)) {
                printf("M ");
            }
            else if(equal(i, mic2.x) && equal(j, mic2.y)) {
                printf("M ");
            }
            else if(equal(i, mic3.x) && equal(j, mic3.y)) {
                printf("M ");
            }
            else if(equal(i, cam.x) && equal(j, cam.y)) {
                printf("C ");
            }
            else if(flag == 1 && equal(j, cam.y)) {
                printf("* ");
            }
            else if(equal1(i, m * j + c1)) {
                printf("* ");
            }
            else printf(". ");
        }
        printf("\n");
    }
}
