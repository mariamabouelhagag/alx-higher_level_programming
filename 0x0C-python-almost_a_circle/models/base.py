#!/usr/bin/python3

"""the base class"""


class Base:
    """the base class for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
