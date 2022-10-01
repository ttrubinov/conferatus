#include <math.h>
#include <stdio.h>
#include <string.h>

typedef struct point {
    double x, y;
} Point;

double dist(Point a, Point b) {
    return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y)* (b.y - a.y));
}

double triang(double a, double b, double angle) {
    return sqrt(a * a + b * b - 2 * a * b * angle);
}

int equal(double a, double b) {
    double diff = a - b;
    double epsilon = 0.0000001;
    return (diff < epsilon && (-diff < epsilon));
}

int equal1(double a, double b) {
    double diff = a - b;
    double epsilon = 0.7;
    return (diff < epsilon && (-diff < epsilon));
}

int main() {
    Point mic1; mic1.x = 15; mic1.y = 30;
    Point mic2; mic2.x = 25; mic2.y = 30;
    Point mic3; mic3.x = 20; mic3.y = 22;
    Point source; source.x = 37; source.y = 3;
    Point cam; cam.x = 3; cam.y = 23;




    for(double i = 0; i <= 50; i++) {
        for(double j = 0; j <= 50; j++) {
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
    double dist1 = dist(mic1, source);
    double dist2 = dist(mic2, source);
    double dist3 = dist(mic3, source);
    printf("\nDistances from Source of sound to mics:\nmic1: %lf mic2: %lf mic3: %lf\n\n", dist(mic1, source), dist(mic2, source), dist(mic3, source));
    double a = dist1, b = dist2, c = dist(mic1, mic2);
    double cosa = (a * a + c * c - b * b) / (2 * a * c);
    double sina = sqrt(1 - cosa * cosa);
    double x = mic1.x + (a / c) * (mic2.x - mic1.x) * cosa - (a / c) * (mic2.y - mic1.y) * sina;
    double y = mic1.y + (a / c) * (mic2.y - mic1.y) * cosa - (a / c) * (mic2.x - mic1.x) * sina;
    printf("Source coordinates:\n");
    printf("Answer: x = %lf; y = %lf\n", source.x, source.y);
    printf("Calculations: x = %lf; y = %lf\n\n", x, y);
    double m = (cam.x - source.x) / (cam.y - source.y);
    double c1 = cam.x - m * cam.y;
    for(double i = 0; i <= 40; i++) {
        for(double j = 0; j <= 40; j++) {
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
            else if(equal1(i, m * j + c1)) {
                printf("* ");
            }
            else printf(". ");
        }
        printf("\n");
    }
}
