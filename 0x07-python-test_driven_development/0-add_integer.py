#!/usr/bin/python3
""" Define"""


def add_integer(a, b=98):
    """ Func
    Args:
        a: 1
        b: 2
    Returns:
        addition
    Raises:
        TypeError: If a or b are not integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
