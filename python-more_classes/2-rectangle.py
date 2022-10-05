#!/usr/bin/python3
""" This is empty class """


class Rectangle:
    """ create rectangle """

    def __init__(self, width=0, height=0, perimeter=0):
        self.__width = width
        self.__height = height
        self.perimeter = perimeter

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return self.perimeter

    def perimeter.setter(self,perimeter):
        if width or height == 0:
            perimeter = 0
