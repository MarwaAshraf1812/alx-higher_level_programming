#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return The area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[Square] {self.__size}/{self.__size}"
