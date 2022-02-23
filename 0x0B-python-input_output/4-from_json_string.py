#!/usr/bin/python3
"""
Contains the "from_json_string" function
"""


import json


def from_json_string(my_str):
    """ Function
    Args:
        my_str: JSON
    Raises:
        Exception: decode
    """
    return json.loads(my_str)
