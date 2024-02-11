#ifndef RATIONAL_NUMBERS_H
#define RATIONAL_NUMBERS_H

#include <math.h>
#include <stdlib.h>

typedef struct
{
    int numerator;
    int denominator;
} rational_t;

rational_t add(rational_t num1, rational_t num2);
rational_t subtract(rational_t num1, rational_t num2);
rational_t multiply(rational_t num1, rational_t num2);
rational_t divide(rational_t num1, rational_t num2);
rational_t absolute(rational_t num1);
rational_t exp_rational(rational_t num1, int power);
float exp_real(int num1, rational_t power);
rational_t reduce(rational_t num);
int greatest_common_denominator(int num1, int num2);

#endif
