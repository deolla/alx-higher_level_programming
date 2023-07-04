#!/usr/bin/python3

"""
Module composed by a function that multiplies 2 matrices

Requirements:
- m_a and m_b must be lists of lists representing matrices
- The matrices must be compatible for multiplication
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices using the module NumPy.
    
    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: The result of the multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """

    return np.matmul(m_a, m_b)
