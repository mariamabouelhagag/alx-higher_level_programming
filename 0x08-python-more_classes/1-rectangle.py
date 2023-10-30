#!/usr/bin/python3
class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0

    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
