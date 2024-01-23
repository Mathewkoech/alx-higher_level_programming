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
    """
    SinglyLinkedList class represents a singly linked list.

    Attributes:
        head: Reference to the first node in the list.
    """
    def __init__(self):
        """initialise empty list"""
        self.head = None
    def sorted_insert(self, value):

        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
