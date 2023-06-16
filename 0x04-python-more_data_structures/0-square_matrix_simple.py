#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for a in range(len(matrix)):
        new_matrix[a] = list(map(lambda x: x**2, matrix[a]))

    return (new_matrix)
