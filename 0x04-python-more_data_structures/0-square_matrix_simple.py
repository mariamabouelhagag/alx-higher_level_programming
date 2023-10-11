#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
       for x in range(len(matrix[i])):
           matrix[i][x] = matrix[i][x] ** 2
    return matrix
