#include "pythagorean_triplet.h"

/* https://stackoverflow.com/a/61756590
    a + b + c = n
    b = n - a - c

    c^2 - b^2 = a^2
    c^2 - (N - a - c)^2 = a^2
    c^2 - (n - a - c)^2 = a^2
    c^2 - (n - a - c) * (n - a - c) = a^2
    c^2 - n(n - a - c) + a(n - a - c) + c(n - a - c) = a^2
    c^2 - n^2 + an + nc + an - a^2 - ac + cn - ac - c^2 = a^2
    -n^2 + 2an + 2nc - a^2 - 2ac = a^2
    -n^2 + 2an + 2nc - 2a^2 - 2ac = 0
    2c(n - a) = n^2 - 2an + 2a^2
    c = (n^2 - 2an + 2a^2) / 2(n - a)
*/
triplets_t *triplets_with_sum(int sum)
{

    int numerator, denominator, b, c;

    triplets_t *result = malloc(sizeof(triplets_t)); // Allocate memory for the result
    triplet_t *solution = malloc(sizeof(triplet_t)); // Allocate memory for a single solution

    result->count = 0;       // Set count to 0
    result->triplets = NULL; // Set triplets to NULL for now.

    // Iterate through possible values of a (1 to sum-1)
    for (int a = 1; a < sum; a++)
    {
        // Calculate the numerator and denominator of the fraction equalling c
        numerator = (sum * sum) - (2 * a * sum) + (2 * a * a);
        denominator = 2 * (sum - a);

        // We cannot divide by 0 and c must be an integer.
        if (denominator > 0 && numerator % denominator == 0)
        {
            c = numerator / denominator; // Integer division.
            b = sum - a - c;             // According to formula.

            // The triplet must be ascending in order.
            if (b > a)
            {
                // There is a solution
                solution->a = a;
                solution->b = b;
                solution->c = c;

                // Reallocate memory of triplets pointer
                result->triplets = realloc(result->triplets, sizeof(triplet_t) * (result->count + 1));
                if (result->triplets == NULL)
                {
                    return NULL;
                }

                // Add the solution and increment count
                result->triplets[result->count] = *solution;
                result->count++;
            }
        }
    }

    free(solution);
    return result;
}

void free_triplets(triplets_t *triplets_struct)
{
    free(triplets_struct->triplets);
    free(triplets_struct);
}