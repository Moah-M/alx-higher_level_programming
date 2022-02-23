#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation
    Attributes:
        __size (int): size of the square.
    """

    def __init__(self, size=0):
        """initializer
        Args:
            size (int): size of the square
        Returns:
            None
        """

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter
        Returns:
            The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value (int): size of the square
        Returns:
            None
        """

        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculator
        Returns:
            area
        """

        return self.__size ** 2

    def my_print(self):
        """print
        Returns:
            None
        """

        if not self.__size:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
