#!/usr/bin/python3
"""Defining an inherited list class MyList."""


class MyList(list):
    """Implementing a sorted printing for the built-in list class."""

    def print_sorted(self):
        """Printing a list in a sorted ascending order."""
        print(sorted(self))
