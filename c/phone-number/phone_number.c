#include "phone_number.h"

const size_t MAX_NUM_LENGTH = 12;

char *phone_number_clean(const char *input)
{
    // Variables
    int curr_idx = 0;

    // Check the larger size
    char *clean_number;
    if (MAX_NUM_LENGTH > strlen(input) + 1)
    {
        clean_number = malloc(MAX_NUM_LENGTH * sizeof(char));
    }
    else
    {
        clean_number = malloc((strlen(input) + 1) * sizeof(char));
    }

    // Add all digits to the initialized clean_number variable
    for (int i = 0, l = strlen(input); i < l; i++)
    {
        if (isdigit(input[i]))
        {
            clean_number[curr_idx++] = input[i];
        }
    }

    // Add a null terminator to clean_number
    clean_number[curr_idx] = '\0';

    // If length is not valid, do not continue.
    if (strlen(clean_number) < 10 || strlen(clean_number) > 11)
    {
        return invalid_number(clean_number);
    }

    // If length is 11, adjust.
    if (strlen(clean_number) == 11)
    {
        if (clean_number[0] == '1')
        {
            memmove(&clean_number[0], &clean_number[1], strlen(clean_number));
        }
        else
        {

            return invalid_number(clean_number);
        }
    }
    // Check the area code
    if (clean_number[0] == '0' || clean_number[0] == '1')
    {
        return invalid_number(clean_number);
    }

    // Check the exchange code
    if (clean_number[3] == '0' || clean_number[3] == '1')
    {
        return invalid_number(clean_number);
    }

    return clean_number;
}

char *invalid_number(char *invalid_number)
{
    free(invalid_number);
    char *temp = malloc((strlen(INVALID_NUMBER) + 1) * sizeof(char));
    strcpy(temp, INVALID_NUMBER);
    return temp;
}
