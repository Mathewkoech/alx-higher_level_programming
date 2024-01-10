#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # create a new matrix with the same size as the input matrix

    squared_matrix = []
    # iterating into rows in matrix
    for i in matrix:
        row_result = []
        # Iterate through each element in the row and square elemnt value
        for j in i:
            squared_j = j ** 2
            row_result.append(squared_j)
        squared_matrix.append(row_result)
    return squared_matrix
