#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    result = {}
    lisp = list(a_dictionary.keys())
    lisp.sort()
    items = list(a_dictionary.items())
    # This is a comment
    for i in range(len(lisp)):
        for j in range(len(items)):
            if lisp[i] == items[j][0]:
                result[lisp[i]] = items[j][1]

    for k, v in result.items():
        print("{:s} {}".format(k, v))
