#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if len(sentence) == 0:
        first = None

    first = sentence[0]

    result = (length, first)
    return result
