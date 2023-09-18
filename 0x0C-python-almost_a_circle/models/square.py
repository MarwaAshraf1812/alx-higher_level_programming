#!/usr/bin/python3
"""
This module contains the Square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square.
    Inherits all attributes and methods of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get/set the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set a new width for this square
        size needs to be an int
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        return super().display()

    def update(self, *args, **kwargs):
        """Updates square values
        """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """Return the dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }