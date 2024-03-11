#ifndef SADDLE_POINTS_H
#define SADDLE_POINTS_H

#include <stdlib.h>
#include <stdint.h>

typedef struct saddle_point_t
{
    int row;
    int column;
} saddle_point_t;

typedef struct saddle_points_t
{
    int count;
    saddle_point_t points[];
} saddle_points_t;

saddle_points_t *saddle_points(uint8_t rows, uint8_t cols, uint8_t matrix[rows][cols]);
void free_saddle_points(saddle_points_t *saddle_points);

#endif
