def roman(number):
    number_of_digits = len(str(number))
    dummy = number
    roman_numeral = ''
    count_I, count_X, count_C, count_M = 0, 0, 0, 0

    while dummy > 0: # while the remainder is not 0
        number_of_digits = len(str(dummy))
        match number_of_digits:
            case 4:
                count_M = dummy // 1000 # count the number of M's
                dummy = dummy % 1000 # get the remainder
                roman_numeral += 'M' * count_M # add the number of M's to the roman numeral
            case 3:
                count_C = dummy // 100 # number of C's
                if count_C == 4:
                    roman_numeral += 'CD'
                    count_C = 0
                    dummy = dummy % 100
                elif count_C == 5:
                    roman_numeral += 'D'
                    count_C = 0
                    dummy = dummy % 100
                elif count_C == 9:
                    roman_numeral += 'CM'
                    count_C = 0
                    dummy = dummy % 100
                else:
                    # if none of the above work, try subtracting 500 from the dummy, if it is positive, add a D and repeat case 3
                    if dummy - 500 > 0:
                        roman_numeral += 'D'
                        dummy -= 500
                    # otherwise, add C count_C times
                    else:
                        dummy = dummy % 100
                        roman_numeral += 'C' * count_C
            case 2:
                count_X = dummy // 10 # count the number of X's
                if count_X == 4:
                    roman_numeral += 'XL'
                    count_X = 0
                    dummy = dummy % 10
                elif count_X == 5:
                    roman_numeral += 'L'
                    count_X = 0
                    dummy = dummy % 10
                elif count_X == 9:
                    roman_numeral += 'XC'
                    count_X = 0
                    dummy = dummy % 10
                else:
                    # if none of the above work, try subtracting 50 from the dummy, if it is positive, add a L and repeat case 3
                    if dummy - 50 > 0:
                        roman_numeral += 'L'
                        dummy -= 50
                    # otherwise, add X count_X times
                    else:
                        dummy = dummy % 10
                        roman_numeral += 'X' * count_X
            case 1:
                count_I = dummy // 1 # count the number of I's
                if count_I == 4:
                    roman_numeral += 'IV'
                    count_I = 0
                    dummy = 0
                elif count_I == 5:
                    roman_numeral += 'V'
                    count_I = 0
                    dummy = 0
                elif count_I == 9:
                    roman_numeral += 'IX'
                    count_I = 0
                    dummy = 0
                else:
                    # if none of the above work, try subtracting 5 from the dummy, if it is positive, add a V and repeat case 1
                    if dummy - 5 > 0:
                        roman_numeral += 'V'
                        dummy -= 5
                    # otherwise, add I count_I times
                    else:
                        roman_numeral += 'I' * count_I
                        dummy = 0

    return roman_numeral