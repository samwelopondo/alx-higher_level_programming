#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        result.append([row[i] ** 2 for i in range(len(matrix[0]))])
    return result
