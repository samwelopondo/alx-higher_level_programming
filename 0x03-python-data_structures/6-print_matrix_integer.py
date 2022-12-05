#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                end = ""
            else:
                end = " "
            print("{:d}".format(row[i]), end=end)
        print()
