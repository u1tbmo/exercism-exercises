#include "armstrong_numbers.h"
#include <stdio.h>
#include <math.h>

bool is_armstrong_number(int number) {
    int sum = 0;
    int temp = number;
    int digits = 0;
    while (temp > 0) { // removes the last digit of temp (the number)
        digits++;
        temp /= 10;
    }
    temp = number;
    while (temp > 0) {
        sum += pow(temp % 10, digits); // temp % 10 gets the last digit of temp
        temp /= 10; // removes the last digit of temp
    }
    return number == sum;
}
