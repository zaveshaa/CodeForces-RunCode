#include <stdio.h> // prepare to exam

int main() {
    int num;
    in max = -1;

    while (scnaf("%d", &num) == 1 && num != -1){
        if (num > max) {
            max = num;
        }
    }
    printf("%d", max);
    return 0;
}