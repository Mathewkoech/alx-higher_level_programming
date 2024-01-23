#!/usr/bin/python3
"""Singley linked list """


class Node:
    """Class for node singley listed list.

    Attributes:
    Data(int): data stored in node
    Next_node: reps next node in list
    """
    def __init__(self, data, next_node=None):
        """Initialise data and next_node singley listed list.
        Attributes:
        Data(int): data stored in node
        Next_node: reps next node in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Raises:
            TypeError: If next_node is not a Node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
