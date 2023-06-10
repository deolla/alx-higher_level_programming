#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print('{:2d}'.format(row[col]), end='')
        print()
