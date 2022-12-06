#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        first = None

    first = sentence[0]
    length = len(sentence)

    result = (length, first)
    return result
