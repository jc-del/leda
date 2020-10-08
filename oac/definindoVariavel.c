#include <stdio.h>
int main() {
    double x = 0.1;
    double y = 0;
    for ( int k = 0; k < 99; k++){
        /* code */
        y += x;
    }
    printf("%lf\n", y);
    return 0;
}
