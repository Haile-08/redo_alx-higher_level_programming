#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    if not roman_string:
        return 0
    roman_map = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(roman_string);
    total = 0

    for i in range(length):
        if i < length - 1:
            current_value = roman_map.get(roman_string[i], 0)
            next_value = roman_map.get(roman_string[i + 1], 0)
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return total

