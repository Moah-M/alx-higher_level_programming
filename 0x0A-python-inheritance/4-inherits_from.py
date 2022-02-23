#!/usr/bin/python3
"""
inherits_from function
"""


def inherits_from(obj, a_class):
    """ Function that returns True/False
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
