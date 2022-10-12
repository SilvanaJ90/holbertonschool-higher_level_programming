#!/usr/bin/python3
""" Doc """


class BaseGeometry:
    """ main class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height  

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ sub class """
    
    def integer_validator(self, name,  width, height):
        if type(self.__height) is not int:
            raise TypeError("{} must be an integer".format(name))
        if type(self.__width) is not int:
            raise TypeError("{} must be an integer".format(name))
        if self.__height  <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if self.__width  <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        print(issubclass(Rectangle, BaseGeometry))
  




