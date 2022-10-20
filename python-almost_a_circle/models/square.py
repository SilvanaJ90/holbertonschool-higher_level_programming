#!/usr/bin/python3
"""
Class Square inhere Rectangle
"""


from models.rectangle import Base, Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter size"""
        return super().width

    @size.setter
    def size(self, size):
        """ setter size """
        self.width = size
        self.height = size
