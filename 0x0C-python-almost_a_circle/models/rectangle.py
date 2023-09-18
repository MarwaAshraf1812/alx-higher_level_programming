#!/usr/bin/python3
"""
This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class to create a rectangle object
    with width, height, x, y, and id attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not type(x) is int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not type(y) is int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        Returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Returns printed rectangle with '#'
        y is newline, x is space
        """
        if self.__y != 0:
            for n in range(self.__y):
                print()
        hash_pattern = '#'
        for r in range(self.__height):
            print((self.__x * " ") + (self.__width * hash_pattern))

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """
        Updates rectangle values
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
