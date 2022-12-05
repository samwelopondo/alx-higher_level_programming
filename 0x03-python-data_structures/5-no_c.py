#!/usr/bin/python3

def no_c(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == 'c':
            my_string[i] = ' '
    _str = ""
    for element in my_string:
        _str += element
    return _str
