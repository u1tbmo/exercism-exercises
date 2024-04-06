#ifndef PASCALS_TRIANGLE_H
#define PASCALS_TRIANGLE_H

#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

// Frees the triangle
void free_triangle(uint8_t **triangle, size_t rows);

// Creates the triangle
uint8_t **create_triangle(size_t rows);

#endif
