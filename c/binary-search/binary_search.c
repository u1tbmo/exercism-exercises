#include "binary_search.h"

const int *binary_search(int value, const int *arr, size_t length)
{
    // Initialize pointers to the start and end of the array
    int l = 0;
    int r = length - 1;

    // While we can still search the array
    while (l <= r)
    {
        // Calculate the middle index
        int mid = l + ((r - l) / 2);

        // Check if the value is in the middle array
        if (arr[mid] == value)
        {
            return &arr[mid];
        }

        // Check the left side if value < arr[mid]
        if (value < arr[mid])
        {
            r = mid - 1;
        }

        // Check the right side if value > arr[mid]
        if (value > arr[mid])
        {
            l = mid + 1;
        }
    }

    // If we didn't find the value in the array
    return NULL;
}