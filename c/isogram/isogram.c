#include "isogram.h"
#include <string.h>
#include <ctype.h>
#include <stdio.h>

bool is_isogram(const char phrase[])
{
    if (phrase == NULL)
    {
        return false;
    }

    // Create an integer array storing the frequency in the phrase
    int freq[26] = {0};
    for (int i = 0, length = strlen(phrase); i < length; i++)
    {
        if (isalpha(phrase[i]))
        {
            int index = tolower(phrase[i]) - 'a';
            if (freq[index] == 1)
            {
                return false; // return false if there is already one occurence
            }
            else
            {
                freq[index] += 1; // update the frequency array
            }
        }
    }
    return true; // return true if we did not find a double occurence of a letter
}