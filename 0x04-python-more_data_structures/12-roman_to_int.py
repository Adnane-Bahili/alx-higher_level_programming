#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    R_N = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    nmbr_dig = 0
    for n in range(len(roman_string)):
        if R_N.get(roman_string[n], 0) == 0:
            return (0)
        if (n != (len(roman_string) - 1) and
                R_N[roman_string[n]] < R_N[roman_string[n + 1]]):
            nmbr_dig += R_N[roman_string[n]] * -1
        else:
            nmbr_dig += R_N[roman_string[n]]
    return (nmbr_dig)
