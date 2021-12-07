#!/usr/bin/python3
"""Definition"""


class Square:
    """Representer
    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0):
        """initializer
        Args:
            size (int): size of the square
        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculator
        Returns:
            The area of the square
        """

        return self.__size ** 2
