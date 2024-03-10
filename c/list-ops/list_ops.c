#include "list_ops.h"

list_t *new_list(size_t length, list_element_t elements[])
{
    // Allocate memory for the structure (list) and check if memory has been allocated
    list_t *list = malloc(sizeof(list_t) + sizeof(list_element_t) * length);
    if (list == NULL)
    {
        return NULL;
    }

    // Set the length
    list->length = length;

    // Copy the elements
    for (size_t i = 0; i < length; i++)
    {
        list->elements[i] = elements[i];
    }

    return list;
}

list_t *append_list(list_t *list1, list_t *list2)
{
    // Get the new length of the new list
    size_t length = list1->length + list2->length;

    // Allocate memory
    list_t *list = malloc(sizeof(list_t) + sizeof(list_element_t) * length);
    if (list == NULL)
    {
        return NULL;
    }

    // Set the length
    list->length = length;

    // Copy elements
    memcpy(list->elements, list1->elements, sizeof(list_element_t) * list1->length);
    memcpy(list->elements + list1->length, list2->elements, sizeof(list_element_t) * list2->length);

    return list;
}

list_t *filter_list(list_t *list, bool (*filter)(list_element_t))
{
    // Allocate memory (assumes that the filtered_list will be as large as the original list)
    list_t *filtered_list = malloc(sizeof(list_t) + sizeof(list_element_t) * list->length);
    if (filtered_list == NULL)
    {
        return NULL;
    }

    // Initialize length
    filtered_list->length = 0;

    // Iterate through every element in the original list and add to the filtered list if it satisfies the filter
    for (size_t i = 0; i < list->length; i++)
    {
        if (filter(list->elements[i]))
        {
            filtered_list->elements[filtered_list->length] = list->elements[i];
            filtered_list->length++;
        }
    }

    // Shrink memory to actual size
    filtered_list = (list_t *)realloc(filtered_list, sizeof(list_t) + sizeof(list_element_t) * filtered_list->length);
    if (filtered_list == NULL)
    {
        free(filtered_list);
        return NULL;
    }

    return filtered_list;
}

size_t length_list(list_t *list)
{
    // Return the length of the list
    return list->length;
}

list_t *map_list(list_t *list, list_element_t (*map)(list_element_t))
{
    // Allocate memory
    list_t *mapped_list = malloc(sizeof(list_t) + sizeof(list_element_t) * list->length);
    if (mapped_list == NULL)
    {
        return NULL;
    }

    // Set the length
    mapped_list->length = list->length;

    // Apply the function to each element in the original list and add to the new list
    for (size_t i = 0; i < list->length; i++)
    {
        mapped_list->elements[i] = map(list->elements[i]);
    }

    return mapped_list;
}

list_element_t foldl_list(list_t *list, list_element_t initial, list_element_t (*foldl)(list_element_t, list_element_t))
{
    // Iterates over each element in the list, applying the foldl function to the current initial value.
    for (size_t i = 0; i < list->length; i++)
    {
        initial = foldl(initial, list->elements[i]);
    }
    return initial;
}

list_element_t foldr_list(list_t *list, list_element_t initial, list_element_t (*foldr)(list_element_t, list_element_t))
{
    // Iterates over each element in the list in reverse order, applying the foldr function to the current initial value.
    for (int i = (int)(list->length - 1); i >= 0; i--)
    {
        initial = foldr(list->elements[i], initial);
    }
    return initial;
}

list_t *reverse_list(list_t *list)
{
    // Allocate memory
    list_t *reversed_list = malloc(sizeof(list_t) + sizeof(list_element_t) * list->length);
    if (reversed_list == NULL)
    {
        return NULL;
    }

    // Set the length
    reversed_list->length = list->length;

    // Iterate through each item in the original list in reverse and copy to the reversed list
    for (size_t i = 0; i < reversed_list->length; i++)
    {
        reversed_list->elements[i] = list->elements[reversed_list->length - 1 - i];
    }

    return reversed_list;
}

void delete_list(list_t *list)
{
    free(list);
}