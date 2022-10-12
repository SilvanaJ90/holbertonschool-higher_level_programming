#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Doc """
    def __init__(self, width, height):
        """ Doc """
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
