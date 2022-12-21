#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}

    lisp = list(a_dictionary.values())

    for a, b in a_dictionary.items():
        result[a] = b*2
    return result
