#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for lists in new_matrix:
        for idx in range(0, len(lists)):
            lists[idx] = lists[idx]**2
    return new_matrix
