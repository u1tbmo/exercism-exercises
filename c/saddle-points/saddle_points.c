#include "saddle_points.h"

saddle_points_t *saddle_points(uint8_t rows, uint8_t cols, uint8_t matrix[rows][cols])
{
    // Transpose the matrix
    uint8_t transpose[cols][rows];
    for (uint8_t i = 0; i < rows; i++)
    {
        for (uint8_t j = 0; j < cols; j++)
        {
            transpose[j][i] = matrix[i][j];
        }
    }

    int row_best[cols], col_best[rows], max, min;
    // Calculate maximum and minimum of each row and column
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (j == 0 || matrix[i][j] > max)
            {
                max = matrix[i][j];
            }
        }
        row_best[i] = max;
    }

    for (int i = 0; i < cols; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            if (j == 0 || transpose[i][j] < min)
            {
                min = transpose[i][j];
            }
        }
        col_best[i] = min;
    }

    // Solution
    saddle_points_t *solutions = malloc(sizeof(saddle_points_t) + sizeof(saddle_point_t) * rows * cols);
    solutions->count = 0;

    saddle_point_t *point = malloc(sizeof(saddle_point_t)); // Create a temporary saddle point which stores a single solution to the grid

    for (uint8_t i = 0; i < rows; i++)
    {
        for (uint8_t j = 0; j < cols; j++)
        {
            if (row_best[i] == col_best[j])
            {
                // Set the saddle point's row and column to the current indexes.
                point->row = i + 1;
                point->column = j + 1;

                // Add the saddle point to the solution's points
                solutions->points[solutions->count] = *point;
                solutions->count++;
            }
        }
    }
    // Shrink memory to actual size
    solutions = realloc(solutions, sizeof(saddle_points_t) + sizeof(saddle_point_t) * solutions->count);

    free(point);
    return solutions;
}

void free_saddle_points(saddle_points_t *saddle_points)
{
    free(saddle_points);
}