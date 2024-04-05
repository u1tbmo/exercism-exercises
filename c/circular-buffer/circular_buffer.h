#ifndef CIRCULAR_BUFFER_H
#define CIRCULAR_BUFFER_H

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

typedef int buffer_value_t;
typedef struct circular_buffer_t
{
    buffer_value_t *elements;
    int head, tail, entry_qty, capacity;

} circular_buffer_t;

// Creates a new circular buffer
circular_buffer_t *new_circular_buffer(int capacity);

// Writes a value to a circular buffer
int write(circular_buffer_t *buffer, buffer_value_t value);

// Writes a value to a circular buffer, overwriting a value
int overwrite(circular_buffer_t *buffer, buffer_value_t value);

// Reads a value from a circular buffer
int read(circular_buffer_t *buffer, buffer_value_t *value);

// Clears a buffer
void clear_buffer(circular_buffer_t *buffer);

// Deletes a buffer
void delete_buffer(circular_buffer_t *buffer);

// Checks if a buffer is full
int buffer_empty(circular_buffer_t *buffer);

// Checks if a buffer is empty
int buffer_full(circular_buffer_t *buffer);

#endif
