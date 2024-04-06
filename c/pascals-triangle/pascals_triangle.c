#include "pascals_triangle.h"

uint8_t **create_triangle(size_t rows)
{
    // If rows == 0, create a triangle with 0 as the value
    if (rows == 0)
    {
        uint8_t **triangle = malloc(sizeof(uint8_t *));
        if ((triangle == NULL))
        {
            return NULL;
        }

        triangle[0] = malloc(sizeof(uint8_t));
        if (triangle[0] == NULL)
        {
            free(triangle);
            return NULL;
        }

        triangle[0][0] = 0;
        return triangle;
    }

    // Allocate memory for a triangle
    uint8_t **triangle = malloc(rows * sizeof(uint8_t *));
    if (triangle == NULL)
    {
        return NULL;
    }

    // Make rows
    for (size_t i = 0; i < rows; i++)
    {
        // Allocate memory for a dynamic array
        triangle[i] = malloc(rows * sizeof(uint8_t));
        if (triangle[i] == NULL)
        {
            // If malloc failed, free all arrays in the triangle then free the triangle
            for (size_t j = 0; j < i; j++)
            {
                free(triangle[j]);
            }
            free(triangle);
            return NULL;
        }

        // Fill the array
        for (size_t j = 0; j < rows; j++)
        {
            // The top of the pyramid is always 1
            if (i == 0)
            {
                if (j == 0)
                {
                    triangle[i][j] = 1;
                }
                else if (j > 0)
                {
                    triangle[i][j] = 0;
                }
            }
            else
            {
                // The left side of the triangle is always a 1
                if (j == 0)
                {
                    triangle[i][j] = 1;
                }
                // Compute for the value in the current place based on the row above
                else
                {
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
                }
            }
        }
    }

    return triangle;
}

void free_triangle(uint8_t **triangle, size_t rows)
{
    // Free every array in triangle
    for (size_t i = 0; i < rows; i++)
    {
        free(triangle[i]);
    }
    // Free the triangle itself
    free(triangle);
}