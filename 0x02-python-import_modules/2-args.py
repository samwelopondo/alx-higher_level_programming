#!/usr/bin/python3
import sys

length = len(sys.argv) - 1

if length == 1:
    print("{} argument:".format(length))
    print("1: {}".format(sys.argv[1]))

elif length == 0:
    print("{} arguments.".format(length))

else:
    print("{} arguments:".format(length))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
