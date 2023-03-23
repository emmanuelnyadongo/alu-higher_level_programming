#!/usr/bin/python3
"""Defining a class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using the above BaseGeometry."""

    def __init__(self, width, height):
        """Intializes a fresh rectangle.
        Args:
            width (int): The width of our new rectangle.
            height (int): The height of our new rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of our rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representing  a rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
