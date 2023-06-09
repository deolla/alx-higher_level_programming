#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    m1 = tuple_a[0] if len(tuple_a) > 0 else 0
    m2 = tuple_a[1] if len(tuple_a) > 1 else 0
    n1 = tuple_b[0] if len(tuple_b) > 0 else 0
    n2 = tuple_b[1] if len(tuple_b) > 1 else 0

    result = (m1 + n1, m2 + n2)
    return (result)
