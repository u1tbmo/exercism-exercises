#ifndef PYTHAGOREAN_TRIPLET_H
#define PYTHAGOREAN_TRIPLET_H

#include <stdlib.h>

typedef struct
{
    int a;
    int b;
    int c;
} triplet_t;

typedef struct
{
    triplet_t *triplets;
    int count;
} triplets_t;

triplets_t *triplets_with_sum(int sum);
void free_triplets(triplets_t *triplets_struct);

#endif
