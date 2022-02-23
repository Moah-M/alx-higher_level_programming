#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation
    Attributes:
        __size (int): size 
    """

    def __eq__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size == other.__size

    def __lt__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size < other.__size

    def __le__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size <= other.__size

    def __ne__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size != other.__size

    def __gt__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size > other.__size

    def __ge__(self, other):
        """Comparison
        Args:
            other (Square): square
        Returns:
            True or False
        """

        return self.__size >= other.__size

    def __init__(self, size=0):
        """initializer
        Args:
            size (int): size
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
            The area
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """getter
        Returns:
            size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value (int): the size
        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
