#!/usr/bin/python3
"""Defines a base class of all other classes in this project"""


class Base:
    """The goal of this class is to manage `id` attribute in all your future
    classes and to avoid dulicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the class

        Args:
            id (int): The class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
