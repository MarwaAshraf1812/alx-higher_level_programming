#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Returns The integer addition of a and b.
    :param int a: First number to be added together.
    :type a: int
    :param int b: Second Number to be added together.
    :type b: int
    Float arguments are typecasted to integer before addition
    raises:
    TypeError : If either argument is not an Integer or float.
    return (a + b)
    """

    if not type(a) in (int, float):
        raise TypeError("a must be an integer")
    if  not type(b) in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
