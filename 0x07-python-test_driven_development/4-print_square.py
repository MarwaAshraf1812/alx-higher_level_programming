#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Print a square made of '#' characters with the specified size.

    Args:
    size (int): The size of the square (number of rows and columns).

    Returns:
    None: This function doesn't return a value, it prints the square directly.
    """

    if type(size) is not int:
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size) 
