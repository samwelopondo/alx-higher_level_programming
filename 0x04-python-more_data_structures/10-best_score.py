#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())

    for i in range(len(values)):
        if values[i] == max(values):
            largest = i

    return keys[largest]
