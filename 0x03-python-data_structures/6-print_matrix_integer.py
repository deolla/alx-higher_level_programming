#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for m, element in enumerate(row):
            print("{:d}".format(element), end=" ")
        print()
