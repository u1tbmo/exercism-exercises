#include "reverse_string.h"

char *reverse(const char *value)
{
    // Get the length of the string
    int length = strlen(value);

    // Allocate memory for a new string
    char *new_string = malloc(length * sizeof(char));
    if (new_string == NULL)
    {
        return NULL;
    }

    // Iterate through the original string in reverse.
    for (int i = length - 1, j = 0; i >= 0; i--, j++)
    {
        new_string[j] = value[i];
    }

    return new_string;
}