#!/usr/bin/python3
"""Definition"""


class Square:
    """square
    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of square
        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
