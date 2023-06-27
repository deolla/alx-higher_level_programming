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
            next_node (Node):  The reference to the next node.

        Raises:
            TypeError: If data is not an integer or next_node is not None.
        """
        self.data = data
        self.next_node = next_node

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
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.

    Attributes:
        head: The first node of linked list.
    """

    def __init__(self):
        """
        Initialise an empty linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the linked list.

        Args:
            values: The value to be inserted.

        Raises:
            TypeError: If value is not an integer.
        """

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a strings representation of the linked list.

        Returns:
                str: The string representation of linked list.
        """
        output = []
        current = self.__head
        while current is not None:
            output.append(str(current.data))
            current = current.next_node
        return ('\n'.join(output))
