#!/usr/bin/python3
"""the rectangle class."""

from .base import Base

class Rectangle(Base):
    """Represent the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
     """Initialize a new rectangle"""
     self.__width = width
     self.__height = height
     self.__x = x
     self.__y = y
     super().__init__(id)
