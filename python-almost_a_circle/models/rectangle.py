#!/usr/bin/python3
"""
class base
"""


class Base:
    """ Doc """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None): 
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """ Doc """

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x
    
    @y.setter
    def y(self, y):
        self.__y = y