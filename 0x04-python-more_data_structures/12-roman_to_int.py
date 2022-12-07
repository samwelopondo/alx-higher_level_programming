#!/usr/bin/python3

def roman_to_int(roman_string):
    a_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
         }

    a_list = list(roman_string)
    result = 0
    # print("Original dict: {}".format(a_dict))
    if roman_string in a_dict:
        return a_dict[roman_string]

    for i in range(len(a_list)):
        result += a_dict[a_list[i]]
        # print("i: {} val: {}".format(a_list[i], a_dict[a_list[i]]))

    return result
