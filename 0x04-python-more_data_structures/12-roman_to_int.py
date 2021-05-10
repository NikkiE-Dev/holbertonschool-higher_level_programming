#!/usr/bin/python3
def roman_to_int(roman_string):
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if not isinstance(roman_string, str) or if roman_string is None:
        return 0
    for i in range(len(roman_number)):
        if i > 0 and conv[roman_string[i]] > conv[roman_string[i - 1]]:
            result += conv[roman_string[i]] - 2 * conv[roman_string[i - 1]]
        else:
            result += conv[roman_string[i]]
    return result
