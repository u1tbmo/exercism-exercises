#include "rational_numbers.h"

rational_t add(rational_t num1, rational_t num2)
{
    rational_t result;
    result.numerator = num1.numerator * num2.denominator + num2.numerator * num1.denominator;
    result.denominator = num1.denominator * num2.denominator;
    return reduce(result);
}

rational_t subtract(rational_t num1, rational_t num2)
{
    rational_t result;
    result.numerator = num1.numerator * num2.denominator - num2.numerator * num1.denominator;
    result.denominator = num1.denominator * num2.denominator;
    return reduce(result);
}

rational_t multiply(rational_t num1, rational_t num2)
{
    rational_t result;
    result.numerator = num1.numerator * num2.numerator;
    result.denominator = num1.denominator * num2.denominator;
    return reduce(result);
}

rational_t divide(rational_t num1, rational_t num2)
{
    rational_t result;
    result.numerator = num1.numerator * num2.denominator;
    result.denominator = num1.denominator * num2.numerator;
    return reduce(result);
}

rational_t absolute(rational_t num1)
{
    rational_t result;
    result.numerator = abs(num1.numerator);
    result.denominator = abs(num1.denominator);
    return reduce(result);
}

rational_t exp_rational(rational_t num, int power)
{
    rational_t result;
    result.numerator = (power > 0) ? pow(num.numerator, power) : pow(num.denominator, abs(power));
    result.denominator = (power > 0) ? pow(num.denominator, power) : pow(num.numerator, abs(power));
    return reduce(result);
}

float exp_real(int num, rational_t power)
{
    return pow(num, (double)power.numerator / (double)power.denominator);
}

rational_t reduce(rational_t num)
{
    rational_t result;
    if (num.numerator == 0)
    {
        result.numerator = 0;
        result.denominator = 1;
        return result;
    }
    int gcd = greatest_common_denominator(num.numerator, num.denominator);
    result.numerator = (num.denominator > 0) ? num.numerator / gcd : -num.numerator / gcd;
    result.denominator = (num.denominator > 0) ? num.denominator / gcd : -num.denominator / gcd;
    return result;
}

int greatest_common_denominator(int num1, int num2)
{
    int result;

    num1 = (num1 > 0) ? num1 : -num1;
    num2 = (num2 > 0) ? num2 : -num2;

    for (int i = 1; i <= num1 && i <= num2; i++)
    {
        if (num1 % i == 0 && num2 % i == 0)
        {
            result = i;
        }
    }
    return result;
}
