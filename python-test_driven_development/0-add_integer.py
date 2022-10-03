#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module is function that adds 2 integers, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ Returns an integer: the addition of a and b

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
