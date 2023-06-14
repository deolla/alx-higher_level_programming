#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    f = list(map(lambda m: list(map(lambda x: m ** 2, m)), matrix))
    return f
