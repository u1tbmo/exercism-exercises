#ifndef PHONE_NUMBER_H
#define PHONE_NUMBER_H

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define INVALID_NUMBER "0000000000"

char *phone_number_clean(const char *input);
char *invalid_number(char *invalid_number);

#endif
