#!/usr/bin/python3
"""Definition"""


class Node:
    """Representation
    Attributes:
        __data (int): data
        __next_node (Node): next node
    """

    def __init__(self, data, next_node=None):
        """Initializer
        Args:
            data (int): data
            next_node (Node): next node
        Returns:
            None
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter
        Returns:
            data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """setter
        Args:
            value (int): data
        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter
        Returns:
           the next node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter
        Args:
            value (Node): next node
        Returns:
            None
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Definition """


class SinglyLinkedList:
    """Representation
    Attributes:
        __head (Node): head
    """

    def __init__(self):
        """Initializer
        Returns:
            None
        """

        self.__head = None

    def __str__(self):
        """representation
        Returns:
            Format
        """

        rtn = ""
        pt = self.__head

        while pt is not None:
            rtn += str(pt.data)
            if pt.next_node is not None:
                rtn += "\n"
            pt = pt.next_node

        return rtn

    def sorted_insert(self, value):
        """ insert
        Args:
            value (int): data
        Returns:
            None
        """

        pt = self.__head

        while pt is not None:
            if pt.data > value:
                break
            pt_prev = pt
            pt = pt.next_node

        new_node = Node(value, pt)
        if pt == self.__head:
            self.__head = new_node
        else:
            pt_prev.next_node = new_node
