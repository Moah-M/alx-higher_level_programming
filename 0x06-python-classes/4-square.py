#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation
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

    @property
    def size(self):
        """getter
        Returns:
            The size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value (int): the size of square
        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
