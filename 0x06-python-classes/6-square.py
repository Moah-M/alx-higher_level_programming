#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation
    Attributes:
        __size (int): size of the square
        __position (tuple): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializer
        Args:
            size (int): size of the square
            position (tuple): position
        Returns:
            None
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter
        Returns:
            position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """setter
        Args:
            value (int): position
        Returns:
            None
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculator
        Returns:
            The area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """printer
        Returns:
            None
        """

        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(0, self.size):
                for y in range(self.position[0]):
                    print(" ", end='')
                for z in range(self.size):
                    print("#", end='')
                print()
