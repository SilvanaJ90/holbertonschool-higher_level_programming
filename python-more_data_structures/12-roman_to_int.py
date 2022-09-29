#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_string = {"X": 10, "VII": 10, "IX": 10, "LXXXVII": 10, "DCCVII": 10}
    for key, value in roman_string.items():
        while key != None:
            return roman_string.replace(key, value)
