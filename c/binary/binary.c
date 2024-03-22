#include "binary.h"

int convert(const char *input)
{
    int decimal = 0, digit, length;

    length = strlen(input);

    for (int i = length - 1, base = 0; i >= 0; i--, base++)
    {

        if (!(input[i] == '0' || input[i] == '1'))
        {
            return INVALID;
        }
        else
        {
            digit = input[i] - '0'; // convert the char to an integer
            decimal += digit * pow(2, base);
        }
    }

    return decimal;
}
