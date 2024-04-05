#include "circular_buffer.h"

circular_buffer_t *new_circular_buffer(int capacity)
{
    circular_buffer_t *buffer = malloc(sizeof(circular_buffer_t) + sizeof(buffer_value_t *));
    if (buffer == NULL)
    {
        errno = ENOMEM;
        return NULL;
    }

    buffer->capacity = capacity;
    buffer->elements = malloc(sizeof(buffer_value_t) * buffer->capacity);
    if (buffer->elements == NULL)
    {
        free(buffer);
        errno = ENOMEM;
        return NULL;
    }

    buffer->entry_qty = 0;
    buffer->head = 0;
    buffer->tail = 0;

    return buffer;
}

int write(circular_buffer_t *buffer, buffer_value_t value)
{
    if (buffer_full(buffer))
    {
        errno = ENOBUFS;
        return 1;
    }

    buffer->elements[buffer->tail] = value;
    buffer->entry_qty++;
    buffer->tail = (buffer->tail + 1) % buffer->capacity;

    return 0;
}

int overwrite(circular_buffer_t *buffer, buffer_value_t value)
{
    if (buffer_full(buffer))
    {
        buffer->elements[buffer->head] = value;
        buffer->head = (buffer->head + 1) % buffer->capacity;
    }
    else
    {
        buffer->elements[buffer->tail] = value;
        buffer->tail = (buffer->tail + 1) % buffer->capacity;
        buffer->entry_qty++;
    }

    return 0;
}

int read(circular_buffer_t *buffer, buffer_value_t *value)
{
    if (buffer_empty(buffer))
    {
        errno = ENODATA;
        return 1;
    }

    *value = buffer->elements[buffer->head];
    buffer->head = (buffer->head + 1) % buffer->capacity;
    buffer->entry_qty--;

    return 0;
}

void clear_buffer(circular_buffer_t *buffer)
{
    buffer->head = 0;
    buffer->tail = 0;
    buffer->entry_qty = 0;
}

void delete_buffer(circular_buffer_t *buffer)
{
    free(buffer->elements);
    free(buffer);
}

int buffer_empty(circular_buffer_t *buffer)
{
    return (buffer->entry_qty == 0);
}

int buffer_full(circular_buffer_t *buffer)
{
    return (buffer->entry_qty == buffer->capacity);
}