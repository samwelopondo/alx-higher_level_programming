#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {}:
        print()
        exit(0)

    result = {}
    lisp = list(a_dictionary.keys())
    lisp.sort()
    items = list(a_dictionary.items())

    for i in range(len(lisp)):
        result[lisp[i]] = items[i][1]

    for k, v in result.items():
        print(k, v)
