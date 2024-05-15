#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        newrow = []
        for num in row:
            newrow.append(num**2)
        newmatrix.append(newrow)
    return newmatrix
