#!/usr/bin/python3

"""
This is a class node that defines a node of singly linked list.
"""


class Node:
    """
    This class represent a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a node instance with the given data and next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node):  The reference to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not None or a None Object.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
                int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""
This class defines a singly linked list.
"""


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        __head: The head of a linked list.
    """
    def __init__(self):
        """
        Initialise an empty linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a strings representation of the linked list.
        """
        if self.__head is None:
            return ""

        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the linked list.

        Args:
            values: The value to be inserted.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
