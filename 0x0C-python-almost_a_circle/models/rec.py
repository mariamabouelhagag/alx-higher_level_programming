#!/usr/bin/python3
"""the Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle
        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
            x: The x coordinate of the new Rectangle.
            y: The y coordinate of the new Rectangle.
            id: The identity of the new Rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property:
    def width(self):
        """width Getter"""
        return self.__width


    @width.setter:
    def width(self, val):
        """width Setter"""
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter x"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter y"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
