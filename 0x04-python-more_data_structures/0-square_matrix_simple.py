#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda n: n**2, new_list)) for new_list in matrix]
