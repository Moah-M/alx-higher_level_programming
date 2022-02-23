
#!/usr/bin/python3
"""
Contains the function append_wrtie
"""


def append_write(filename="", text=""):
    """ Function
    Args:
        filename: filename
        text: txt to write
    Raises
        Exception: open
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
