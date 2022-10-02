#include <math.h>
#include <stdio.h>
#include <string.h>

typedef struct point {
    double x, y;
} Point;

//distance from 2 points
double dist(Point a, Point b) {
    return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y)* (b.y - a.y));
}

//comparing two doubles
int equal(double a, double b) {
    double diff = a - b;
    double epsilon = 0.001;
    return (diff < epsilon && (-diff < epsilon));
}

//comparing two doubles but with a larger error
int equal1(double a, double b) {
    double diff = a - b;
    double epsilon = 0.7;
    return (diff < epsilon && (-diff < epsilon));
}

int main() {
    //you can change .x values from 0 to 50 and .y values from 36 to 50
    Point mic1; mic1.x = 20; mic1.y = 45;
    Point mic2; mic2.x = 30; mic2.y = 45;
    Point mic3; mic3.x = 25; mic3.y = 37;

    //you can change .x values from 0 to 50 and .y values from 0 to 34
    Point source; source.x = 30; source.y = 7;

    //you can change .x and .y values from 0 to 50
    Point cam; cam.x = 7; cam.y = 38;



    //printing given data
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
            else if(equal(j, 35)) {
                printf("| ");
            }
            else printf(". ");
        }
        printf("\n");
    }

    //calculating distances from each mic to source of sound
    double dist1 = dist(mic1, source);
    double dist2 = dist(mic2, source);
    double dist3 = dist(mic3, source);
    printf("\nDistances from Source of sound to mics:\nmic1: %lf mic2: %lf mic3: %lf\n\n", dist(mic1, source), dist(mic2, source), dist(mic3, source));

    //triangulation
    double a = dist1, b = dist2, c = dist(mic1, mic2);
    double cosa = (a * a + c * c - b * b) / (2 * a * c);
    double sina = sqrt(1 - cosa * cosa);
    if(equal(cosa, 0) || equal(sina, 0)) {
        printf("AAAAAAAAAAAAAAAAAAAAAAAAA COS = 0 OR SIN = 0 AAAAAAAAAAAAAAAAAAAA"); //microphones and camera must not be at the same line
        return 0;
    }
    double x = mic1.x + (a / c) * (mic2.x - mic1.x) * cosa - (a / c) * (mic2.y - mic1.y) * sina;
    double y = mic1.y + (a / c) * (mic2.y - mic1.y) * cosa - (a / c) * (mic2.x - mic1.x) * sina;
    printf("Source coordinates:\n");
    printf("Answer: x = %lf; y = %lf\n", source.x, source.y);
    printf("Calculations: x = %lf; y = %lf\n\n", x, y);

    //calculation of the line along which camera should be directed (y = m * x + b)
    double m = (cam.x - source.x) / (cam.y - source.y);
    double c1 = cam.x - m * cam.y;
    double flag = 0;
    if(equal(cam.y - source.y, 0)) flag = 1; //if camera and source are at the same Y coordinates

    //printing result
    for(double i = 0; i <= 50; i++) {
        for(double j = 0; j <= 50; j++) {
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
            else if(equal(j, 35)) {
                printf("| ");
            }
            else printf(". ");
        }
        printf("\n");
    }
}
