#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation
    Attributes:
        __size (int): size of the square
        __position (tuple): position
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializer
        Args:
            size (int): size 
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
            The size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value (int): size
        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
            value (tuple): position
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
            area
        """

        return (self.__size ** 2)

    def my_print(self):
        """print
        Returns:
            None
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    def __str__(self):
        """String representation
        Returns:
            Formatted
        """

        rn = ""

        if self.size == 0:
            return rn

        for i in range(self.position[1]):
            rn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rn += " "
            for j in range(self.size):
                rn += "#"
            if i is not (self.size - 1):
                rn += "\n"

        return rn
