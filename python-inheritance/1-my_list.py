#!/usr/bin/python3
"""Provides a list subclass able to print itself sorted."""


class MyList(list):
    """Represents a list that can print its elements in ascending order."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
