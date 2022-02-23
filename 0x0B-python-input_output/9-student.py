#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary"""
        return self.__dict__
