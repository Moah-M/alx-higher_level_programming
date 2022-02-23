#!/usr/bin/python3
"""
Contains function
"""


import json


def to_json_string(my_obj):
    """ Function 
    Args:
        my_obj: object
    Raises:
        Exception: wencode
    """
    return json.dumps(my_obj)
