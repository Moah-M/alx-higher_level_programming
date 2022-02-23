#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """ Function
    Args:
        filename: filename
        text: text
    Raises
        Exception: opened
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
