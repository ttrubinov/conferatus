#include <math.h>

typedef struct point {
    float x, y;
} Point;

Point add(Point a, Point b) {
    return (Point) {a.x + b.x, a.y + b.y};
}

Point mult(Point a, float b) {
    return (Point) {a.x * b, a.y * b};
}

void printPoint(Point a) {
    printf("%f %f\n", a.x, a.y);
}

typedef struct circle {
    Point o;
    float rad;
} Circle;

typedef struct line {
    float a, b, c;
} Line;

int compare (const void * a, const void * b)
{
  float fa = *(const float*) a;
  float fb = *(const float*) b;
  return (fa > fb) - (fa < fb);
}

float distance(Point a, Point b) {
    return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y)* (b.y - a.y));
}

int equal(float a, float b) {
    float diff = a - b;
    float epsilon = 0.001;
    return (diff < epsilon && (-diff < epsilon));
}

int equalE(float a, float b, float epsilon) {
    float diff = a - b;
    return (diff < epsilon && (-diff < epsilon));
}

float getValue(Point a, Point b) {
    float k = 10000 + (float)rand() / RAND_MAX * 300;
    return k / (distance(a, b) * distance(a, b)) + ((float)rand() / RAND_MAX -0.5) * 0.1;
}

Circle calcCircle(Point s0, Point s1, float k) {
    float x1 = s1.x - s0.x;
    float y1 = s1.y - s0.y;
    float xk1 = x1 / (k * k - 1);
    float yk1 = y1 / (k * k - 1);
    Circle circle;
    circle.o.x = -xk1 + s0.x;
    circle.o.y = -yk1 + s0.y;
    circle.rad = xk1 * xk1 + xk1 * x1 + yk1 * yk1 + yk1 * y1;
    return circle;
}

Point circleIntersection(Circle c1, Circle c2) {
    float x2 = c2.o.x - c1.o.x, y2 = c2.o.y - c1.o.y;
    float a = -2 * x2, b = -2 * y2, c = x2 * x2 + y2 * y2 + c1.rad - c2.rad, r = c1.rad;
    float a2b2 = a * a + b * b;
    float x0 = -a * c / (a2b2),  y0 = -b * c / (a2b2);
    if(c * c > r * (a2b2) + 0.5)
        return (Point) {-100, -100};
    else if(abs(c * c - r * (a2b2)) < 0.5) {
        return (Point) {x0 + c1.o.x, y0 + c1.o.y};
    }
    else {
        float d = r - c * c / (a2b2);
        float mult = sqrt(d / (a2b2));
        float ax, ay, bx, by;
        ax = x0 + b * mult;
        bx = x0 - b * mult;
        ay = y0 - a * mult;
        by = y0 + a * mult;
        if(ay > by)
            return (Point) {ax + c1.o.x, ay + c1.o.y};
        else
            return (Point) {bx + c1.o.x, by + c1.o.y};
    }
}

int pointOnLine(Point p, Line l) {
    equalE(l.a * (p.x) + l.b * (p.y) + l.c, 0, (l.a + l.b) / 2 + 1);
}

int pointOnCircle(Point p, Circle c) {
    equalE((p.x - c.o.x) * (p.x - c.o.x) + (p.y - c.o.y) * (p.y - c.o.y) - c.rad, 0, sqrt(c.rad));
}

Line midperpendicular(Point a, Point b) {
    float x = -a.x + b.x, y = -a.y + b.y;
    return (Line) {2 * x, 2 * y, -(2 * x * a.x + 2 * y * a.y) - x * x - y * y};
}

Point triangulation(Point a, Point b, Point c, float sa, float sb, float sc) {
    float k1 = sqrt(sa / sb);
    if(equalE(k1, 1, 0.1)) {
        Line line = midperpendicular(a, b);
    }
    Circle c1 = calcCircle(a, b, k1);
    float k2 = sqrt(sa / sb);
    if(equalE(k2, 1, 0.1)) {
        Line line = midperpendicular(b, c);
    }
    Circle c2 = calcCircle(b, c, k2);
    return (Point) circleIntersection(c1, c2);
}
