#include "clock.h"

clock_t clock_create(int hour, int minute)
{
    // Variables
    char hour_str[3] = "00";
    char minute_str[3] = "00";
    char time[MAX_STR_LEN];
    clock_t new_clock;

    while (minute < 0 || minute >= 60)
    {
        if (minute < 0)
        {
            minute += 60;
            hour -= 1;
        }
        else if (minute >= 60)
        {
            minute -= 60;
            hour += 1;
        }
    }

    while (hour < 0 || hour >= 24)
    {
        if (hour < 0)
        {
            hour += 24;
        }
        else if (hour >= 24)
        {
            hour -= 24;
        }
    }

    // Conversion to string
    sprintf(hour_str, "%02d", hour);
    sprintf(minute_str, "%02d", minute);

    // Set up string representation
    strcpy(time, hour_str);
    strcpy(time + 3, minute_str);
    time[2] = ':';
    strcpy(new_clock.text, time);
    return new_clock;
}
clock_t clock_add(clock_t clock, int minute_add)
{
    // Variables
    char hour_str[3];
    char minute_str[3];
    int hour, minute;

    // Get hours and minutes from clock
    for (int i = 0, l = strlen(clock.text); i < l; i++)
    {
        if (i < 2)
        {
            hour_str[i] = clock.text[i];
        }
        else if (i > 2)
        {
            minute_str[i - 3] = clock.text[i];
        }
    }

    // Convert to integers
    sscanf(hour_str, "%d", &hour);
    sscanf(minute_str, "%d", &minute);

    return clock_create(hour, minute + minute_add);
}

clock_t clock_subtract(clock_t clock, int minute_subtract)
{
    // Variables
    char hour_str[3];
    char minute_str[3];
    int hour, minute;

    // Get hours and minutes from clock
    for (int i = 0, l = strlen(clock.text); i < l; i++)
    {
        if (i < 2)
        {
            hour_str[i] = clock.text[i];
        }
        else if (i > 2)
        {
            minute_str[i - 3] = clock.text[i];
        }
    }

    // Convert to integers
    sscanf(hour_str, "%d", &hour);
    sscanf(minute_str, "%d", &minute);

    return clock_create(hour, minute - minute_subtract);
}
bool clock_is_equal(clock_t a, clock_t b)
{
    return strcmp(a.text, b.text) == 0;
}
