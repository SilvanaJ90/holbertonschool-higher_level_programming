#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        super().integer_validator("width", width)
        super().
