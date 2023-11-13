#!/usr/bin/python3

class Base:
        """Represent the base model.

    Represents the "base" for all other classes in this project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """


    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
