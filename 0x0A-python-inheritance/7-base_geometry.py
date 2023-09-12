#!/usr/bin/python3
"""module base_geometry"""


class BaseGeometry():
    """class with public instance methods"""
    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate a perimeter as an integer"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
