#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        tot = 0
        prev = 1001
        for c in roman_string:
            if rom_dict[c] > prev:
                tot += rom_dict[c] - (prev * 2)
            else:
                tot += rom_dict[c]
            prev = rom_dict[c]
        return tot
    return 0
