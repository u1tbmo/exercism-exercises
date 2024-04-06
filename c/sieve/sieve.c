#include "sieve.h"

uint32_t sieve(uint32_t limit, uint32_t *primes, size_t max_primes)
{
    // Variables
    int composite_qty = 0;
    size_t primes_count;

    // Create a 2d array that holds the numbers from [2, limit] and their "mark"
    uint32_t **array = malloc(2 * sizeof(uint32_t *));
    array[0] = malloc((limit - 1) * sizeof(uint32_t));
    array[1] = malloc((limit - 1) * sizeof(uint32_t));

    // Enter all numbers from 2 to limit and set them as unmarked
    for (uint32_t number = 2, i = 0; number <= limit; number++, i++)
    {
        array[0][i] = number;
    }
    for (uint32_t i = 0; i < limit - 1; i++)
    {
        array[1][i] = 0;
    }

    // Find all unmarked numbers and mark their multiples
    for (uint32_t i = 0; i < limit - 1; i++)
    {
        for (uint32_t j = i + array[0][i]; j < limit - 1; j += array[0][i])
        {
            if (array[1][j] == 0)
            {
                array[1][j] = 1;
                composite_qty++;
            }
        }
    }

    // Copy all primes to the `primes` array
    for (uint32_t i = 0, j = 0; i < limit - 1; i++)
    {
        if (array[1][i] == 0)
        {
            primes[j++] = array[0][i];
        }
    }

    primes_count = limit - 1 - composite_qty;

    // Free memory
    free(array[0]);
    free(array[1]);
    free(array);

    // Using the indirect method: Set of Numbers - Set of Composites = Set of Primes
    return (max_primes > primes_count) ? primes_count : max_primes;
}
