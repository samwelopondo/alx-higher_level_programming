#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b

    list_a = list(a)
    list_b = list(b)
    result = ()
    if len(list_b) == 0:
        list_b = [0, 0]

    if len(list_b) == 1:
        list_b.append(0)

    if len(list_b) > 2:
        list_b = list_b[:2]

    a = tuple(list_a)
    b = tuple(list_b)
    for c, d in zip(a, b):
        sumw = ((c + d),)
        result += sumw
    return result
