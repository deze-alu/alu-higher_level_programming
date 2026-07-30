#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node with the given data and next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node after validating its type."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node of the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node after validating that it is a Node or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Returns the list with one node value per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node in the correct sorted position of the list."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while (current.next_node is not None and
                current.next_node.data < value):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
