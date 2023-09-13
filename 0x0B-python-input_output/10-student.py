#!/usr/bin/python3
"""
Represents a student with attributes such as first name, last name, and age.
"""


class Student:
    """
    Define a class student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance."""
        if (type(attrs) == list and
                all(type(element)  == str) for element in attrs):
            return {i: getattr(self, attrs) for i in element}
