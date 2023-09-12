#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return The area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
